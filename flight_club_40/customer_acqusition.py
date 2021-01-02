import requests
import json
from pprint import pprint
from common import resource


class CustomerModel:
    def __init__(self, f_name: str, l_name: str, em: str):
        self.first_name: str = f_name
        self.last_name: str = l_name
        self.email: str = em
        self.endpoint_users = resource.get_resource_key("sheety")['endpoint_users']
        self.bearer_token = resource.get_resource_key("sheety")['bearer_token']

    def get_user_data(self):
        print("Welcome to the Flight club.\nWe find the best flight deals and email you")
        self.first_name = input("what is your first name\n").title().strip()
        self.last_name = input("what is your first name\n").title().strip()
        email_1 = input("what is your Email\n").title().strip()
        email_2 = input("type your Email\n").title().strip()
        if email_1 == email_2:
            self.email = email_1
            print("You are in the flight club.")
            self.insert_data_into_google_sheet()

    def insert_data_into_google_sheet(self):
        headers = {"Authorization": f"Bearer {self.bearer_token}",
                   "Content-Type": "application/json"}
        payload = {
            "user" : {
                "firstname" : self.first_name,
                "lastname" : self.last_name,
                "email" : self.email,

            }
        }
        pprint(payload)
        response = requests.post(url=f"{self.endpoint_users}", headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        pprint(response.text)





