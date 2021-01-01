#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import json
from flight_club_39.data_manager import DataManager
from flight_club_39.flight_search import FlightSearch
from flight_club_39.flight_data import FlightData

# Get Flight Data from sheety
data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_flight_data()
data = json.loads(sheet_data)
pprint(data)
print("*****\n")


def update_iata_codes(data: dict):
    for row in data['prices']:
        print(row['city'])
        if row['iataCode'] is None:
            flight_search = FlightSearch()
            code = flight_search.get_iata_code(row['city'])
            row['iataCode'] = code

    print(data)

    for row in data['prices']:
        put_data = {'price': {'iataCode': row['iataCode']}}
        print(put_data)
        # Invoke PUT request in sheety to update the iataCode
        if row['iataCode'] is None:
            data_manager.update_iata_code(row['id'], put_data)


# Flight Search
for row in data['prices']:
    print(row['city'])
    flight = FlightData(row['lowestPrice'])
    search_results: dict = flight_search.search(flight, row['iataCode'])
    # print(search_results)
    if search_results is not None:
        for search_result in search_results['data']:
            price = int(search_result['price'])
            if price < int(row['lowestPrice']):
                print("*** Lower Price Record Found ***")
                print(search_result)

