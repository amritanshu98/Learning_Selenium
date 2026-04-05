import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

def test_mini_project_5():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/")

    # Set implicit wait for all elements, Not Recommended for use
    driver.implicitly_wait(10)


    email_input = driver.find_element(By.XPATH, "//input[contains(@id, 'login-username')]")
    password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")

    email_input.send_keys("admin@admin.com")
    password_input.send_keys("admin@123")

    login_btn = driver.find_element(By.XPATH, "//button[contains(@id, 'js-login-btn')]")
    login_btn.click()

    err_msg = driver.find_element(By.ID, "js-notification-box-msg")
    print(err_msg.text)

    # time.sleep(2)
    assert err_msg.text == "Your email, password, IP address or location did not match"


# Error:
# Ah! That explains why your test is failing. The Actual : '' means Selenium found the element but its text is empty at the moment it was read. This usually happens because:
# The error message isn’t immediately present in the DOM after clicking login.
# Implicit wait only waits for the element to exist, not for its text to appear.
# Without explicit waits or a time.sleep(), Selenium may read the element too early.