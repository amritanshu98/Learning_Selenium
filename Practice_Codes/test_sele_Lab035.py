import time
import logging
import allure
import pytest
import openpyxl
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger("selenium_test_logger")
logger.setLevel(logging.INFO)  # Capture INFO and above

# Create file handler
file_handler = logging.FileHandler(r"D:\Automation_via_Python\Learning_Selenium\Practice_Codes\selenium_project.log")
file_handler.setLevel(logging.INFO)

# Create formatter and add to handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(file_handler)

# Optional: also log to console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.info("Logger initialized successfully!")


# file_path = os.getcwd()+ "TD.xlsx"
file_path = r"D:\Automation_via_Python\Learning_Selenium\Practice_Codes\TD.xlsx"

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


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(file_path))
@allure.title("Verify Invalid Login with Excel Test Data")
@allure.description("TC#1 - Invalid Login with Excel Test Data on website: 'practice.qabrains.com'")
def test_login_ddt(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    login_practice_qabrains(username=username, password=password)



def login_practice_qabrains(username, password):
    driver = webdriver.Chrome()
    logger.info("Chrome browser started")
    driver.maximize_window()
    logger.info("Window Maximized")
    driver.get("https://practice.qabrains.com/ecommerce/login")
    logger.info("Navigated to Practice Qqabrains")

    username_input = driver.find_element(By.XPATH, "//input[@id='email']")
    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    login_btn = driver.find_element(By.XPATH, "//button[@type= 'submit']")

    username_input.send_keys(username)
    logger.info("Username Entered")
    password_input.send_keys(password)
    logger.info("Password Entered")
    login_btn.click()
    logger.info("Login Button Clicked")

    time.sleep(5)
    result= driver.current_url

    # Correct Username and Password
    # if result == "https://practice.qabrains.com/ecommerce":
    if "login" not in result:
        wait = WebDriverWait(driver=driver, timeout=10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='Products']")))
        assert "login" not in result
        logger.info("Login Successful")


    # Username and Password incorrect
    else:
        wait = WebDriverWait(driver=driver, timeout=10)
        err_msg_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//section[@aria-relevant='additions text']"))
        )

        error_text = err_msg_element.text
        logger.info(f"Login Failed: {error_text}")


        valid_errors = [
            "Username matched but password is incorrect.",
            "Neither email nor password matched."
        ]

        assert error_text in valid_errors
    # time.sleep(10)

    driver.quit()


