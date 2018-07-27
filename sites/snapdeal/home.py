from selenium.webdriver.common.by import By
from lib.base_element import Element
from lib.page import Page
from sites.snapdeal.results import Results
from sites.snapdeal.product import Product
from commons.functions import CommonFunctions
from selenium.common.exceptions import NoSuchElementException


class Snapdeal(Page):
    url = 'https://www.snapdeal.com/'
    search_box = Element(By.ID, "inputValEnter")
    search_button = Element(By.XPATH, "//*[contains(@class, 'searchformButton')]")

    results_page = Results()
    product_page = Product()

    @classmethod
    def search_results(cls, item):
        CommonFunctions.search(cls, item)
        results = []
        for result in cls.results_page.results(20):
            info = cls.get_result(result)
            results.append(info)
        return results

    @staticmethod
    def get_result(result):
        info = {}
        result.find_element().location_once_scrolled_into_view
        for key in result.sub_elements.keys():
            element = result.get_sub_element(key)
            if key == 'link':
                info[key] = element.get_attribute('href')
            elif key == 'image':
                info[key] = element.get_attribute('src')
            elif key == 'stars':
                element = result.get_sub_element('link')
                for i in CommonFunctions.open_in_new_tab(element):
                    info['stars'] = Snapdeal.product_page.stars.get_attribute('ratings')
            else:
                text = element.get_text()
                if text:
                    if key == 'price':
                        info[key] = int(text.split()[1].replace(',', ''))
                    elif key == 'reviews_num':
                        info[key] = int(text[1:-1].replace(',', ''))
                    else:
                        info[key] = text
            if not info.get(key):
                info[key] = ''
        return info
