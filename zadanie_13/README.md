mlflow run . --env-manager local --experiment-name penguins-classification

mlflow run . -P n_estimators=200 -P max_depth=10 --env-manager local --experiment-name penguins-classification

mlflow run . -e evaluate -P run_id=5bf24fb2773044d681cbb4bc7d9fd5f2 --env-manager local