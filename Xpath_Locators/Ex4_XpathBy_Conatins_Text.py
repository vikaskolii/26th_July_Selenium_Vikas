from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Forgotte')]").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Create')]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Nikhil")
time.sleep(1)
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("Yadav")
time.sleep(2)
driver.refresh()
time.sleep(3)
driver.quit()
