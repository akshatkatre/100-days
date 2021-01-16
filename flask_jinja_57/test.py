import requests

blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
response = requests.get(url=blog_url)
response.raise_for_status()
data: list = response.json()
print(data[0])