import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def test_action_yatra_website():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.yatra.com/")

    wait = WebDriverWait(driver, 60)

    wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[@class='style_cross__q1ZoV']//img[@alt='cross']"))
    )
    driver.find_element(By.XPATH, "//span[@class='style_cross__q1ZoV']//img[@alt='cross']").click()


    # Departure From
    search_btn_1 = driver.find_element(By.XPATH, "//p[normalize-space()='Departure From']")

    actions = ActionChains(driver)
    (actions.move_to_element(search_btn_1).click().send_keys("Mumbai").perform())

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[normalize-space()='Chhatrapati Shivaji International']"))
    )

    (actions.move_to_element(driver.find_element(By.XPATH, "//span[text()='Mumbai']")).click().perform())


    # Going To
    search_btn_2 = driver.find_element(By.XPATH, "//p[normalize-space()='Going To']")

    actions = ActionChains(driver)
    (actions.move_to_element(search_btn_2).click().send_keys("Goa").perform())

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[normalize-space()='Manohar International Airport Airport']"))
    )

    (actions.move_to_element(driver.find_element(By.XPATH, "//span[normalize-space()='Manohar International Airport Airport']")).click().perform())

    # Date
    date_2 = driver.find_element(By.XPATH, "//span[normalize-space()='Departure Date']")

    actions = ActionChains(driver)
    (actions.move_to_element(date_2).click().perform())

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@aria-label='Choose Sunday, April 19th, 2026']//span[@aria-label='MAHA SHIVARATHIRI']"))
    )

    (actions.move_to_element(driver.find_element(
        By.XPATH,"//div[@aria-label='Choose Sunday, April 19th, 2026']//span[@aria-label='MAHA SHIVARATHIRI']")).click().perform())


    search_btn = driver.find_element(By.XPATH, "//button[text()='Search']")
    search_btn.click()

    wait.until(
        EC.url_contains('air-search-ui/dom2/trigger')
    )

    time.sleep(40)





# import time
#
# from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from dotenv import load_dotenv
# import os
#
#
# def test_022_actions():
#     load_dotenv()
#     driver = webdriver.Chrome()
#     driver.get("https://www.makemytrip.com/")
#     driver.maximize_window()
#
#     WebDriverWait(driver=driver, timeout=5).until(
#         EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))
#     )
#
#     driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()
#
#     time.sleep(2)
#
#     fromCity = driver.find_element(By.ID, "fromCity")
#
#     actions = ActionChains(driver)
#     (actions
#      .move_to_element(fromCity)
#      .click()
#      .send_keys(os.environ.get("CITY"))
#      .key_down(Keys.ARROW_DOWN)
#      .key_down(Keys.ENTER)
#      .perform())
#
#     time.sleep(10)
#
#     driver.quit()