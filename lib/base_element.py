from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from configuration import TIMEOUT
from globals import driver


class Element(object):
    def __init__(self, by, locator, timeout=TIMEOUT):
        self.by = by
        self.locator = locator
        self.timeout = timeout

    def set_sub_elements(self, **kwargs):
        """
        TODO: adding subs considering self.sub_elements already has some elements
        :subs: example = {'example1': (By.ID, 'example')}
        """
        if self.by == By.XPATH:
            try:
                for k,v in kwargs.items():
                    self.sub_elements[k] = v
            except AttributeError:
                self.sub_elements = kwargs
        return None

    def get_sub_element(self, sub):
        if self.by == By.XPATH:
            locator = self.locator + self.sub_elements.get(sub)
            sub_element = Element(self.by, locator)
            return sub_element
        else:
            return None

    def get_sub_locator(self, sub):
        if self.by == By.XPATH:
            locator = self.locator + self.sub_elements.get(sub)
            return locator
        else:
            return None

    def find_element(self):
        element = driver.find_element(self.by, self.locator)
        return element

    def find_elements(self):
        elements = driver.find_elements(self.by, self.locator)
        return elements

    def wait_element(self, timeout=None):
        if not timeout:
            timeout = self.timeout
        try:
            WebDriverWait(driver.get_driver(), timeout).until(EC.visibility_of_element_located((self.by, self.locator)))
        except TimeoutException:
            return False
        return True

    def wait_elements(self, timeout=None):
        if not timeout:
            timeout = self.timeout
        try:
            WebDriverWait(driver.get_driver(), timeout).until(EC.visibility_of_all_elements_located((
                self.by, self.locator)))
        except TimeoutException:
            return False
        return True

    def wait_for_click(self, timeout=None):
        if not timeout:
            timeout = self.timeout
        try:
            WebDriverWait(driver.get_driver(), timeout).until(EC.element_to_be_clickable((self.by, self.locator)))
        except TimeoutException:
            return False
        return True

    def send_keys(self, keys):
        element = self.find_element()
        element.send_keys(keys)

    def set_text(self, text):
        element = self.find_element()
        element.clear()
        element.send_keys(text)

    def get_attribute(self, attribute):
        element = self.find_element()
        attr_value = element.get_attribute(attribute)
        if not attr_value in ('true', 'false'):
            return attr_value
        elif attr_value=='true':
            return True
        else:
            return False

    def get_text(self):
        self.wait_element()
        element = self.find_element()
        return element.text

    def click(self):
        self.wait_for_click()
        element = self.find_element()
        element.click()

class Elements(Element):
    def __init__(self, xpath, timeout=TIMEOUT):
        super(Elements, self).__init__(By.XPATH, xpath, timeout)
        self.i = 0

    def __getitem__(self, item):
        locator_item = '(' + self.locator + ')[' + str(item) + ']'
        element = Element(self.by, locator_item)
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
        while(True):
            self.i += 1
            if self[self.i].wait_element():
                yield self[self.i]
            else:
                raise StopIteration
