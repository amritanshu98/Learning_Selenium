from selenium import webdriver
from selenium.webdriver.common.by import By

def test_web_tables():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/webtable.html")

    row_elements = driver.find_elements(By.XPATH, "//table[contains(@id, 'customers')]/tbody/tr")
    row = len(row_elements)
    print(row)

    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id, 'customers')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)


    # //table[contains(@id, 'customers')]/tbody/tr[4]/td[2]
    # 1st Part: //table[contains(@id, 'customers')]/tbody/tr[
    # 4
    # 2nd Part: ]/td[
    # 2
    # 3rd Part: ]

    first_part = "//table[contains(@id, 'customers')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row+1):
        for j in range(1, col+1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"

            # print(dynamic_path)
            data = driver.find_element(By.XPATH, dynamic_path)
            # print(data.text)

    # find the country of "Roland Mendel"
            if "Roland Mendel" in data.text:
                country_path = f"{dynamic_path}/following-sibling::td"
                country_data = driver.find_element(By.XPATH, country_path).text
                print(f"Roland Mendel belongs to {country_data}")



