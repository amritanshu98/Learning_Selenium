# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# def test_shadow_dom():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://selectorshub.com/xpath-practice-page/")
#
#     element = driver.find_element(By.CSS_SELECTOR, 'input[id="pizza"]')
#     driver.execute_script("arguments[0].scrollIntoView();", element)
#     element.send_keys("Hello")

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_shadow_dom():
    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    time.sleep(3)

    # Step 1: Locate shadow host
    shadow_host = driver.find_element(By.CSS_SELECTOR, "user-name")  # Correct shadow host

    # Step 2: Get shadow root using JS
    shadow_root = driver.execute_script("return arguments[0].shadowRoot", shadow_host)

    # Step 3: Find element inside shadow root
    pizza_input = shadow_root.find_element(By.CSS_SELECTOR, "#pizza")

    # Step 4: Interact
    pizza_input.send_keys("Margherita")

    time.sleep(3)
    driver.quit()

