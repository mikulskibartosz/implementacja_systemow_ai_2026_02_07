from pydantic import BaseModel
import yaml


class DataConfig(BaseModel):
    path: str
    format: str
    validation_split: float

class ModelConfig(BaseModel):
    type: str
    n_estimators: int
    max_depth: int
    random_state: int

class TrainingConfig(BaseModel):
    batch_size: int
    epochs: int
    learning_rate: float
    early_stopping: bool

class Config(BaseModel):
    data: DataConfig
    model: ModelConfig
    training: TrainingConfig

with open("config.yaml", "r") as f:
    config_dict = yaml.safe_load(f)
    config = Config(**config_dict)

print(config_dict)
print(config)
print(config.model.n_estimators)