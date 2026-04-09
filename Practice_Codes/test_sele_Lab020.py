import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

class TestAlerts(object):
    @pytest.mark.qa
    def test_alerts_tc1_normal_alert(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        element_prompt = self.driver.find_element(By.XPATH, "//button[text() = 'Click for JS Alert']")
        element_prompt.click()

        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID, "result").text
        print(result)
        assert result == "You successfully clicked an alert"

        self.driver.quit()




    def test_alerts_tc2_confirm_alert(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        element_prompt = self.driver.find_element(By.XPATH, "//button[text() = 'Click for JS Confirm']")
        element_prompt.click()

        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.accept()

        result = self.driver.find_element(By.ID, "result").text
        print(result)
        assert result == "You clicked: Ok"

        self.driver.quit()


    def test_alerts_tc2_confirm_alert_2(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        element_prompt = self.driver.find_element(By.XPATH, "//button[text() = 'Click for JS Confirm']")
        element_prompt.click()

        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.dismiss()

        result = self.driver.find_element(By.ID, "result").text
        print(result)
        assert result == "You clicked: Cancel"

        self.driver.quit()


    def test_alerts_tc3_prompt_alert(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        element_prompt = self.driver.find_element(By.XPATH, "//button[text() = 'Click for JS Prompt']")
        element_prompt.click()

        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.send_keys("Selenium Learning")
        alert.accept()

        result = self.driver.find_element(By.ID, "result").text
        print(result)
        assert result == "You entered: Selenium Learning"

        self.driver.quit()


    def test_alerts_tc3_prompt_alert_2(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        element_prompt = self.driver.find_element(By.XPATH, "//button[text() = 'Click for JS Prompt']")
        element_prompt.click()

        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)
        wait.until(EC.alert_is_present())

        alert = Alert(self.driver)
        print(alert.text)
        alert.dismiss()

        result = self.driver.find_element(By.ID, "result").text
        print(result)
        assert result == "You entered: null"

        self.driver.quit()


    # Using switch_to method in Alert
    def test_alerts_tc3_prompt_alert_3(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        element_prompt = self.driver.find_element(By.XPATH, "//button[text() = 'Click for JS Prompt']")
        element_prompt.click()

        # Alert which is coming - stage, qa - wat
        wait = WebDriverWait(driver=self.driver, timeout=5)
        wait.until(EC.alert_is_present())

        # alert = Alert(self.driver)
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.dismiss()

        result = self.driver.find_element(By.ID, "result").text
        print(result)
        assert result == "You entered: null"

        self.driver.quit()

