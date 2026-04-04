import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType


def test_mini_project_7():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    allure.attach(driver.get_screenshot_as_png(), name="Step1_Open_URL", attachment_type=AttachmentType.PNG)

    make_appointment = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    make_appointment.click()

    WebDriverWait(driver=driver, timeout=5).until(
        EC.url_contains('/profile.php#login')
    )
    allure.attach(driver.get_screenshot_as_png(), name="Step2_Login_Page", attachment_type=AttachmentType.PNG)


    username_input = driver.find_element(By.CSS_SELECTOR, "#txt-username")
    password_input = driver.find_element(By.CSS_SELECTOR, "#txt-password")

    username_input.send_keys("John Doe")
    password_input.send_keys("ThisIsNotAPassword")

    WebDriverWait(driver=driver, timeout=3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#btn-login")))

    login_btn = driver.find_element(By.CSS_SELECTOR, "#btn-login")
    login_btn.click()

    allure.attach(driver.get_screenshot_as_png(), name="Step3_Login_Click", attachment_type=AttachmentType.PNG)

    WebDriverWait(driver=driver, timeout=15).until(
        EC.url_contains('#appointment')
    )

    h2_element = driver.find_element(By.XPATH, "//h2[text()='Make Appointment']")
    allure.attach(driver.get_screenshot_as_png(), name="Step 4 PNG", attachment_type=AttachmentType.PNG)
    assert h2_element.text == "Make Appointment"




