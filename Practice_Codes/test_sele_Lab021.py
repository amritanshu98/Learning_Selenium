import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCheckboxes(object):
    @pytest.mark.qa
    def test_tc1_checkbox(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/checkboxes")
        time.sleep(3)
        checkboxes = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        checkboxes[0].click()
        time.sleep(5)
        print("Clicked !!!")

        self.driver.quit()