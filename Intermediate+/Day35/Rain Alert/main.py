import requests

API_KEY = "926c4f3ae959afb89faeadd77980815b"
MY_LAT = 60.173920
MY_LONG = 24.803804
# OMW_Endpoint1 = "https://api.openweathermap.org/data/2.5/onecall"
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
	"lat": MY_LAT,
	"lon": MY_LONG,
	"appid": API_KEY
	# "exclude": "current,minutely,hourly"
}

response = requests.get(OMW_Endpoint, weather_params)
response.raise_for_status()
weather_data = response.json()
current_weather = dict.get(weather_data, "weather")

print(current_weather[0]["id"])

if current_weather[0]["id"] < 700:
	print("Bring an umbrella!")