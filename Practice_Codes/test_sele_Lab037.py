from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_tables():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable1.html")

    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")

    row_table = driver.find_elements(By.XPATH, "//table[@summary='Sample Table']/tbody/tr")

    for row in row_table:
        col_table = row.find_elements(By.TAG_NAME, "td")
        for col in col_table:
            # print(col.text)

            if "China" in col.text:
                city_path = driver.find_elements(By.XPATH, "//table[@summary='Sample Table']/tbody/tr/td/following-sibling::td[1]")
                city_data = col.find_element(By.XPATH, "following-sibling::td[1]").text
                print(city_data)