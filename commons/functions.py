"""
This module contains the CommonFunctions class which is a collection of common functions which
can be used in the entire module
"""
from selenium.webdriver.common.keys import Keys
from lib.driver import driver


class CommonFunctions(object):
    """
    This class is a collections of common functions that can be used throughout the module
    """
    @staticmethod
    def search(page_cls, term):
        """
        Enters a term in the search box and clicks the search_button
        :param page_cls: Class having the necessary member elements
        :param term: term to be searched
        :return: None
        """
        page_cls.search_box.wait_element()
        page_cls.search_box.set_text(term)
        page_cls.search_button.click()

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
        driver.switch_to_window(windows[curr_i+1])
        yield
        driver.close()
        driver.switch_to_window(windows[curr_i])
