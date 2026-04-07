import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_flipkart_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://flipkart.com/")

    wait = WebDriverWait(driver=driver, timeout=15)

    cross_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@role='button']"))
    )
    cross_btn.click()

    list_input = driver.find_elements(By.XPATH, "//input[@placeholder='Search for Products, Brands and More']")

    keyword = "smartphone"
    actions = ActionChains(driver)
    actions.move_to_element(list_input[0]).click().perform()
    actions.send_keys_to_element(list_input[0], keyword).perform()


    search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']//*[name()='svg']")))
    actions.move_to_element(search_btn).click().perform()
    # search_btn.click()

    item_list = driver.find_elements(By.XPATH, "//div[text()='vivo T5x 5G (Star Silver, 128 GB)']")
    actions.move_to_element(item_list[0]).click().perform()



    time.sleep(10)
