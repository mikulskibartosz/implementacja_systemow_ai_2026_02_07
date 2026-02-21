import mlflow

iris_features = [5.1, 3.5, 1.4, 0.2]

run_id = "90bcd1086f384bf4b1d0a33479d1fac0"
model_uri = f"runs:/{run_id}/model"

print("Pobranie z Run")

loaded_model = mlflow.sklearn.load_model(model_uri)
print(loaded_model)

prediction = loaded_model.predict([iris_features])
print(prediction)

print("Pobranie z ModelRegistry")
model_name = "IrisClassifier"
model_version = 1

loaded_model = mlflow.sklearn.load_model(f"models:/{model_name}/{model_version}")
print(loaded_model)

prediction = loaded_model.predict([iris_features])
print(prediction)

print("Pobranie z ModelRegistry - alias")
model_name = "IrisClassifier"
model_alias = "production"

loaded_model = mlflow.sklearn.load_model(f"models:/{model_name}@{model_alias}")
print(loaded_model)

prediction = loaded_model.predict([iris_features])
print(prediction)
