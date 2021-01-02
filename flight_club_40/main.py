from datetime import datetime, timedelta
from flight_club_40.data_manager import DataManager
from flight_club_40.flight_search import FlightSearch
from flight_club_40.notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue
        # flight = flight_search.check_flights(
        #     ORIGIN_CITY_IATA,
        #     destination["iataCode"],
        #     from_time=tomorrow,
        #     to_time=six_month_from_today, stopovers=2)
        # if flight is None:
        #     continue

    if flight.price < destination["lowestPrice"]:
        # notification_manager.send_sms(
        #     message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
        #             f"{flight.destination_city}-{flight.destination_airport}, "
        #             f"from {flight.out_date} to {flight.return_date}.",
        #     live=False
        # )
        users_list = notification_manager.get_email_ids()
        for user in users_list:
            notification_manager.send_email(
                message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.out_date} to {flight.return_date}.\n"
                        f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}",
                live=False,
            to_email = user['email']
            )
