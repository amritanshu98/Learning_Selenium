import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_action_click_hold_release():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    #Draggable Item
    element_to_hold = driver.find_element(By.XPATH, "//div[@id= 'draggable']")
    element_to_release = driver.find_element(By.XPATH, "//div[@id='droppable']")


    # Drag and Drop in steps: Manually complete the chain
    actions = ActionChains(driver)
    actions.click_and_hold(element_to_hold).perform()
    actions.move_to_element(element_to_release).release().perform()

    # Drag and Drop in one go
    actions = ActionChains(driver)
    actions.drag_and_drop(element_to_hold, element_to_release).perform()

    wait = WebDriverWait(driver=driver, timeout=10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//strong[@id='drop-status']")))

    drop_msg_element = driver.find_element(By.XPATH, "//strong[@id='drop-status']")

    drop_msg = drop_msg_element.text
    assert drop_msg == "dropped"

    time.sleep(5)
    driver.quit()

