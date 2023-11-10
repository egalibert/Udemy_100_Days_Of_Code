import requests
import datetime
# import twilio.rest from Client

#   This project wont work because I've removed API:s 

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = ""
NEWS_API = ""

params = {
	"function": "TIME_SERIES_DAILY",
	"interval": "60min",
	"symbol": STOCK_NAME,
	"apikey": STOCK_API
}

# Get Stock change
response = requests.get(STOCK_ENDPOINT, params)
response.raise_for_status()

data = response.json()["Time Series Daily"]
data_list = [value for (key, value) in data.items()]

yesterday_close_price = data_list[0]["4. close"]
two_days_ago_price = data_list[1]["4. close"]

difference = abs(float(yesterday_close_price) - float(two_days_ago_price))
percentage_dif = difference / float(yesterday_close_price) * 100

# print(difference, percentage_dif)

# Get News about company
params2 = {
	"q": COMPANY_NAME,
	"apiKey": NEWS_API
}

response2 = requests.get(NEWS_ENDPOINT, params2)
response2.raise_for_status()
news_data = response2.json()["articles"]
# print(news_list, len(news_list))

# If change is more than 5% send sms

if percentage_dif >= 5.0:
	news_list = news_data[:3]
	formatted_articles = [f"Headline: {news_data["title"]}. \n Brief {news_data['description']}" for news_data in news_list]
    # for article in formatted_articles:
    #     message = client.message.create(
    #                   body=article,
    #                   from="Phone number"
    #                   to="Phone number"
    # )


#TODO 9. - Send each article as a separate message via Twilio. 
# Not spamming messages to myself!


