import bentoml
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Wczytanie zbioru danych Iris
iris = load_iris()
X, y = iris.data, iris.target

# Podział na zbiór treningowy i testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Trenowanie modelu
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Zapisanie modelu w BentoML
model_tag = bentoml.sklearn.save_model(
    "iris_classifier",
    model,
    signatures={
        "predict": {"batchable": True, "batch_dim": 0},
        "predict_proba": {"batchable": True, "batch_dim": 0}
    },
    metadata={"accuracy": model.score(X_test, y_test)}
)

print(f"Model zapisany: {model_tag}")