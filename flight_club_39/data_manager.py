import requests
import json
from pprint import pprint
from common import resource


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = resource.get_resource_key("sheety")['endpoint']
        self.bearer_token = resource.get_resource_key("sheety")['bearer_token']

    def get_flight_data(self):
        headers = {"Authorization": f"Bearer {self.bearer_token}",
                   "Content-Type": "application/json"}
        response = requests.get(url=self.endpoint, headers=headers)
        response.raise_for_status()
        return response.text

    def update_iata_code(self, record_id: str, record: dict):
        headers = {"Authorization": f"Bearer {self.bearer_token}",
                   "Content-Type": "application/json"}
        response = requests.put(url=f"{self.endpoint}/{record_id}", headers=headers, data=json.dumps(record))
        response.raise_for_status()
        print(response.text)