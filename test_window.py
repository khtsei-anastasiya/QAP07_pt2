from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_robot_form():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url_4 = " http://the-internet.herokuapp.com/windows"
        chrome.get(url_4)
        #chrome.fullscreen_window()
        main_window = chrome.current_window_handle
        chrome.find_element(By.XPATH, "//a[contains(text(),'Click Here')]").click()
        time.sleep(5)
        #chrome.execute_script("window.open()")
        new_window = [window for window in chrome.window_handles if window != main_window][0]
        chrome.switch_to.window(new_window)
        #chrome.fullscreen_window()
        text_new_w = chrome.find_element(By.XPATH, "//h3[contains(text(),'New Window')]").text
        assert text_new_w == "New Window"
        time.sleep(5)
        chrome.close()
        chrome.switch_to.window(main_window)

    finally:
        chrome.quit()
