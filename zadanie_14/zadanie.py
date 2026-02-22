import mlflow
import optuna
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, KFold
from optuna.integration.mlflow import MLflowCallback
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import os
import optuna.visualization as vis
from mlflow.models.signature import infer_signature


df = fetch_openml(data_id=42585)
df = df['frame']
df = df.dropna()

X = df.drop(columns=['species'])
y = df['species']


encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
X_categorical = X[['sex', 'island']].copy()
X_numerical = X.drop(columns=['sex', 'island']).copy()

encoded_features = encoder.fit_transform(X_categorical)
encoded_feature_names = encoder.get_feature_names_out(['sex', 'island'])

encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_names, index=X.index)
encoded_df = pd.concat([X_numerical, encoded_df], axis=1)

X_train, X_test, y_train, y_test = train_test_split(encoded_df, y, test_size=0.2, random_state=42)

cv = KFold(n_splits=5, shuffle=True, random_state=42)

def objective(trial):
    n_estimators = trial.suggest_int('n_estimators', 50, 300, step=50)
    max_depth = trial.suggest_categorical('max_depth', [None, 5, 10, 15, 20])
    min_samples_split = trial.suggest_categorical('min_samples_split', [2, 5, 10])
    min_samples_leaf = trial.suggest_categorical('min_samples_leaf', [1, 2, 4])
    bootstrap = trial.suggest_categorical('bootstrap', [True, False])

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        bootstrap=bootstrap,
        random_state=42
    )

    val_scores = []

    for step, (train_idx, val_idx) in enumerate(cv.split(X_train, y_train)):
        X_train_cv, X_val_cv = X_train.iloc[train_idx], X_train.iloc[val_idx]
        y_train_cv, y_val_cv = y_train.iloc[train_idx], y_train.iloc[val_idx]

        model.fit(X_train_cv, y_train_cv)
        val_score = model.score(X_val_cv, y_val_cv)
        val_scores.append(val_score)
        trial.report(val_score, step)

        if trial.should_prune():
            raise optuna.exceptions.TrialPruned()

    return sum(val_scores) / len(val_scores)

mlflow_callback = MLflowCallback(
    tracking_uri=mlflow.get_tracking_uri(),
    metric_name="accuracy",
)

study = optuna.create_study(direction='maximize', pruner=optuna.pruners.MedianPruner())
study.optimize(objective, n_trials=20, callbacks=[mlflow_callback])

best_params = study.best_params
best_model = RandomForestClassifier(
    n_estimators=best_params['n_estimators'],
    max_depth=best_params['max_depth'],
    min_samples_split=best_params['min_samples_split'],
    min_samples_leaf=best_params['min_samples_leaf'],
    bootstrap=best_params['bootstrap'],
    random_state=42
)
best_model.fit(X_train, y_train)

with mlflow.start_run(run_name="Best Model", nested=True):
    for param, value in best_params.items():
        mlflow.log_param(f"best_{param}", value)

    mlflow.log_metric("best_score", study.best_value)

    print("Train score: ", study.best_value)
    y_pred = best_model.predict(X_test)
    test_score = best_model.score(X_test, y_test)
    mlflow.log_metric("test_score", test_score)
    print("Test score: ", test_score)

    mlflow.sklearn.log_model(best_model, "best_model", signature=infer_signature(X_train, y_train))
    mlflow.sklearn.log_model(encoder, "encoder", signature=infer_signature(X_train, encoded_features))

    current_file = os.path.abspath(__file__)
    mlflow.log_artifact(current_file)

    mlflow.register_model(
        f"runs:/{mlflow.active_run().info.run_id}/best_model",
        "PenguinsClassifier"
    )

    print("Generowanie wykresów...")
    artifact_dir = "optuna_artifacts"
    os.makedirs(artifact_dir, exist_ok=True)

    fig = vis.plot_optimization_history(study)
    fig.write_image(f"{artifact_dir}/optimization_history.png")

    fig = vis.plot_contour(study, params=['n_estimators', 'min_samples_split', 'min_samples_leaf', 'bootstrap', 'max_depth'])
    fig.write_image(f"{artifact_dir}/contour_plot.png")

    fig = vis.plot_parallel_coordinate(study)
    fig.write_image(f"{artifact_dir}/parallel_coordinate.png")

    fig = vis.plot_slice(study)
    fig.write_image(f"{artifact_dir}/slice_plot.png")

    mlflow.log_artifacts(artifact_dir)