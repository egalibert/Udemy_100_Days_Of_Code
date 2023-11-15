from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
URL = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# number = driver.find_element(By.XPATH, value="//*[@id='articlecount']/a[1]")
# number.click()

# all_portals = driver.find_element(By.LINK_TEXT, value= "Jessie Murray")
# all_portals.click()

search_bar = driver.find_element(By.NAME, value= "search")
search_bar.send_keys("Python")
# search_bar.send_keys(Keys.RETURN)

button = driver.find_element(By.XPATH, value= "//*[@id='searchform']/div/button")
button.click()

# print(number.text)

# driver.quit()