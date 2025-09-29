from selenium import webdriver
from selenium.webdriver.common.by import By
import time


#Open with LINK_TEXT
driver=webdriver.Chrome()
driver.get("file:///F:/Automation%20Testing/HTML%20CODE/LinkText%20&%20PartialText%20Locator%20Type.html")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"facebook").click()
time.sleep(2)
driver.close()


#Open with Partial_Link_text
driver=webdriver.Chrome()
driver.get("file:///F:/Automation%20Testing/HTML%20CODE/LinkText%20&%20PartialText%20Locator%20Type.html")
time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"fac").click()
time.sleep(2)
driver.quit()

