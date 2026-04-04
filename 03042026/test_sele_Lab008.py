import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.negative
@allure.title("VWO Invalid Login Page - test_mini_project_2")
@allure.description("Verify that with Invalid Email, Password. Error message came")
def test_mini_project_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(2)
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"

    # id -> name -> classname -> link/partial -> tagname -> css selector -> xpath.

    # Find the email, password and enter the invalid details.
    # <input type="email"
    # class="text-input W(100%)"
    # name="username" vwo-html-translate-attr="placeholder"
    # vwo-html-translate-placeholder="login:enterEmailID"
    # id="login-username"
    # data-qa="hocewoqisi"
    # placeholder="Enter email ID">

    email_web_element = driver.find_element(By.ID, "login-username")
    email_web_element.send_keys("admin@admin.com")
    time.sleep(3)

    # <input type="password"
    # class="text-input W(100%) Pend(36px)"
    # vwo-html-translate-attr="placeholder"
    # vwo-html-translate-placeholder="login:enterPassword"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # placeholder="Enter password">

    # password_web_element = driver.find_element(By.ID, "login-password")
    password_web_element = driver.find_element(By.CSS_SELECTOR, "[data-qa='jobodapuxe']")
    #CSS Selectors are Custom attribute, which we need to add in Square Bracket
    password_web_element.send_keys("admin123")
    time.sleep(2)

    see_password_svg_element = driver.find_element(By.ID, "js-password-show-icon")
    see_password_svg_element.click()
    time.sleep(5)

    submit_button = driver.find_element(By.ID, "js-login-btn")
    submit_button.click()
    time.sleep(5)

    #for Error Message
    #<div class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match
    # </div>

    err_message = driver.find_element(By.ID, "js-notification-box-msg")
    assert err_message.text == "Your email, password, IP address or location did not match"
    time.sleep(3)

    driver.quit()




