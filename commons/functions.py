from globals import *

class CommonFunctions(object):
    @staticmethod
    def search(cls, term):
        cls.search_box.wait_element()
        cls.search_box.set_text(term)
        cls.search_button.click()

    @staticmethod
    def open_in_new_tab(element):
        element.send_keys(Keys.CONTROL + Keys.ENTER)
        windows = driver.get_window_handles()
        driver.switch_to_window(windows[1])
        yield
        driver.close()
        driver.switch_to_window(windows[0])
