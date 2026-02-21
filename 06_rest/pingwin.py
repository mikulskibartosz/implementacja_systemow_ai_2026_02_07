import requests


data = {
  "penguin_features": {
    "culmen_length_mm": 80,
    "culmen_depth_mm": 50,
    "flipper_length_mm": 158,
    "body_mass_g": 4000,
    "sex": "male",
    "island": "Dream"
  }
}

response = requests.post("http://localhost:3000/predict", json=data)

if response.status_code == 200:
    data = response.json()
    print(data)