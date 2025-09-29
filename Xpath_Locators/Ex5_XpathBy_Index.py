from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH,"//a[@class='_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy']").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("Vaibhavi")
time.sleep(1)
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("Koli")
time.sleep(1)

driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys("8070909093")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Vaibhu@123")
time.sleep(3)

driver.refresh()
time.sleep(3)

driver.quit()