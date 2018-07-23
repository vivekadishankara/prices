from selenium.webdriver.common.by import By
from lib.base_element import Element
from lib.page import Page
from sites.flipkart.results import Results
from commons.functions import CommonFunctions
from selenium.common.exceptions import NoSuchElementException


class Flipkart(Page):
    url = 'https://www.flipkart.com'
    search_box = Element(By.NAME, 'q')
    search_button = Element(By.XPATH, "//*[@type='submit']")
    close_login_notification = Element(By.XPATH, "//*[@tabindex]/div/button")

    results_page = Results()

    @classmethod
    def navigate(cls):
        super(Flipkart, cls).navigate()
        cls.close_notification()

    @classmethod
    def search_results(cls, item):
        CommonFunctions.search(cls, item)
        results = []
        for result in cls.results_page.results:
            one = {}
            result.find_element().location_once_scrolled_into_view
            for key in ['text', 'price', 'stars', 'reviews_num', 'link']:
                try:
                    element = result.get_sub_element(key)
                    if key == 'link':
                        one[key] = cls.url+element.get_attribute('href')
                    else:
                        text = element.get_attribute('textContent')
                        if key  == 'price':
                            one[key] = int(text[1:].replace(',', ''))
                        elif key == 'reviews_num':
                            one[key] = int(text[1:-1].replace(',', ''))
                        elif key == 'stars':
                            one[key] = float(text.split()[0])
                        else:
                            one[key] = text
                except NoSuchElementException:
                    one[key] = ''
            results.append(one)
        return results

    @classmethod
    def close_notification(cls):
        try:
            cls.close_login_notification.click()
        except:
            pass
