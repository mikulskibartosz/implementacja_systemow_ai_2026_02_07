import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import os
import pandas as pd
import numpy as np
from mlflow.models.signature import infer_signature

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

mlflow.set_experiment("iris-experiment")

with mlflow.start_run(run_name="LogisticRegression"):
    params = {
        "C": 1.0,
        "penalty": "l2",
    }

    mlflow.log_params(params)
    mlflow.log_param("test_size", 0.2)

    model = LogisticRegression(**params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)

    signature = infer_signature(X_test, y_pred)
    mlflow.sklearn.log_model(model, "model", signature=signature, input_example=X_test[:5])

    current_file = os.path.abspath(__file__)
    mlflow.log_artifact(current_file)

    iris_df = pd.DataFrame(data=np.c_[iris.data, iris.target], columns=iris.feature_names + ["target"])
    iris_df.to_csv("iris_df.csv", index=False)
    mlflow.log_artifact("iris_df.csv")

    mlflow.set_tag("model_type", "LogisticRegression")
