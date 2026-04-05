# TimeOutException

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

def test_TimeoutException():
    driver = webdriver.Chrome()
    driver.get("https://google.com/")

    try:
        WebDriverWait(driver=driver, timeout=10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        print("End of the Program")
    except TimeoutException as te:
        print(te)
        print("TimeoutException occurred!! , 10 Seconds Passed")

    finally:
        driver.quit()