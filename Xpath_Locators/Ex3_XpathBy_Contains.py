from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[contains(@placeholder,'Email add')]").send_keys("nikhil121@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,"//input[contains(@name,'pass')]").send_keys("nikhil@456")
time.sleep(3)
driver.find_element(By.XPATH,"//button[contains(@name,'login')]").click()
driver.refresh()
time.sleep(3)
driver.quit()