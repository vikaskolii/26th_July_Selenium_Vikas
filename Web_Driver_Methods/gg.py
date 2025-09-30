from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("file:///F:/Automation%20Testing/HTML%20CODE/TAGNAME.html")
time.sleep(2)
driver.find_element(By.TAG_NAME,"input").send_keys("Vikas")
time.sleep(2)
driver.find_element(By.TAG_NAME,"input").send_keys("Koli")
time.sleep(5)

driver.refresh()
time.sleep(5)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.quit()


"""""""""
When we can’t use tagname as a locator type?
When Tagname is duplicate

"""""""""