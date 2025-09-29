from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///F:/Automation%20Testing/HTML%20CODE/CLASS.html")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"xyz123").send_keys("Vikas")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"xyz123").send_keys("Koli")
time.sleep(5)

d

"""""""""
When we can’t use CLASS_Name as a locator type?
When ClassName attribute value is duplicate
When ClassName attribute is not present for that element


"""""""""