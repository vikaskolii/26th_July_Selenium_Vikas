import time

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(3)
driver.get("https://meet.google.com/landing")
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.close()