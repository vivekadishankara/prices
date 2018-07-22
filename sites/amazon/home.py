from selenium.webdriver.common.by import By
from lib.base_element import Element
from lib.page import Page
from sites.amazon.results import Results
from commons.functions import CommonFunctions
from selenium.common.exceptions import NoSuchElementException


class Amazon(Page):
    url = 'http://www.amazon.in'
    search_box = Element(By.ID, "twotabsearchtextbox")
    search_button = Element(By.XPATH, "//*[@value='Go']")

    results_page = Results()

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
                        one[key] = element.get_attribute('href')
                    else:
                        text = element.get_attribute('textContent')
                        if key in ['price', 'reviews_num']:
                            one[key] = int(text.replace(',', ''))
                        elif key == 'stars':
                            one[key] = float(text.split()[0])
                        else:
                            one[key] = text
                except NoSuchElementException:
                    one[key] = ''
            results.append(one)
        return results
