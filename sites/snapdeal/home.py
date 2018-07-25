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
        for result in cls.results_page.results:
            one = {}
            result.find_element().location_once_scrolled_into_view
            for key in ['text', 'price', 'stars', 'reviews_num', 'link']:
                try:
                    element = result.get_sub_element(key)
                    if key == 'link':
                        one[key] = element.get_attribute('href')
                    elif key == 'stars':
                        if element.wait_element(2):
                            element = result.get_sub_element('link')
                            for i in CommonFunctions.open_in_new_tab(element):
                                if Snapdeal.product_page.stars.wait_element():
                                    one['stars'] = Snapdeal.product_page.stars.get_attribute('ratings')
                        if not one.get('stars'):
                            one['stars'] = ''
                    else:
                        text = element.get_attribute('textContent')
                        if key == 'price':
                            one[key] = int(text.split()[1].replace(',', ''))
                        elif key == 'reviews_num':
                            one[key] = int(text[1:-1].replace(',', ''))
                        else:
                            one[key] = text
                except NoSuchElementException:
                    if not one.get(key):
                        one[key] = ''
                    if key == 'link':
                        one['stars'] = ''
            results.append(one)
        return results

