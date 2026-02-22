dvc stage add -n download_data -d download_data.py -d params.yaml -o data/iris.csv python download_data.py

dvc exp run

dvc stage add -n train_model -d train_model.py -d data/iris.csv -d params.yaml -o models/model.pkl -M metrics.json python train_model.py

dvc exp run

dvc dag

dvc exp show