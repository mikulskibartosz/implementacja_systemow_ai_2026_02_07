import bentoml
from pydantic import BaseModel
import pandas as pd

class PenguinFeatures(BaseModel):
    culmen_length_mm: float
    culmen_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float
    sex: str
    island: str


@bentoml.service(
    name="penguins_classifier_service"
)
class PenguinsClassifierService:

    def __init__(self):
        self.model = bentoml.models.get("penguins_classifier:latest").load_model()
        self.encoder = bentoml.models.get("penguins_encoder:latest").load_model()


    def _preprocess_features(self, features):
        numerical_features = pd.DataFrame({
            'culmen_length_mm': [features.culmen_length_mm],
            'culmen_depth_mm': [features.culmen_depth_mm],
            'flipper_length_mm': [features.flipper_length_mm],
            'body_mass_g': [features.body_mass_g]
        })

        categorical_features = pd.DataFrame({
            'sex': [features.sex],
            'island': [features.island]
        })

        encoded_categorical = self.encoder.transform(categorical_features)
        encoded_df = pd.DataFrame(
            encoded_categorical,
            columns=self.encoder.get_feature_names_out(['sex', 'island'])
        )

        return pd.concat([numerical_features, encoded_df], axis=1)

    @bentoml.api()
    def predict(self, penguin_features: PenguinFeatures):
        """
        Przewiduje gatunek pingwina na podstawie podanych cech.
        """
        processed_features = self._preprocess_features(penguin_features)

        pred_class = self.model.predict(processed_features)

        species = pred_class[0]
        return {"species": species}