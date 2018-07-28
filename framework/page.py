"""
This module defines the Page class which is to be inherited by the home pages of all sites
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from framework.base_element import Element
from framework.driver import driver


class Page(object):
    """
    Page class for the Page object model.
    All other related pages for the sites inherit from object
    """
    url = None
    search_box = None
    search_button = None

    @classmethod
    def navigate(cls):
        """
        navigates to the site url
        :return: None
        """
        driver.get(cls.url)

    @staticmethod
    def text_element(text):
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

    @classmethod
    def search(cls, term):
        """
        Enters a term in the search box and clicks the search_button
        :param cls: Class having the necessary member elements
        :param term: term to be searched
        :return: None
        """
        cls.search_box.wait_element()
        cls.search_box.set_text(term)
        cls.search_button.click()

    @staticmethod
    def open_in_new_tab(element):
        """
        Open the given link in the element in a new tab and closes the new tab after the actions taken
        Used by putting in a for loop, all the actions to be taken on the new tab come inside the for loop
        :param element: link element necessary
        :return:
        """
        element.send_keys(Keys.CONTROL + Keys.ENTER)
        curr = driver.get_current_window_handle()
        windows = driver.get_window_handles()
        curr_i = windows.index(curr)
        driver.switch_to_window(windows[curr_i + 1])
        yield
        driver.close()
        driver.switch_to_window(windows[curr_i])
