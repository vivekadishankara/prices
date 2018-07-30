"""
This module defines the classes required to map the sites and their common features
"""
from contextlib import contextmanager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from framework.base_element import Element, Elements
from framework.driver import driver


class PrePage(object):
    """
    This class defines locator methods that return instances of Element and Element class
    """
    @staticmethod
    def element_by_xpath(locator, multi=False):
        if multi:
            return Elements(locator)
        else:
            return Element(By.XPATH, locator)

    @staticmethod
    def element_by_name(locator):
        return Element(By.NAME, locator)

    @staticmethod
    def element_by_id(locator):
        return Element(By.ID, locator)

    @staticmethod
    def element_by_class(locator):
        return Element(By.CLASS_NAME, locator)

    @classmethod
    def text_element(cls, text, multi=False):
        """
        Gets an element characterized by the given text
        :param text: required text
        :return: Element object
        """
        locator = "//*[text()='" + text + "']"
        return cls.element_by_xpath(locator, multi)

    @classmethod
    def text_partial(cls, text, multi=False):
        """
        Gets the element which contains the given text along with other possible text
        :param text: required text
        :return: Element object
        """
        locator = "//*[contains(text(), '" + text + "')]"
        return cls.element_by_xpath(locator, multi)

    @classmethod
    def element_by_attr(cls, attr, val, multi=False):
        locator = "//*[@" + attr + "='" + val + "']"
        return cls.element_by_xpath(locator, multi)

    @classmethod
    def element_by_attr_partial(cls, attr, val, multi=False):
        locator = "//*[contains(@" + attr + ",'" + val + "')]"
        return cls.element_by_xpath(locator, multi)


class Results(PrePage):
    """
    This class maps the result page that appears after carrying out a search on a page
    """
    results = PrePage.element_by_xpath('', True)
    next_page_link = PrePage.element_by_xpath('')
    see_more_link = PrePage.element_by_xpath('')


class Page(PrePage):
    """
    Page class for the Page object model.
    All home pages inherit from this class
    """
    url = ''
    search_box = PrePage.element_by_xpath('')
    search_button = PrePage.element_by_xpath('')

    results_page = Results()

    @classmethod
    def navigate(cls):
        """
        navigates to the site url
        :return: None
        """
        driver.get(cls.url)

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
    @contextmanager
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
