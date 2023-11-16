from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

FB_EMAIL = "extream-man@hotmail.com"
FB_PASS = "SoGiVMA5"

phone_xpath = '//*[@id="s2018968691"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button'
FB_XPATH = '//*[@id="s2018968691"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'

URL = "https://tinder.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Opening tinder page and pressing log in
time.sleep(3)
first_login = driver.find_elements(By.TAG_NAME, value="button")
first_login[1].click()

# Choosing Facebook login
time.sleep(3)
fb_login = driver.find_element(By.XPATH, value=FB_XPATH)
fb_login.click()

# Switching and saving different windows
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]

driver.switch_to.window(fb_login_window)
print(driver.title)

time.sleep(3)

# After switch login using Facebook

mail_tab = driver.find_element(By.ID, value="email")
mail_tab.send_keys(FB_EMAIL)

password_tab = driver.find_element(By.ID, value="pass")
password_tab.send_keys(FB_PASS)
password_tab.send_keys(Keys.ENTER)

# Switch back to Tinder Window

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(10)

# Click to allow locations, and no notifications and cookies 
salli_xpath = '//*[@id="s2018968691"]/main/div/div/div/div[3]/button[1]'
ei_kiinnosta_xpath = '//*[@id="s2018968691"]/main/div/div/div/div[3]/button[2]'
cookies_xpath = '//*[@id="s-547617529"]/div/div[2]/div/div/div[1]/div[1]/button'

allow = driver.find_element(By.XPATH, value=salli_xpath)
allow.click()
time.sleep(3)
not_interested = driver.find_element(By.XPATH, value=ei_kiinnosta_xpath)
not_interested.click()
time.sleep(3)
cookies = driver.find_element(By.XPATH, value=cookies_xpath)
cookies.click()

# Start liking or disliking

like_xpath = '//*[@id="s-547617529"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button'
dislike_xpath = '//*[@id="s-547617529"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[2]/button'
age_xpath = '//*[@id="s-547617529"]/div/div[1]/div/div/main/div/div/div[1]/div/div[2]/div[3]/div/div/div/div/div[1]/div/span[2]'
tinder = driver.find_element(By.ID, value="Tinder")

for n in range(10):
	time.sleep(2)
	try:
		tinder.send_keys(Keys.ARROW_RIGHT)
	#Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
	except ElementClickInterceptedException:
		time.sleep(4)
		try:
			match_popup = driver.find_element_by_css_selector(".itsAMatch a")
			match_popup.click()
		#Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
		except NoSuchElementException:
			time.sleep(2)
driver.quit()