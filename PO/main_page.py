from PO.base_page import BasePage
from PO.locators_main_page import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def verify_card_is_empty(self):
        assert self.is_element_present(MainPageLocators.card), "Card is not empty"
