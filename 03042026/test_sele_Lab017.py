# NoSuchElementException Handling

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import *

def test_NoSuchElementException():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    try:
        element = driver.find_element(By.ID, "this_id_doesnot_exist")

    except NoSuchElementException:
        print("No Such Element Found")

    print("End of Program")
    time.sleep(3)