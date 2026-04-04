import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert

class TestCheckboxes(object):
    @pytest.mark.qa
    def test_alerts_tc1_checkbox(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        checkboxes[0].click()
        time.sleep(5)

        self.driver.quit()