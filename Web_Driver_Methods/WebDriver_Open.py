# Web Driver Intiallisation
#Note ::: Only Machine Installed browser will be open when we-trying to open browser

import time

from selenium import webdriver

driver=webdriver.Chrome()
time.sleep(10)   # It will be open for only 10 second.

driver=webdriver.Firefox()
time.sleep(10)

driver=webdriver.Edge()
time.sleep(10)

driver=webdriver.Safari()
time.sleep(10)

# selenium -> package
# webdriver -> module
# Chrome()  -> constructor of Chrome class


