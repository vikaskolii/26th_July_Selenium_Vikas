import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@name='email']").send_keys("abc")

value1=driver.find_element(By.XPATH,"//input[@name='email']").get_attribute("value")
print(value1)

value2=driver.find_element(By.XPATH,"//input[@name='email']").get_attribute("placeholder")
print(value2)