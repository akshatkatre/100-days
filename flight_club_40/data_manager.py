from pprint import pprint
import requests
from common import resource

SHEETY_PRICES_ENDPOINT = resource.get_resource_key("sheety")['endpoint_prices']
BEARER_TOKEN = resource.get_resource_key("sheety")['bearer_token']

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}",
                   "Content-Type": "application/json"}
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}",
                   "Content-Type": "application/json"}
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)
