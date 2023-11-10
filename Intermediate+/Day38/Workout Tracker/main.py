import requests
import os
from datetime import datetime
from requests.auth import HTTPBasicAuth

AUTHENTICATION = HTTPBasicAuth('koira', 'kissa123')
APP_ID = "c5180bb6"
APP_KEY = "9c76fcf1aa976e515bd8cb2ed2864ec9"

os.environ["APP_ID"] = APP_ID

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/4fe89e975a42104dd0a07e717612f79f/treenipäiväkirja/workouts"

# exercise_text = input("Tell me what exercises you did")

headers = {
	"x-app-id": APP_ID,
	"x-app-key": APP_KEY,
	"x-remote-user-id": "0"
}

info = {
	"query": "running for 30 min",
	"gender": "male",
	"weight_kg": "83.5",
	"height_cm": "183.37",
	"age": "27"
}

response = requests.post(ENDPOINT, json=info, headers=headers)
data = response.json()
# print(data)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
	sheet_inputs = {
		"workout": {
			"date": today_date,
			"time": now_time,
			"exercise": exercise["name"].title(),
			"duration": exercise["duration_min"],
			"calories": exercise["nf_calories"]
		}
	}

response1 = requests.post(SHEET_ENDPOINT, json=sheet_inputs, auth=AUTHENTICATION)

