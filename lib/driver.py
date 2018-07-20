from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime
import configuration as config


class Driver(object):
    def start_driver(self, browser=config.browser, path_to_executable=config.path, headless=config.headless):
        """
        initializes the Driver object
        :param browser: 'Firefox' or 'Chrome'
        :param headless: boolean
        """
        self.headless = headless
        self.path = path_to_executable
        if browser.lower() == 'firefox':
            self.capabilities = webdriver.DesiredCapabilities.FIREFOX
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

    def get_driver(self):
        return self.driver

    def get(self, url):
        self.driver.get(url)

    def find_element(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)

    def take_screenshot(self, name=''):
        self.driver.save_screenshot('./images/'+name+datetime.datetime.now().strftime('%Y_%m_%d_(%H_%M).png'))

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, window):
        self.driver.switch_to.window(window)

    def refresh(self):
        self.driver.refresh()

    def page_source(self):
        return self.driver.page_source

    def page_title(self):
        return self.driver.title

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def maximize_window(self):
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()

    def close(self):
        self.driver.close()
