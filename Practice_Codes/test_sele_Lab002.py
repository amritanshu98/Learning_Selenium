import time

from selenium import webdriver

def test_open_google():
    driver = webdriver.Chrome()
    # Code -> HTTP REQUEST - POST
    # POST request | Create the Session
    # Session is created - Unique ID - 16-digit ID
    # 6f25aae2e1b81aaa1e0cc48dc7b1898c

    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()

    # driver.maximize_window()

    # Code -> HTTP REQUEST -. CHROMEdRIVER -> CHROME (SessionID)
    print(driver.session_id)
    driver.get("https://www.google.com")
    print(driver.title)
    assert driver.title == "Google"

    time.sleep(5)