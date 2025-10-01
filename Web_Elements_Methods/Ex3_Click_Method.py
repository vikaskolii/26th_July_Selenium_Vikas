from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.find_element(By.XPATH ,"//input[@type='text']").send_keys("kartik")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@value='1']").click()
time.sleep(5)

driver.quit()