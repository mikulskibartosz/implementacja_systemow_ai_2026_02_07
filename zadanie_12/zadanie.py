import mlflow
import mlflow.sklearn
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
from mlflow.models.signature import infer_signature
import os

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

mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("Palmer Penguins-Klasyfikacja")

param_sets = [
    {"n_estimators": 50, "max_depth": 5, "min_samples_split": 2, "random_state": 42},
    {"n_estimators": 100, "max_depth": 10, "min_samples_split": 2, "random_state": 42},
    {"n_estimators": 200, "max_depth": 15, "min_samples_split": 5, "random_state": 42},
    {"n_estimators": 100, "max_depth": None, "min_samples_split": 10, "random_state": 42},
    {"n_estimators": 150, "max_depth": 8, "min_samples_split": 3, "random_state": 42}
]

for i, params in enumerate(param_sets):
    with mlflow.start_run(run_name=f"RandomForestClassifier_{i}"):
        print(f"Trenowanie modelu z parametrami: {i} {params}")
        mlflow.log_params(params)

        model = RandomForestClassifier(**params)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='macro')
        recall = recall_score(y_test, y_pred, average='macro')
        f1 = f1_score(y_test, y_pred, average='macro')

        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1", f1)

        model_signature = infer_signature(X_test, y_pred)
        mlflow.sklearn.log_model(model, "model", signature=model_signature, input_example=X_test[:5])

        encoder_signature = infer_signature(X_categorical, encoded_features)
        mlflow.sklearn.log_model(encoder, "encoder", signature=encoder_signature, input_example=X_categorical[:5])

        current_file = os.path.abspath(__file__)
        mlflow.log_artifact(current_file)