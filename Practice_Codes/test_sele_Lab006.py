
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_mini_project_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    time.sleep(5)
    driver.get("https://www.google.com")
    time.sleep(5)
    driver.refresh()
    print(driver.title)
    driver.back()
    time.sleep(3)
    driver.get("https://www.bing.com")
    time.sleep(5)
    driver.refresh()
    print(driver.title)
    driver.forward()
    time.sleep(5)
    driver.quit()







    # driver.get("https://katalon-demo-cura.herokuapp.com")
    #
    # make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")
    #
    # make_appointment_element.click()
    # time.sleep(10)
    #
    # assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    #
    # driver.quit()

