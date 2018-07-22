from selenium.webdriver.common.by import By
from lib.base_element import Element
from globals import driver


class Page(object):
    url = ''

    @classmethod
    def navigate(cls):
        driver.get(cls.url)

    @staticmethod
    def text(text):
        element = Element(By.XPATH, "//*[text()='" + text + "']")
        return element

    @staticmethod
    def text_partial(text):
        element = Element(By.XPATH, "//*[contains(text(), '" + text + "')]")
        return element
