import mlflow

iris_features = [5.1, 3.5, 1.4, 0.2]

run_id = "90bcd1086f384bf4b1d0a33479d1fac0"
model_uri = f"runs:/{run_id}/model"

loaded_model = mlflow.sklearn.load_model(model_uri)
print(loaded_model)

prediction = loaded_model.predict([iris_features])
print(prediction)