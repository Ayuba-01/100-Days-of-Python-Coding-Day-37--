import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
NUTRITIONIX_END_POINT = os.environ.get("NUTRITIONIX_END_POINT")
SHEETY_END_POINT = os.environ.get("SHEETY_END_POINT")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "14.5"
AGE = "27"
headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

query = input("Which exercise did you do today ? ")
parameters = {
    'query': query,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

nutritionix_response = requests.post(url=NUTRITIONIX_END_POINT, json=parameters, headers=headers)
exersice_list = nutritionix_response.json()["exercises"]

today = datetime.now()
for i in range(len(exersice_list)):
    parameters = {
        "workout": {
            "date": today.strftime("%Y/%m/%d"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exersice_list[i]["name"].title(),
            "duration": exersice_list[i]["duration_min"],
            "calories": exersice_list[i]["nf_calories"],

        }
    }
    header = {
        "Authorization": f"Bearer {SHEETY_TOKEN}",
    }
    sheety_response = requests.post(url=SHEETY_END_POINT, json=parameters, headers=header)
    print(sheety_response.text)

