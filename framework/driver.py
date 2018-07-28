"""
This module defines the Driver class which wraps the Selenium Webdriver
"""
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import configuration as config


class Driver(object):
    """
    This class wraps the Selenium Webdriver and defines the driver specific methods
    """
    def start_driver(self, browser=config.BROWSER, path_to_executable=config.PATH, headless=config.HEADLESS,
                     pageLoadStrategy=config.PAGE_LOAD_STRATEGY):
        """
        Initializes the Driver object
        :param browser: 'Firefox' or 'Chrome'
        :param headless: boolean
        """
        self.headless = headless
        self.path = path_to_executable
        if browser.lower() == 'firefox':
            self.capabilities = webdriver.DesiredCapabilities.FIREFOX
            self.capabilities["pageLoadStrategy"] = pageLoadStrategy
            self.profile = webdriver.FirefoxProfile()
            self.profile.set_preference("browser.tabs.remote.autostart", False)
            self.profile.set_preference("browser.tabs.remote.autostart.1", False)
            self.profile.set_preference("browser.tabs.remote.autostart.2", False)
            self.profile.set_preference("dom.webnotifications.enabled", False)
            self.options = Options()
            if self.headless:
                self.options.add_argument('--headless')
            self.driver = webdriver.Firefox(executable_path=self.path, capabilities=self.capabilities,
                                            firefox_profile=self.profile, options=self.options)
            self.maximize_window()

    def get_driver(self):
        """
        Return the driver
        :return: None
        """
        return self.driver

    def get(self, url):
        """
        Navigates to the given url
        :param url: url of the website
        :return: None
        """
        self.driver.get(url)

    def find_element(self, by, locator):
        """
        Wraps the Webdriver.find_element
        :param by: locator strategy
        :param locator: locator
        :return: element
        """
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        """
        Wraps the Webdriver.find_elements
        :param by: locator strategy
        :param locator: locator
        :return: list of elements
        """
        return self.driver.find_elements(by, locator)

    def take_screenshot(self, name=''):
        """
        Take a screenshot of the current browser state with the given name and timestamp
        :param name: name to be appended to the filename
        :return: None
        """
        self.driver.save_screenshot('./images/'+name+datetime.datetime.now().strftime('%Y_%m_%d_(%H_%M).png'))

    def get_current_window_handle(self):
        """
        Return current window handles
        :return: window handle (str)
        """
        return self.driver.current_window_handle

    def get_window_handles(self):
        """
        Returns a list of window handles currently active on the window
        :return: list of str(int)
        """
        return self.driver.window_handles

    def switch_to_window(self, window):
        """
        Switches to the given tab
        :param window: window handle of the required tab
        :return: None
        """
        self.driver.switch_to.window(window)

    def refresh(self):
        """
        Switches the current tab
        :return: None
        """
        self.driver.refresh()

    def page_source(self):
        """
        Returns the url on the current tab
        :return: url (str)
        """
        return self.driver.page_source

    def page_title(self):
        """
        Returns the page title
        :return: page title (str)
        """
        return self.driver.title

    def back(self):
        """
        Takes the current tab back one page
        :return: None
        """
        self.driver.back()

    def forward(self):
        """
        Takes the current tab forward one page
        :return: None
        """
        self.driver.forward()

    def maximize_window(self):
        """
        Maximizes the current window
        :return: None
        """
        self.driver.maximize_window()

    def quit(self):
        """
        Closes the current window and ends the webdriver session
        :return: None
        """
        self.driver.quit()

    def close(self):
        """
        Closes the current tab while the webdriver session continues in the remaining tabs on the window
        :return: None
        """
        self.driver.close()


driver = Driver()
