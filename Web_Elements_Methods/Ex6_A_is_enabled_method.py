from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(2)

a1=driver.find_element(By.XPATH,"//button[@class=' _aswp _aswr _aswu _asw_ _asx2']").is_enabled()
print(a1)
time.sleep(5)

if(a1):
    print("Is Enabled")
else:
    print("Is not enabled")