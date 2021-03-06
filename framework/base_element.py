"""
This module defines the base element class, which corresponds to each element of the webpage
The other class is the Elements class which corresponds to the repeated element present of the
webpage
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By
from configuration import TIMEOUT
from framework.driver import driver as global_driver


class Element(object):
    """
    An instance of this class maps an element on the page. It wraps around the Selenium Webdriver class.
    """
    def __init__(self, by, locator, timeout=TIMEOUT, driver=global_driver):
        self.by = by
        self.locator = locator
        self.timeout = timeout
        self.driver = driver

    def set_timeout(self, timeout=TIMEOUT):
        """
        Sets the object timeout variable to a given value. If no value is given than sets to the default value
        :param timeout: no of seconds
        :return: None
        """
        self.timeout = timeout

    def set_sub_elements(self, **kwargs):
        """
        sets the sub elements of an element
        :param kwargs: example='//*[text()='example']'
        :return: None
        """
        if self.by == By.XPATH:
            try:
                for key, value in kwargs.items():
                    self.sub_elements[key] = value
            except AttributeError:
                self.sub_elements = kwargs

    def get_sub_element(self, sub):
        """
        create a new Element object having a locator which appends the existing self.locator
        and the value keyed from self.sub_elements dictionary
        :param sub: key to the self.sub_elements
        :return: Element object
        """
        if self.by == By.XPATH:
            try:
                locator = self.locator + self.sub_elements.get(sub)
                sub_element = Element(self.by, locator, driver=self.driver)
                return sub_element
            except AttributeError:
                pass

    def get_sub_locator(self, sub):
        """
        Appends the self.locator and value keyed from self.sub_elements and returns it
        :param sub: key to the self.sub_elements
        :return: sub element locator (srt)
        """
        if self.by == By.XPATH:
            try:
                locator = self.locator + self.sub_elements.get(sub)
                return locator
            except AttributeError:
                pass

    def find_element(self):
        """
        A webdriver element of the current element using the self.by and self.locator variables
        :return: Webdriver element
        """
        try:
            element = self.driver.find_element(self.by, self.locator)
            return element
        except Exception as exception:
            return exception

    def find_elements(self):
        """
        A list of webdriver elements corresponding to the current element using the self.by and
        self.locator variables
        :return: list of Webdriver elements
        """
        try:
            elements = self.driver.find_elements(self.by, self.locator)
            return elements
        except Exception as exception:
            return exception

    @staticmethod
    def is_element(element):
        """
        The element argument is the output of the self.find_element() method or self.wait_element(True)
        This method checks it is an exception raised by the Webdriver or a Webdriver element
        :param element: output from self.find_element
        :return: True if Webdriver element
        """
        return not issubclass(element.__class__, WebDriverException)

    def wait_element(self, timeout=None, ret=False):
        """
        Waits for the element to be visible on page for timeout seconds.
        In case timeout is None, it waits for self.timeout amount of time
        :param timeout: time in seconds to wait
        :return: True if element becomes visible
        """
        if not timeout:
            timeout = self.timeout
        try:
            element = WebDriverWait(self.driver.get_driver(), timeout).until(EC.visibility_of_element_located(
                (self.by, self.locator)))
        except TimeoutException as exception:
            if ret:
                return exception
            return False
        if ret:
            return element
        return True

    def wait_elements(self, timeout=None, ret=False):
        """
        Waits for the all the element corresponding to the object to be visible on page
        for timeout seconds.
        In case timeout is None, it waits for self.timeout amount of time
        :param timeout: time in seconds to wait
        :return: True if element becomes visible
        """
        if not timeout:
            timeout = self.timeout
        try:
            element = WebDriverWait(self.driver.get_driver(), timeout).until(EC.visibility_of_all_elements_located((
                self.by, self.locator)))
        except TimeoutException as exception:
            if ret:
                return exception
            return False
        if ret:
            return element
        return True

    def wait_for_click(self, timeout=None, ret=False):
        """
        Waits for the element to be clickable for timeout seconds.
        In case timeout is None, it waits for self.timeout amount of time
        :param timeout: time in seconds to wait
        :return: True if element becomes clicakble
        """
        if not timeout:
            timeout = self.timeout
        try:
            element = WebDriverWait(self.driver.get_driver(), timeout).until(EC.element_to_be_clickable(
                (self.by, self.locator)))
        except TimeoutException as exception:
            if ret:
                return exception
            return False
        if ret:
            return element
        return True

    def send_keys(self, keys):
        """
        Sends keys passed to the current element
        :param keys: keys to be passed
        :return: None
        """
        element = self.wait_element(ret=True)
        if self.is_element(element):
            element.send_keys(keys)

    def set_text(self, text):
        """
        Clears the current text in the text field and enters new text
        :param text: text ot be written
        :return: None
        """
        element = self.wait_element(ret=True)
        if self.is_element(element):
            element.clear()
            element.send_keys(text)

    def get_attribute(self, attribute):
        """
        Gets an value of the attibute passed for the current element.
        In case, the attribute is present and has no value, it return True
        :param attribute: attribute required
        :return: value (str) or True or False if value not present
        """
        element = self.wait_element(ret=True)
        if self.is_element(element):
            attr_value = element.get_attribute(attribute)
            if attr_value == 'true':
                return True
            elif attr_value == 'false':
                return False
            else:
                return attr_value

    def get_text(self):
        """
        Waits for the elemetn to be visible and gets the text in the current element
        :return: text (str)
        """
        return self.get_attribute('textContent')

    def click(self):
        """
        Waits for the element to become clickable and clicks on it
        :return: True if successfully clicked and False otherwise
        """
        element = self.wait_for_click(ret=True)
        if self.is_element(element):
            try:
                element.click()
                return True
            except Exception:
                pass
        return False

    def __repr__(self):
        string = super(Element, self).__repr__().split()
        ins = "({0}, {1})".format(self.by, self.locator)
        string.insert(1, ins)
        return ' '.join(string)

    def __str__(self):
        return "Element ({0}, {1})".format(self.by, self.locator)


class Elements(Element):
    """
    Class inherits Element, corresponds to repeated element present on the page.
    Each instance of the repeated element is characterized by an indexed XPATH.
    Hence the self.by is By.XPATH by default
    """
    def __init__(self, xpath, timeout=TIMEOUT, driver=global_driver):
        super(Elements, self).__init__(By.XPATH, xpath, timeout, driver)
        self.i = 0
        self.num = None

    def set_i(self, i=0):
        """sets i"""
        self.i = i

    def get_i(self):
        """gets i"""
        return self.i

    def set_num(self, num):
        """sets num"""
        self.num = num

    def get_num(self):
        """gets num"""
        return self.num

    def __getitem__(self, item):
        locator_item = '(' + self.locator + ')[' + str(item) + ']'
        element = Element(self.by, locator_item, self.timeout, self.driver)
        try:
            if self.sub_elements is not None:
                element.set_sub_elements(**self.sub_elements)
        except AttributeError:
            pass
        return element

    def __len__(self):
        elements = self.find_elements()
        return len(elements)

    def __iter__(self):
        while not self.num or self.i < self.num:
            self.i += 1
            if self[self.i].wait_element():
                yield self[self.i]
            else:
                self.i -= 1 # making up for lost element
                return None

    def __call__(self, num=None):
        self.num = num
        return iter(self)
