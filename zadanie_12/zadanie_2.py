import os

import mlflow
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score
from mlflow.models.signature import infer_signature

mlflow.set_experiment("Palmer Penguins-Klasyfikacja")

df = fetch_openml(data_id=42585)
df = df["frame"]
df.dropna(inplace=True)
df.reset_index(inplace=True, drop=True)

y = df.species
X = df.drop("species", axis=1)

categorical_features = ["island", "sex"]
numerical_features = X.columns.drop(categorical_features).to_list()

# Split raw data first so pipeline sees the same train/test structure
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

with mlflow.start_run(run_name="RandomForestClassifier"):
    params = {
        "classifier__n_estimators": 4,
        "classifier__max_depth": 3,
        "classifier__min_samples_split": 2,
    }

    preprocessor = ColumnTransformer(
        [
            ("cat", OneHotEncoder(sparse_output=False), categorical_features),
            ("num", "passthrough", numerical_features),
        ]
    )
    pipeline = Pipeline(
        [
            ("preprocessor", preprocessor),
            ("classifier", RandomForestClassifier(random_state=42)),
        ]
    )
    pipeline.fit(X_train, y_train)

    mlflow.log_params(params)
    mlflow.log_param("random_state", 42)
    mlflow.log_param("test_size", 0.2)

    y_pred = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)

    # Single artifact: pipeline = encoder + model; signature on raw input
    signature = infer_signature(X_test, y_pred)
    input_example = X_test.head(5).copy()
    for col in categorical_features:
        input_example[col] = input_example[col].astype(str)
    mlflow.sklearn.log_model(
        pipeline, "model", signature=signature, input_example=input_example
    )

    current_file = os.path.abspath(__file__)
    mlflow.log_artifact(current_file)

    mlflow.set_tag("model_type", "RandomForestClassifier")

print("Eksperyment zakończony")