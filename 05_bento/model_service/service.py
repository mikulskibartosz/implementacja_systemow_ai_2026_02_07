import bentoml
from bentoml.models import BentoModel
from pydantic import BaseModel
import numpy as np
import pandas as pd

# format danych wejściowych
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


SPECIES = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

@bentoml.service(name="iris_classifier_service")
class IrisClassifierService():
    iris_model = BentoModel("iris_classifier:latest")

    def __init__(self):
        self.model = bentoml.sklearn.load_model(self.iris_model)

    @bentoml.api()
    def predict(self, iris_features: IrisFeatures) -> str:
        feature_array = np.array([
            [
                iris_features.sepal_length,
                iris_features.sepal_width,
                iris_features.petal_length,
                iris_features.petal_width
            ]
        ])

        pred_class = self.model.predict(feature_array)[0]
        return SPECIES[pred_class]

    @bentoml.api()
    def predict_batch(self, features_batch: pd.DataFrame):
        pred_classes = self.model.predict(features_batch)

        results = []
        for i, pred_class in enumerate(pred_classes):
            results.append(SPECIES[pred_class])

        return {"predictions": results}