import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_mini_project_6():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")

    email_input = driver.find_element(By.XPATH, "//input[contains(@id, 'login-username')]")
    password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")

    email_input.send_keys("admin@admin.com")
    password_input.send_keys("admin@123")

    login_btn = driver.find_element(By.XPATH, "//button[contains(@id, 'js-login-btn')]")
    login_btn.click()

    # A condition is needed to check the element
    # Error message comes after 5 seconds
    # I have to wait with some condition -
    # wait with the condition
    # Add a condition so that Webdriver should wait for that condition.
    # element is visible then assertion
    # when  this -> then do this


    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.ID, "js-notification-box-msg"))
    )


    err_msg = driver.find_element(By.ID, "js-notification-box-msg")
    print(err_msg.text)

    # time.sleep(2)
    assert err_msg.text == "Your email, password, IP address or location did not match"


