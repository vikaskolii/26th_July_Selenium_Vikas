from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///F:/Automation%20Testing/HTML%20CODE/NAME.html")
time.sleep(3)

driver.find_element(By.NAME,"abc123").send_keys("Email")
time.sleep(2)
driver.find_element(By.NAME,"mit").send_keys("xya")
time.sleep(6)
driver.refresh()
time.sleep(2)
driver.quit()


'''''''''
When we can’t use Name as a locator type?
When Name attribute value is duplicate
When Name attribute is not present for that element

'''''''''''