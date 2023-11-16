from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

USER = "ElliotGalibert"
PASS = "floora123"
X_URL = "https://twitter.com/login"
SPEEDTEST_URL = "https://www.speedtest.net/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

class InternetSpeedTwitterBot:
	def __init__(self):
		self.driver = webdriver.Chrome(options=chrome_options)
		self.down = 0
		self.up = 0
		
	def get_internet_speed(self):
		self.driver.get(SPEEDTEST_URL)
		sleep(5)
		go = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
		go.click()
		sleep(60)
		downlaod = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
		upload = self.driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
		print(downlaod, upload)

	def tweet_at_provider(self):
		# Log in to Twitter aka X
		username = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
		username.send_keys(USER)

		next = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[6]')
		next.click()
		sleep(3)

		password =self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
		# password.click()
		password.send_keys(PASS)
		password.send_keys(Keys.ENTER)
		sleep(3)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
# bot.tweet_at_provider()

