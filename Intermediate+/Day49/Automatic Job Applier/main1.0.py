from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USER = "elliotgalibert@gmail.com"
PASS = ""
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3764510146&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

#Click Sign in button
sign_in_button = driver.find_element(By.XPATH, value="/html/body/div[3]/header/nav/div/a[2]")
sign_in_button.click()
time.sleep(2)

#Sign in
username = driver.find_element(By.ID, value="username")
username.send_keys(USER)
password = driver.find_element(By.ID, value="password")
password.send_keys(PASS)
sign_in2 = driver.find_element(By.XPATH, value="//*[@id='organic-div']/form/div[3]/button")
sign_in2.click()

time.sleep(5)
#Locate apply button

apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
# time.sleep(5)
# phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
# if phone.text == "":
#     phone.send_keys(PHONE)

#Click Next
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
time.sleep(2)
submit_button.click()

#Filling info
infos = driver.find_elements(By.CLASS_NAME, value="artdeco-text-input--input")
for info in infos:
	info.send_keys("2")

time.sleep(2)

#Click review
buttons = driver.find_elements(By.TAG_NAME, value="button")
print(len(buttons))
buttons[2].click()

time.sleep(2)

#Submit
buttons2 = driver.find_elements(By.TAG_NAME, value="button")
buttons2[6].click()