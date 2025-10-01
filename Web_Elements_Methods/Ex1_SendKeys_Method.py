from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Vikas")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Ram@123")
time.sleep(2)

driver.quit()