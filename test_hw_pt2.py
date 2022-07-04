import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_controls():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url_5 = "http://the-internet.herokuapp.com/frames"
        wait = WebDriverWait(chrome, 70)
        chrome.get(url_5)
        chrome.fullscreen_window()
        chrome.find_element(By.XPATH, "//a[contains(text(), 'iFrame')]").click()
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@id= 'mce_0_ifr']")))
        frame1 = chrome.find_element(By.XPATH, "//p[contains(text(),'Your content goes here.')]").text
        assert frame1 == "Your content goes here."

    finally:
        chrome.quit()
