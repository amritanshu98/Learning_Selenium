import time
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_window_handling():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # STEP 1: OPEN APPLICATION
    driver.get("https://the-internet.herokuapp.com/windows")

    parent_window = driver.current_window_handle
    print("Parent Window", parent_window)

    assert len(driver.window_handles) == 1

    # STEP 2: OPEN NEW WINDOW (CLICK ACTION)
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[text()='Click Here']").click()
    time.sleep(3)

    # Wait for new window using built-in condition
    wait.until(EC.number_of_windows_to_be(2))

    windows = driver.window_handles
    print("Windows after click: ", windows)

    assert len(windows) == 2

    # STEP 3: SWITCH TO CHILD WINDOW
    child_window = None
    for window in windows:
        if window != parent_window:
            child_window = window
            break

    driver.switch_to.window(child_window)
    print("Switched to child window:", child_window)
    print("Child title:", driver.title)

    assert "New Window" in driver.page_source

    # STEP 4: PERFORM ACTION IN CHILD WINDOW

    header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    assert header.text == "New Window"

    # STEP 5: CLOSE CHILD WINDOW
    driver.close()
    print("Child Windows Closed")

    driver.switch_to.window(parent_window)
    assert driver.current_window_handle == parent_window

    # STEP 6: OPEN MULTIPLE WINDOWS (JS)
    time.sleep(3)
    driver.execute_script("window.open('https://google.com');")
    time.sleep(3)
    driver.execute_script("window.open('https://bing.com');")
    time.sleep(3)

    wait.until(EC.number_of_windows_to_be(3))
    all_windows = driver.window_handles
    print("All windows: ", all_windows)
    assert len(all_windows) == 3

    # STEP 7: ITERATE THROUGH ALL WINDOWS
    titles =[]
    for window in all_windows:
        driver.switch_to.window(window)
        titles.append(window.title)
        print("Visited: ", driver.title)

    assert len(titles) == 3

    # STEP 8: CLOSE ONLY CHILD WINDOWS
    for window in driver.window_handles:
        if window != parent_window:
            driver.switch_to.window(window)
            print("Closing: ", driver.title)
            driver.close()

    driver.switch_to.window(parent_window)
    assert len(driver.window_handles) == 1

    # STEP 9: NEGATIVE TEST (INVALID WINDOW)
    try:
        driver.switch_to.window("invalid_window")
    except Exception as e:
        print("Handled Invalid Window", str(e))

    # STEP 10: FINAL VALIDATION
    print("Final Window Title: ", driver.title)
    assert "The Internet" in driver.title

    time.sleep(3)

    driver.quit()
    print("All windows closed")




