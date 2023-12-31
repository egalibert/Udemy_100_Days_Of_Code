from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
# from notification_manager import NotificationManager
from datetime import datetime, timedelta

ORIGIN_CITY_IATA = "HEL"


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":
	for row in sheet_data:
		row["iataCode"] = flight_search.get_destination_code(row["city"])
	print(f"sheet_data:\n {sheet_data}")

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