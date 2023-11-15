from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# price = driver.find_element(By.CLASS_NAME, value= "a-offscreen")
price = driver.find_element(By.XPATH, value="//*[@id='corePrice_desktop']/div/table/tbody/tr/td[2]/span[1]/span[2]")
print(price.text)
# By ID, By CSS SELECTOR, By.NAME
# Xpath //*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[2]

driver.quit()