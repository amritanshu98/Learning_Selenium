# StaleElementReferenceException

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import *

def test_StaleElementReferenceException():
    driver = webdriver.Chrome()
    driver.get("https://google.com/")

    try:
        textarea = driver.find_element(By.NAME, "q")
        driver.refresh()

        # Document HTML might change  - refresh
        # element - textarea -> might be case that it is not available now.
        # // Refresh, Navigate other Page, change in DOM elements (Ajax Calls) - VueJS, AngularJS

        textarea.send_keys("Selenium Learning")
        print("End of the Program")
    except StaleElementReferenceException as see:
        print(see)
        print("Stale element reference")

        # After Adding these lines of code, our task will get completed. Ideally we are not using this.
        # textarea = driver.find_element(By.NAME, "q")
        # textarea.send_keys("Selenium Learning")

    time.sleep(5)