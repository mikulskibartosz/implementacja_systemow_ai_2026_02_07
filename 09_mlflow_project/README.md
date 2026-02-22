mlflow run . --env-manager local --experiment-name iris-classification

mlflow run . -P n_estimators=200 -P max_depth=10 --env-manager local --experiment-name iris-classification

mlflow run . -e evaluate -P run_id=33850de06841469786c82d9915063cb6 --env-manager local

mlflow models serve -m runs:/33850de06841469786c82d9915063cb6/model --port 1234
