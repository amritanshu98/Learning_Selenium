import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_js_executor():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    time.sleep(3)

    click_btn = driver.find_element(By.XPATH, "//button[normalize-space()='Add Element']")

    js_executor = driver.execute_script
    js_executor("arguments[0].click();", click_btn)
    time.sleep(1)
    js_executor("arguments[0].click();", click_btn)
    time.sleep(1)
    js_executor("arguments[0].click();", click_btn)
    time.sleep(1)
    js_executor("arguments[0].click();", click_btn)
    time.sleep(1)

    # js_executor("window.scrollTo(0, 50);")
    title = js_executor("return document.title;")
    print(title)
    url = js_executor("return document.URL;")
    print(url)
    js_executor("document.body.style.zoom = '150%'")
    time.sleep(1)

    btn_add = driver.find_element(By.CLASS_NAME, "added-manually")
    # btn_add.click()
    js_executor("arguments[0].click();", btn_add)



    time.sleep(5)
