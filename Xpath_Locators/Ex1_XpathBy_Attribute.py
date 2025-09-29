import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("abc@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Vikas123")
time.sleep(5)
driver.find_element(By.XPATH, "//a[text()='Log in']").click()
time.sleep(5)
driver.close()