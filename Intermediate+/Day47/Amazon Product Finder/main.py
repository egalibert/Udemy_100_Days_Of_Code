import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
import lxml

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "fi-FI,fi;q=0.9,en-US;q=0.8,en;q=0.7"

header = {
	"User-Agent": USER_AGENT,
	"Accept-Language": ACCEPT_LANGUAGE
}

response = requests.get(url=URL, headers=header)

soup = BeautifulSoup(response.text, "lxml")
price = soup.find(class_ = "a-offscreen").text
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

print (price_as_float)

if (price_as_float < 100):
	pass
	# with smtplib.SMTP( port=587) as connection:
	# 	connection.starttls()
	# 	result = connection.login(MAIL, PASSWORD)
	# 	connection.sendmail(
	# 		from_addr=YOUR_EMAIL,
	# 		to_addrs=YOUR_EMAIL,
	# 		msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
	# 	)