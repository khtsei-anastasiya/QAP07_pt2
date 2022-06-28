from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_demo_qa():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url = "https://demoqa.com/text-box"
        fullname = "Test User"
        email = "test@test.pl"
        address = "Test Address"
        chrome.get(url)
        chrome.fullscreen_window()
        search_fullname = chrome.find_element(By.XPATH, "//input[@id='userName']")
        search_fullname.send_keys(fullname)
        search_email = chrome.find_element(By.XPATH, "//input[@id='userEmail']")
        search_email.send_keys(email)
        search_address = chrome.find_element(By.XPATH, "//textarea[@id='currentAddress']")
        search_address.send_keys(address)
        search_button = chrome.find_element(By.XPATH, "//button[@id='submit']")
        search_button.click()
        search_output = chrome.find_element(By.XPATH, "//p[@id='name']").text.replace("Name:", "")
        assert search_output == fullname, f"{search_output} is not equal {fullname}"
        search_output_2 = chrome.find_element(By.XPATH, "//p[@id='email']").text.replace("Email:", "")
        assert search_output_2 == email, f"{search_output_2} is not equal {email}"
        search_output_3 = chrome.find_element(By.XPATH, "//p[@id='currentAddress']").text.replace("Current Address :",
                                                                                                  "")
        assert search_output_3 == address, f"{search_output_3} is not equal {address}"

    finally:
        chrome.quit()
