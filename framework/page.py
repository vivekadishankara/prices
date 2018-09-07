"""
This module defines the classes required to map the sites and their common features
"""
from contextlib import contextmanager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from framework.base_element import Element, Elements
from framework.driver import driver as global_driver


class PrePage(object):
    """
    This class defines locator methods that return instances of Element and Element class
    """
    def __init__(self, driver=global_driver):
        self.driver = driver

    def element_by_xpath(self, locator, multi=False):
        if multi:
            return Elements(locator, driver=self.driver)
        else:
            return Element(By.XPATH, locator, driver=self.driver)

    def element_by_name(self, locator):
        return Element(By.NAME, locator, driver=self.driver)

    def element_by_id(self, locator):
        return Element(By.ID, locator, driver=self.driver)

    def element_by_class(self, locator):
        return Element(By.CLASS_NAME, locator, driver=self.driver)

    def text_element(self, text, multi=False):
        """
        Gets an element characterized by the given text
        :param text: required text
        :param multi: bool to create object of Element or Elements
        :return: Element object
        """
        locator = "//*[text()='" + text + "']"
        return self.element_by_xpath(locator, multi)

    def text_partial(self, text, multi=False):
        """
        Gets the element which contains the given text along with other possible text
        :param text: required text
        :param multi: bool to create object of Element or Elements
        :return: Element object
        """
        locator = "//*[contains(text(), '" + text + "')]"
        return self.element_by_xpath(locator, multi)

    def element_by_attr(self, attr, val, multi=False):
        locator = "//*[@" + attr + "='" + val + "']"
        return self.element_by_xpath(locator, multi)

    def element_by_attr_partial(self, attr, val, multi=False):
        locator = "//*[contains(@" + attr + ",'" + val + "')]"
        return self.element_by_xpath(locator, multi)


class Results(PrePage):
    """
    This class maps the result page that appears after carrying out a search on a page
    """
    results_locator = ''
    next_page_link_locator = ''
    see_more_link_locator = ''

    def __init__(self, driver):
        super(Results, self).__init__(driver)
        self.results = self.element_by_xpath(self.results_locator, True)
        self.next_page_link = self.element_by_xpath(self.next_page_link_locator)
        self.see_more_link = self.element_by_xpath(self.see_more_link_locator)


class Page(PrePage):
    """
    Page class for the Page object model.
    All home pages inherit from this class
    """
    url = ''
    search_box_locator = ''
    search_button_locator = ''

    def __init__(self, driver):
        super(Page, self).__init__(driver)
        self.search_box = self.element_by_xpath(self.search_box_locator)
        self.search_button = self.element_by_xpath(self.search_button_locator)

        if self.__class__ == Page:
            self.results_page = Results(driver)

    def navigate(self):
        """
        navigates to the site url
        :return: None
        """
        self.driver.get(self.url)

    def search(self, term):
        """
        Enters a term in the search box and clicks the search_button
        :param self: Class having the necessary member elements
        :param term: term to be searched
        :return: None
        """
        self.search_box.wait_element()
        self.search_box.set_text(term)
        self.search_button.click()

    @contextmanager
    def open_in_new_tab(self, element):
        """
        Open the given link in the element in a new tab and closes the new tab after the actions taken
        Used by putting in a for loop, all the actions to be taken on the new tab come inside the for loop
        :param element: link element necessary
        :return:
        """
        element.send_keys(Keys.CONTROL + Keys.ENTER)
        curr = self.driver.get_current_window_handle()
        windows = self.driver.get_window_handles()
        curr_i = windows.index(curr)
        self.driver.switch_to_window(windows[curr_i + 1])
        yield
        self.driver.close()
        self.driver.switch_to_window(windows[curr_i])
