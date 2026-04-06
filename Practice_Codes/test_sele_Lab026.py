import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_window_handles():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")
    time.sleep(2)

    parent_window = driver.current_window_handle
    print(parent_window)


    new_window_btn = driver.find_element(By.XPATH, "//a[text()='Click Here']")
    new_window_btn.click()

    window_handles = driver.window_handles
    print(window_handles)

    for handle in window_handles:
        driver.switch_to.window(handle) #child
        if "New Window" in driver.page_source:
            print("Test Case Passed !!!",handle)
            break

    # for handle in window_handles:
    #     driver.switch_to.window(handle) #child
    #     if driver.find_element(By.TAG_NAME, "h3").text == "New Window":
    #         print("Test Case Passed !!!",handle)
    #         break

    time.sleep(5)
    driver.quit()
