import requests
import datetime
from common import resource
from flight_club_39.flight_data import FlightData
import html
import urllib.parse


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.search_endpoint = "https://tequila-api.kiwi.com/search"
        self.api_key = resource.get_resource_key("tequila")['api_key']

    def get_iata_code(self, city_name: str):
        ""
        parameters = {
            "term" : city_name,
            "locale" : "en - US",
            "location_types" : "airport",
            "limit" : 1,
            "active_only" : "true"
        }
        headers = {
            "apikey": self.api_key
        }
        response = requests.get(url=self.endpoint, params=parameters, headers=headers)
        response.raise_for_status()
        print(response.text)
        flight_search_data = response.json()
        iata_code = flight_search_data['locations'][0]['code']
        print(f"code: {iata_code}")
        return iata_code

    def search(self, data: FlightData, city: str):
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        end_date = datetime.datetime.now() + datetime.timedelta(days=180)

        payload = html.unescape({
            "fly_from" : data.departure_airport_code,
            "fly_to" : city,
            "date_from" : html.unescape(tomorrow.strftime("%d/%m/%Y")),
            "date_to" : html.unescape(end_date.strftime("%d/%m/%Y")),
            "max_stopovers": 0,
            "nights_in_dst_from" : 7,
            "nights_in_dst_to" : 28,
            "flight_type" : "round",
            "adults" : 1,
            "curr" : "GBP",
            "locale" : "en"
        })
        payload_str = urllib.parse.urlencode(payload, safe='/')
        headers = {
            "apikey": self.api_key
        }
        print(payload_str)
        response = requests.get(url=self.search_endpoint, params=payload_str, headers=headers)
        response.raise_for_status()
        # print("****Response****")
        return response.json()