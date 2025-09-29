#Example 1
import time

from selenium import webdriver
print("______________________________")

# Initialize the Chrome browser
driver = webdriver.Chrome()
# Open Facebook
driver.get("https://www.facebook.com")
time.sleep(3)                           #Time 3 second for next page reload
driver.maximize_window()                # maximize the current window
time.sleep(5)                           #Time 5 second for next page reload
driver.minimize_window()                # minimize the current window
time.sleep(2)                           #Time 2 second for next page reload
driver.fullscreen_window()              # FullScreen the current window
# time.sleep(5)
s1=driver.title                         # This way also use for getting title/Current URL
print(s1)
print("_______________________")
print(driver.title)                     #used for Getting the title of web page
print(driver.current_url)               #Used for the Getting the URL of The website

driver.close()                          #Close the Current window/web page
