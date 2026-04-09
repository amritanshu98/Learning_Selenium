from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time



def test_alerts_tc1_normal_alert():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    element_prompt = driver.find_element(By.XPATH, "//button[text() = 'Click for JS Alert']")
    element_prompt.click()
    time.sleep(2)

    # Alert which is coming - stage, qa - wat
    wait = WebDriverWait(driver=driver, timeout=5)
    wait.until(EC.alert_is_present())

    # using import Alert
    # alert = Alert(driver)

    # using switch_to alert
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(2)

    result = driver.find_element(By.ID, "result").text
    print(result)
    assert result == "You successfully clicked an alert"

    driver.quit()