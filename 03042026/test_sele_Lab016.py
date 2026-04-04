# NoSuchElementException

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_NoSuchElementException():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")
    element = driver.find_element(By.ID, "this_id_doesnot_exist")

    # 'status': 404
    # no such element , Unable to locate element
    # NoSuchElementException

    print("End of Program")
    time.sleep(5)