from selenium.webdriver.common.by import By
from lib.base_element import Element


class Page(object):
    @staticmethod
    def text(text):
        element = Element(By.XPATH, "//*[text()='" + text + "']")
        return element

    @staticmethod
    def text_partial(text):
        element = Element(By.XPATH, "//*[contains(text(), '" + text + "')]")
        return element
