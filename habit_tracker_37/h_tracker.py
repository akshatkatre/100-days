import requests
from common import resource
from datetime import datetime

url_user_endpoint = "https://pixe.la/v1/users"

# get token & username
TOKEN = resource.get_resource_key("pixela")["token"]
USERNAME = resource.get_resource_key("pixela")["username"]

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=url_user_endpoint, json=user_parameters)
# print(response.json())

graph_endpoint = f"{url_user_endpoint}/{USERNAME}/graphs"
print(f"Endpoint : {graph_endpoint}")

graph_id = "graph1"
graph_parameters = {
    "id": graph_id,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
"X-USER-TOKEN" : TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.json())


now = datetime.now()
# current_date = f"{now.year}{now.month}{now.day}"
current_date = now.strftime("%Y%m%d")
print(current_date)
# Posting a pixel
pixel_data = {
    "date" : str(current_date),
    "quantity" : "0.5"
}

pixel_endpoint = f"{url_user_endpoint}/{USERNAME}/graphs/{graph_id}"
print(pixel_endpoint)
# response = requests.post(url=pixel_endpoint, headers=headers, json=pixel_data)
# print(response.text)

# Update a pixel
print('Updating pixel')

pixel_data = {
    "quantity" : "2.1"
}

pixel_endpoint = f"{url_user_endpoint}/{USERNAME}/graphs/{graph_id}/{current_date}"
# response = requests.put(url=pixel_endpoint, headers=headers, json=pixel_data)
# print(response.text)

# Delete a pixel
print('Deleting pixel')

pixel_endpoint = f"{url_user_endpoint}/{USERNAME}/graphs/{graph_id}/{current_date}"
response = requests.delete(url=pixel_endpoint, headers=headers)
print(response.text)