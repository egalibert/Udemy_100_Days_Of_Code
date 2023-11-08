import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 60.173920
MY_LONG = 24.803804

MY_EMAIL = "elliotgalibert@gmail.com"
MY_PASSWORD = 12345

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def position_check():
	if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
			return True
	else:
		return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now <= sunrise:
        return True

while(True):
    time.sleep(60)
    if position_check() and is_night():
        connection = smtplib.SMTP("gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.send_message(from_addr=MY_EMAIL,
                                    to_addrs=MY_EMAIL,
                        msg= "Subject: Look up!")
