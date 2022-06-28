from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def test_drop_downs():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url_2 = "https://demoqa.com/select-menu"
        chrome.get(url_2)
        chrome.fullscreen_window()
        search_dd1 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select Option')]")
        search_dd1.click()
        search_dd1_value = chrome.find_element(By.XPATH, "//*[contains(text(), 'Group 1, option 2')]")
        search_dd1_value.click()
        search_dd1_filled = chrome.find_element(By.XPATH, "//*[contains(text(), 'Group 1, option 2')]")
        assert search_dd1_filled.text == 'Group 1, option 2'

        search_dd2 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select Title')]")
        search_dd2.click()
        search_dd2_value = chrome.find_element(By.XPATH, "//*[contains(text(), 'Mrs.')]")
        search_dd2_value.click()
        search_dd2_filled = chrome.find_element(By.XPATH, "//*[contains(text(), 'Mrs.')]")
        assert search_dd2_filled.text == 'Mrs.'

        search_dd3 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Red')]")
        search_dd3.click()
        search_dd3_value = chrome.find_element(By.XPATH, "//*[contains(text(), 'Black')]")
        search_dd3_value.click()
        search_dd3_filled = chrome.find_element(By.XPATH, "//*[contains(text(), 'Black')]")
        assert search_dd3_filled.text == 'Black'

        search_dd4 = chrome.find_element(By.XPATH, "//*[contains(text(), 'Select...')]")
        search_dd4.click()
        search_dd4_value = chrome.find_element(By.XPATH, "//*[contains(text(), 'Blue')]")
        search_dd4_value.click()
        search_dd4_filled = chrome.find_element(By.XPATH, "//*[contains(text(), 'Blue')]")
        assert search_dd4_filled.text == 'Blue'
        time.sleep(2)

    finally:
        chrome.quit()