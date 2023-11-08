import requests
from datetime import datetime

MY_LAT = 60.173920
MY_LONG = 24.803804
formatted = 0

parameters = {
	"lat": MY_LAT,
	"lng": MY_LONG,
	"formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()

data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise.split("T")[1].split(":"))