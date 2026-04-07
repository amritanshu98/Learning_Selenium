import time
import pytest
import allure
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# -------------------------
# Configure Logging
# -------------------------
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


# -------------------------
# Test Function
# -------------------------
def test_mini_project_7():
    driver = webdriver.Chrome()
    logger.info("Chrome browser started")
    driver.maximize_window()
    logger.info("Browser window maximized")

    try:
        # Step 1: Open URL
        driver.get("https://katalon-demo-cura.herokuapp.com/")
        logger.info("Navigated to Katalon demo site")
        allure.attach(driver.get_screenshot_as_png(), name="Step1_Open_URL", attachment_type=AttachmentType.PNG)

        # Step 2: Click "Make Appointment"
        make_appointment = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
        make_appointment.click()
        logger.info("Clicked 'Make Appointment' button")

        WebDriverWait(driver=driver, timeout=5).until(
            EC.url_contains('/profile.php#login')
        )
        logger.info("Login page loaded")
        allure.attach(driver.get_screenshot_as_png(), name="Step2_Login_Page", attachment_type=AttachmentType.PNG)

        # Step 3: Fill username and password
        username_input = driver.find_element(By.CSS_SELECTOR, "#txt-username")
        password_input = driver.find_element(By.CSS_SELECTOR, "#txt-password")

        username_input.send_keys("John Doe")
        password_input.send_keys("ThisIsNotAPassword")
        logger.info("Entered username and password")

        WebDriverWait(driver=driver, timeout=3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#btn-login"))
        )

        # Step 4: Click login
        login_btn = driver.find_element(By.CSS_SELECTOR, "#btn-login")
        login_btn.click()
        logger.info("Clicked login button")
        allure.attach(driver.get_screenshot_as_png(), name="Step3_Login_Click", attachment_type=AttachmentType.PNG)

        # Step 5: Wait for appointment page
        WebDriverWait(driver=driver, timeout=15).until(
            EC.url_contains('#appointment')
        )
        logger.info("Appointment page loaded")

        # Step 6: Verify appointment heading
        h2_element = driver.find_element(By.XPATH, "//h2[text()='Make Appointment']")
        allure.attach(driver.get_screenshot_as_png(), name="Step4_Make_Appointment_Page", attachment_type=AttachmentType.PNG)
        assert h2_element.text == "Make Appointment"
        logger.info("Verified 'Make Appointment' heading successfully")

    except NoSuchElementException as e:
        logger.error(f"Element not found: {e}", exc_info=True)
        pytest.fail(f"Test failed due to missing element: {e}")

    except TimeoutException as e:
        logger.error(f"Timeout waiting for element or page: {e}", exc_info=True)
        pytest.fail(f"Test failed due to timeout: {e}")

    except Exception as e:
        logger.critical(f"Unexpected error: {e}", exc_info=True)
        pytest.fail(f"Test failed due to unexpected error: {e}")

    finally:
        driver.quit()
        logger.info("Browser closed")