from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

USER = "elliotgalibert@gmail.com"
PASS = ""
SIMILIAR_ACCOUNT = "cristiano"
IG_URL = "https://www.instagram.com/accounts/login/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InstaFollower:
	def __init__(self):
		self.driver = webdriver.Chrome(options=chrome_options)

	# Login into instagram with account
	def login(self):
		self.driver.get(IG_URL)
		sleep(3)
		cookies = self.driver.find_element(By.XPATH, value="/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
		cookies.click()
		sleep(2)

		username = self.driver.find_element(By.NAME, value="username")
		username.send_keys(USER)

		password = self.driver.find_element(By.NAME, value="password")
		password.send_keys(PASS)
		password.send_keys(Keys.ENTER)
		sleep(5)

	# Choose account, and click on people he's following
	def find_followers(self):
		self.driver.get(f"https://www.instagram.com/{SIMILIAR_ACCOUNT}")
		sleep(7)
		followers = self.driver.find_elements(By.CSS_SELECTOR, value='ul li a')[1]
		followers.click()
		sleep(4)

	# Scroll followers popup and follow everyone
	def follow(self):
		follows = self.driver.find_elements(By.CSS_SELECTOR, value="._aano ._acan")
		i = 0
		for count in range(100):
			sleep(1)
			count += 1
			# Need to scroll down to find more people to followe
			if i == 12:
				follows = self.driver.find_elements(By.CSS_SELECTOR, value="._aano ._acan")
			follows[i].location_once_scrolled_into_view
			try:
				follows[i].click()
			except ElementClickInterceptedException:
				self.driver.find_elements(By.CLASS_NAME, '_a9--')[1].click()
				sleep(2)
			i += 1

instagram = InstaFollower()
instagram.login()
instagram.find_followers()
instagram.follow()