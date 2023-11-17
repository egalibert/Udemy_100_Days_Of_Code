from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import bs4

URL = "https://appbrewery.github.io/Zillow-Clone"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdvG9ttnse5r2toYPTza1z6Yuw9_LJOX5FxemeyDZIjKyJA_A/viewform?usp=sf_link"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Get Zillow page and use Beautiful Soup to make readable html
response = requests.get(url=URL)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")

#Finding prices and making a list
prices = soup.find_all(class_ = "PropertyCardWrapper__StyledPriceLine")
prices_list = []

for price in prices:
		text = price.text
		slice_object = slice(6)
		final_text = text[slice_object]
		final_text.replace("+", "")
		prices_list.append(final_text)

# Finding hyperlinks and making a list
links_list = []
links = soup.find_all("a", class_ = "StyledPropertyCardDataArea-anchor")

for link in links:
	links_list.append(link.get("href"))

# Finding addresses and making a list
address_list = []
addresses = soup.find_all("address")

for address in addresses:
	text = address.text
	text = " ".join(text.split())
	address_list.append(text)

# Using selenium to fill form with list info
index = 0
for _ in range(len(address_list)):
	driver.get(FORM)
	sleep(3)

	q1_text = address_list[index]
	q2_text = prices_list[index]
	q3_text = links_list[index]

	q1 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
	q1.send_keys(q1_text)

	q2 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
	q2.send_keys(q2_text)

	q3 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
	q3.send_keys(q3_text)
	index += 1

	submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
	submit.click()

