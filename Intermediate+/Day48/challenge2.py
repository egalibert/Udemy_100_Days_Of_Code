URL = "http://secure-retreat-92358.herokuapp.com/"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

f_name = driver.find_element(By.NAME, value= "fName")
f_name.send_keys("Elliot")

l_name = driver.find_element(By.NAME, value= "lName")
l_name.send_keys("Galibert")

email = driver.find_element(By.NAME, value= "email")
email.send_keys("elliotgalibert@gmail.com")

button = driver.find_element(By.XPATH, value= "/html/body/form/button")
button.click()