import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



@pytest.mark.positive
def test_select_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    driver.find_element(By.ID, "dropdown")
    select = Select(driver.find_element(By.ID, "dropdown"))
    select.select_by_visible_text("Option 2")

    time.sleep(20)

