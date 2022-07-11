import pytest
from PO.main_page import MainPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def open_browser():
    #chrome = webdriver.Chrome('./chromedriver')
    chrome = webdriver.Chrome(ChromeDriverManager().install())
    chrome.implicitly_wait(15)
    yield chrome
    chrome.quit()


def test_check_card(open_browser):
    url = "http://automationpractice.com/index.php"
    home_page = MainPage(open_browser, url)
    home_page.open()
    home_page.verify_card_is_empty()