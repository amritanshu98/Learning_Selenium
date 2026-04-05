import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_action_chain():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.XPATH, "//input[@name = 'firstname']")
    time.sleep(2)
    first_name.send_keys("selenium")

    time.sleep(5)
    first_name.clear()

    actions = ActionChains(driver)
    # Below code will add selenium automation in Capital Letters -> SELENIUM AUTOMATION
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "selenium automation").key_up(Keys.SHIFT).perform()

    time.sleep(10)
    driver.quit()

