import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_using_proxy():
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=http://45.140.147.82:1081')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://whatismyipaddress.com/")
    print(driver.title)
    time.sleep(10)