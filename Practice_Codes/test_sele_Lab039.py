from selenium import webdriver
import time



def test_shadowDOM():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")

    # Need to use CSS_SELECTORS with "querySelector"
    script = 'return document.querySelector("#userName").shadowRoot.querySelector("#app2").shadowRoot.querySelector("#pizza")'

    pizza_input = driver.execute_script(script)

    pizza_input.send_keys("Margarita")

    time.sleep(5)