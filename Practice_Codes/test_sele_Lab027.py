import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_window_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.spicejet.com")

    input_src = driver.find_element(By.XPATH, "//div[@data-testid='to-testID-origin']/div/div/input")

    actions = ActionChains(driver)
    # actions.move_to_element(input_src).perform()
    # actions.send_keys_to_element(input_src, "BLR").perform()

    actions.move_to_element(input_src).click().send_keys("BLR").perform()

    input_dest = driver.find_element(By.XPATH, "//div[@data-testid='to-testID-destination']/div/div/input")
    # actions.move_to_element(input_src).perform()
    # actions.send_keys_to_element(input_dest, "DEL").perform()

    actions.move_to_element(input_dest).click().send_keys("DEL").perform()







    time.sleep(5)
    driver.quit()