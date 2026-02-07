import tomllib
from datetime import datetime
from pydantic import BaseModel
from typing import Union

class ServerConfig(BaseModel):
    ip: str
    role: str

class OwnerConfig(BaseModel):
    name: str
    dob: datetime

class DatabaseConfig(BaseModel):
    enabled: bool
    ports: list[int]
    data: list[list[Union[str, float]]]
    temp_targets: dict[str, float]

class Config(BaseModel):
    title: str
    owner: OwnerConfig
    database: DatabaseConfig
    servers: dict[str, ServerConfig]

with open("config.toml", "rb") as f:
    config_toml = tomllib.load(f)

    config = Config(**config_toml)

print(config_toml)
print(config)
print(config.owner.name)