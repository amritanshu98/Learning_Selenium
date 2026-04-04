import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

def test_mini_project_4():
    chrome_options = Options()

    chrome_options.add_argument("--incognito")

    # prefs = {
    # "credentials_enable_service": False,
    # "profile.password_manager_enabled": False,
    # "profile.password_manager_leak_detection": False
    #  }
    #
    # chrome_options.add_experimental_option("prefs", prefs)


    driver = webdriver.Chrome(options=chrome_options)

    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(3)
    make_appointment_btn = driver.find_element(By.ID, "btn-make-appointment")
    make_appointment_btn.click()
    time.sleep(3)

    username_input = driver.find_element(By.ID, "txt-username")
    username_input.send_keys("John Doe")

    password_input = driver.find_element(By.ID, "txt-password")
    password_input.send_keys("ThisIsNotAPassword")
    time.sleep(2)

    login_btn = driver.find_element(By.ID, "btn-login")
    login_btn.click()
    time.sleep(10)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    appointment = driver.find_element(By.XPATH, "//*[@id='appointment']/div/div/div/h2[text()='Make Appointment']")
    assert appointment.text == "Make Appointment"

