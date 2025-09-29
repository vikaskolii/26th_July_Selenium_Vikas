from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("file:///F:/Automation%20Testing/HTML%20CODE/ID.html")
time.sleep(2)
driver.find_element(By.ID,"1234").send_keys("RAM123")
time.sleep(2)
driver.find_element(By.ID,"4567").send_keys("Nikhil")
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.quit()







'''''''''
When we can’t use ID as a locator type?
When ID is attribute value is duplicate.
When ID attribute is not present for that element.
'''''''''