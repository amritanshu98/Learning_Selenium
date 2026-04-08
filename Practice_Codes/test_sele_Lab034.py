import time

import allure
import pytest
import openpyxl
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# https://practice.qabrains.com/ecommerce/login - login check with Excel 2nd project


def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append(({
            "username": username,
            "password": password
        }))
    return credentials

# file_path = os.getcwd()+ "TD.xlsx"
file_path = r"D:\Automation_via_Python\Learning_Selenium\Practice_Codes\TD.xlsx"


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(file_path))
@allure.title("Verify Invalid Login with Excel Test Data")
@allure.description("TC#1 - Invalid Login with Excel Test Data on website: 'app.vwo.com'")
def test_vwo_login(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    login_vwo(username=username, password=password)



def login_vwo(username, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")

    username_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
    password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")
    login_btn = driver.find_element(By.ID, 'js-login-btn')

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_btn.click()

    time.sleep(10)

    result= driver.current_url

    # if result != "https://app.vwo.com/#/dashboard/get-started?accountId=1218233":
    if "accountId=1218233" not in result:
        wait = WebDriverWait(driver=driver, timeout=10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='js-notification-box-msg']")))

        err_msg_element = driver.find_element(By.XPATH, "//div[@id='js-notification-box-msg']")
        print(err_msg_element.text)
        assert err_msg_element.text == "Your email, password, IP address or location did not match"

    else:
        wait = WebDriverWait(driver=driver, timeout=15)
        wait.until(EC.url_contains("#/dashboard"))
        assert "accountId=1218233" in driver.current_url
        print("Login Successful")
    # time.sleep(10)

    driver.quit()


