from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"(//a[@role='button'])[2]").click()
time.sleep(2)

driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("Vikas")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("Koli")
time.sleep(2)
driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys("8070909093")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Koli@125864")
time.sleep(2)

#is_selected Method
a1=driver.find_element(By.XPATH,"(//input[@class='_8esa'])[1]").is_selected()
print(a1)

if(a1):
    print("Button Selected")
else:
    print("Button De-selected")


