import mlflow
import optuna
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from optuna.integration.mlflow import MLflowCallback
import os

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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

    score = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    mean_score = score.mean()

    return mean_score

mlflow_callback = MLflowCallback(
    tracking_uri=mlflow.get_tracking_uri(),
    metric_name="accuracy",
)

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=10, callbacks=[mlflow_callback])


best_params = study.best_params
best_model = RandomForestClassifier(
    n_estimators=best_params['n_estimators'],
    max_depth=best_params['max_depth'],
    min_samples_split=best_params['min_samples_split'],
    min_samples_leaf=best_params['min_samples_leaf'],
    bootstrap=best_params['bootstrap'],
    random_state=42
)

with mlflow.start_run(run_name="Best Model", nested=True):
    best_model.fit(X_train, y_train)

    for param, value in best_params.items():
        mlflow.log_param(f"best_{param}", value)

    mlflow.log_metric("best_score", study.best_value)
    mlflow.log_metric("test_score", best_model.score(X_test, y_test))

    mlflow.sklearn.log_model(best_model, "best_model")

    current_file = os.path.abspath(__file__)
    mlflow.log_artifact(current_file)