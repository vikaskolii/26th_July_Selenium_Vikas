from selenium import webdriver
import time

# Example 1
# Initialize the Chrome browser
driver = webdriver.Chrome()
# Open Facebook
driver.get("https://www.facebook.com")
# Wait for 5 seconds
time.sleep(5)
# Close the browser window
driver.close()
# Quit the driver completely
driver.quit()

