import bentoml
from sklearn.datasets import fetch_openml
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


df = fetch_openml(data_id=42585)
df = df['frame']
df = df.dropna()

X = df.drop(columns=['species'])
y = df['species']

X_categorical = X[['sex', 'island']].copy()
X_numerical = X.drop(columns=['sex', 'island']).copy()

encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded_features = encoder.fit_transform(X_categorical)
encoded_feature_names = encoder.get_feature_names_out(['sex', 'island'])
encoded_df = pd.DataFrame(encoded_features, columns=encoded_feature_names, index=X.index)

encoded_df = pd.concat([X_numerical, encoded_df], axis=1)

X_train, X_test, y_train, y_test = train_test_split(encoded_df, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)

encoder_tag = bentoml.sklearn.save_model(
    "penguins_encoder",
    encoder,
    signatures={
        "transform": {"batchable": True, "batch_dim": 0},
    },
    metadata={"description": "OneHotEncoder for sex and island features"}
)
print(f"Encoder zapisany w BentoML: {encoder_tag}")

model_tag = bentoml.sklearn.save_model(
    "penguins_classifier",
    model,
    signatures={
        "predict": {"batchable": True, "batch_dim": 0},
    },
    metadata={"accuracy": accuracy}
)

print(f"Model zapisany: {model_tag}")