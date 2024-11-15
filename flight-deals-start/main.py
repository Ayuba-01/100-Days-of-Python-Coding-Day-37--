from data_manager import DataManager
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        flight_search = FlightSearch()
        row["iataCode"] = flight_search.get_destination_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_sheet()

