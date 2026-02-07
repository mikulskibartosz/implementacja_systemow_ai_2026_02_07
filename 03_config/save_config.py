import yaml
from dataclasses import dataclass


@dataclass
class ServerConfig:
    ip: str
    role: str

config = ServerConfig(ip="127.0.0.1", role="frontend")

with open("config_dataclass.yaml", "w") as f:
    yaml.dump(config.__dict__, f)


with open("config_dataclass.toml", "w") as f:
    f.write(f"server_ip = \"{config.ip}\"\n")
    f.write(f"server_role = \"{config.role}\"\n")