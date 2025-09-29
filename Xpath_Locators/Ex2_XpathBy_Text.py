import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(5)
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Vikas")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("ram45")
time.sleep(5)
driver.find_element(By.XPATH, "//a[text()='Log in']").click()
time.sleep(5)
driver.quit()
