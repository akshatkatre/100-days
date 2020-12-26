import requests

response = requests.get(url="https://api.kanye.rest")
data = response.json()
print(f"Kanye says: {data['quote']}")