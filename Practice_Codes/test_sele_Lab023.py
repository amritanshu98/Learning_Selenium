import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_action_builder():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    time.sleep(3)
    a_tag = driver.find_element(By.XPATH, "//a[@id = 'click']")
    a_tag.click()

    # click - Normal Driver, will find the element and click on it. release it.
    # click and Hold -> click and Hole, we will not release it.

    time.sleep(3)

    # Actions Builders - Mouse interactions

    action_builder = ActionBuilder(driver)
    action_builder.pointer_action.pointer_up(MouseButton.BACK)
    action_builder.perform()

    time.sleep(5)
    driver.quit()

