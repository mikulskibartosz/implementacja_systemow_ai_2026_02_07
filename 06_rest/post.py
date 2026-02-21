import requests


response = requests.post("https://jsonplaceholder.typicode.com/posts", json={"title": "test", "body": "jakiś tekst", "userId": 12345})

if response.status_code == 201:
    data = response.json()
    print(data)
else:
    print(response.status_code)
    print(response.text)

