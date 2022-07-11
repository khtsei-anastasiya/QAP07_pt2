from lib2to3.pgen2 import driver

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


def test_register_form():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url_3 = "https://demo.guru99.com/test/newtours/register.php"
        wait = WebDriverWait(chrome, 50)
        chrome.get(url_3)
        chrome.fullscreen_window()
        time.sleep(30)
        alert = chrome.switch_to.alert.text("//*[contains(text(), 'Управляйте конфиденциальностью')")
        alert.accept()
        wait.until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//div[contains(@class,'footer-container')]")))
        search_first_name_field = chrome.find_element(By.XPATH, "//tbody/tr[2]/td[2]/input[1]")
        search_first_name_field.send_keys("Test")
        search_last_name_field = chrome.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]")
        search_last_name_field.send_keys("User_1")
        search_phone_field = chrome.find_element(By.XPATH, "//tbody/tr[3]/td[2]/input[1]")
        search_phone_field.send_keys("123456")
        search_email_field = chrome.find_element(By.XPATH, "//input[@id='userName']")
        search_email_field.send_keys("testemail@test.com")
        search_address_field = chrome.find_element(By.XPATH, "//tbody/tr[7]/td[2]/input[1]")
        search_address_field.send_keys("Street 22")
        search_city_field = chrome.find_element(By.XPATH, "//tbody/tr[8]/td[2]/input[1]")
        search_city_field.send_keys("City123")
        search_state_field = chrome.find_element(By.XPATH, "//tbody/tr[9]/td[2]/input[1]")
        search_state_field.send_keys("State 1")
        search_zip_field = chrome.find_element(By.XPATH, "//tbody/tr[10]/td[2]/input[1]")
        search_zip_field.send_keys("22-333")
        search_country_field = chrome.find_element(By.XPATH, "//tbody/tr[11]/td[2]/select[1]")
        search_country_field.click()
        search_country_field_select = chrome.find_element(By.XPATH, "//*[contains(text(), 'AUSTRALIA')")
        time.sleep(10)
        search_country_field_select.click()
        search_username_field = chrome.find_element(By.XPATH, "//input[@id='email']")
        search_username_field.send_keys("UserName1")
        search_pass_field = chrome.find_element(By.XPATH, "//tbody/tr[14]/td[2]/input[1]")
        search_pass_field.send_keys("Pass123")
        search_pass_repeat_field = chrome.find_element(By.XPATH, "//tbody/tr[15]/td[2]/input[1]")
        search_pass_repeat_field.send_keys("Pass123")

    finally:
        chrome.quit()
