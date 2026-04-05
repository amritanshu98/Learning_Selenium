import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_youtube_with_adblocker():
    chrome_options = Options()
# OR
    # chrome_options = webdriver.ChromeOptions()


    # chrome_options.add_extension("D:\\Selenium_L_Extensions\\adblocker")
    # chrome_options.add_argument("--load-extension=D:\\Selenium_L_Extensions\\adblocker")
    # chrome_options.add_argument(r"--load-extension=D:\Selenium_L_Extensions\adblocker.crx")

    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--page-load-strategy=none")
    # chrome_options.add_argument("--page-load-strategy=normal")
    # chrome_options.add_argument("--page-load-strategy=eager")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.youtube.com/")

    # time.sleep(10)
    print(driver.page_source)


