import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_google():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--disable-infobars")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.google.com")
    print(driver.title)
    time.sleep(5)

