from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
time.sleep(2)


#1st Apporach
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Vikas")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='text']").clear()
time.sleep(2)



# #2nd Approach
# S1=driver.find_element(By.XPATH,"//input[@type='text']")
# S1.send_keys("Kartik")
# time.sleep(5)
# S1.clear()
# time.sleep(2)
#
# driver.quit()