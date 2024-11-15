import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEET_END_POINT = os.environ["SHEET_END_POINT"]
SHEET_TOKEN = os.environ["SHEET_TOKEN"]
header = {
    "Authorization": f"Basic {SHEET_TOKEN}",
}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_END_POINT, headers=header)
        response_data = response.json()["prices"]
        self.destination_data = response_data
        return self.destination_data

    def update_sheet(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEET_END_POINT}/{city['id']}", json=new_data, headers=header)
            print(response.text)
