from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_controls():
    chrome = webdriver.Chrome('./chromedriver')
    try:
        url_5 = "http://the-internet.herokuapp.com/dynamic_controls"
        wait = WebDriverWait(chrome, 70)
        chrome.get(url_5)
        chrome.fullscreen_window()
        chrome.find_element(By.XPATH, "//input[@type='checkbox']")
        chrome.find_element(By.XPATH, "//button[contains(text(),'Remove')]").click()
        wait.until(EC.text_to_be_present_in_element(
            (By.XPATH, "//p[@id='message']"), "It's gone!"))
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "#checkbox")))
        chrome.find_element(By.XPATH, "//input[@type='text']").get_property('disabled')
        chrome.find_element(By.XPATH, "//button[contains(text(),'Enable')]").click()
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@id='message']"), "It's enabled!"))
        chrome.find_element(By.XPATH, "//input[@type='text']").get_property('enabled')

    finally:
        chrome.quit()
