import requests
from common import resource
from datetime import datetime
import json


def write_data_to_sheety(row: dict):
    """
    The function takes a row as a dictionary and invokes a sheety endpoint
    to create the data.
    The endpoint uses Bearer Token for authentication.
    :param row: Dictionary
    :return: None
    """
    # print(row)
    headers = {"Authorization": f"Bearer {resource.get_resource_key('sheety')['bearer_token']}",
               "Content-Type": "application/json"}
    SHEETY_ENDPOINT = resource.get_resource_key("sheety")["endpoint"]
    response = requests.post(url=SHEETY_ENDPOINT, data=json.dumps(row), headers=headers)
    response.raise_for_status()
    # print(response.text)


raw_input = input("Enter today's exercise description: ")

API_ID = resource.get_resource_key("nutritionix")["application_id"]
API_KEY = resource.get_resource_key("nutritionix")["api_key"]
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
"x-app-id" : API_ID,
"x-app-key" : API_KEY,
    "x-remote-user-id" : "0"
}

input_data = {
"query":raw_input,
 "gender":"male",
 "weight_kg":"Your weight",
 "height_cm": "Your height",
 "age": "Your age"
}

response = requests.post(url=ENDPOINT, headers=headers, json=input_data)
response.raise_for_status()
# print(response.json())
now = datetime.now()
Date = now.strftime("%d/%m/%Y")
Time = now.strftime("%H:%M:%S")
data = [{"workout": {"date": Date, "time": Time,
         "exercise": x['user_input'],
         "duration": x['duration_min'],
        "calories": x['nf_calories']}} for x in response.json()['exercises']]

for item in data:
    write_data_to_sheety(item)


