from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.instagram.com/")
time.sleep(2)

a1=driver.find_element(By.XPATH,"//i[@aria-label='Instagram']").is_displayed()
time.sleep(1)
print(a1)

if(a1):
    print("The element/logo is displayed")
else:
    print("The Element/Logo is not Displayed")