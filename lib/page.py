"""
This module defines the Page class which is to be inherited by the home pages of all sites
"""
from selenium.webdriver.common.by import By
from lib.base_element import Element
from lib.driver import driver


class Page(object):
    """
    Page class for the Page object model. Home pages of all sites inherit from this class
    All other related pages for the sites inherit from object
    """
    url = ''

    @classmethod
    def navigate(cls):
        """
        navigates to the site url
        :return: None
        """
        driver.get(cls.url)

    @staticmethod
    def text(text):
        """
        Gets an element characterized by the given text
        :param text: required text
        :return: Element object
        """
        element = Element(By.XPATH, "//*[text()='" + text + "']")
        return element

    @staticmethod
    def text_partial(text):
        """
        Gets the element which contains the given text along with other possible text
        :param text: required text
        :return: Element object
        """
        element = Element(By.XPATH, "//*[contains(text(), '" + text + "')]")
        return element
