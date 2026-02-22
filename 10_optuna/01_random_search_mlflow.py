import mlflow
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, RandomizedSearchCV

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

param_distributions = {
    'n_estimators': np.arange(50, 300, 50),
    'max_depth': [None, 5, 10, 15, 20],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(random_state=42),
    param_distributions=param_distributions,
    n_iter=100,
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=-1
)

with mlflow.start_run(run_name="RandomSearch-RF"):
    mlflow.log_param("search_method", "RandomizedSearchCV")
    mlflow.log_param("n_iterations", 100)

    random_search.fit(X_train, y_train)

    best_params = random_search.best_params_
    for param, value in best_params.items():
        mlflow.log_param(f"best_{param}", value)

    mlflow.log_metric("best_score", random_search.best_score_)
    mlflow.log_metric("test_score", random_search.score(X_test, y_test))

    mlflow.sklearn.log_model(random_search.best_estimator_,
                            "best_model")