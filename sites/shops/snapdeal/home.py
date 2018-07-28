from selenium.webdriver.common.by import By
from framework.base_element import Element
from framework.shop import Shop
from sites.shops.snapdeal.results import Results
from sites.shops.snapdeal.product import Product


class Snapdeal(Shop):
    url = 'https://www.snapdeal.com/'
    search_box = Element(By.ID, "inputValEnter")
    search_button = Element(By.XPATH, "//*[contains(@class, 'searchformButton')]")

    results_page = Results()
    product_page = Product()

    @classmethod
    def get_result_stars(cls, element):
        stars_path = cls.results_page.results.sub_elements.get('stars')
        link_path = cls.results_page.results.sub_elements.get('link')
        link_loc = element.locator.split(stars_path)[0] + link_path
        element_link = Element(By.XPATH, link_loc)
        for i in cls.open_in_new_tab(element_link):
            stars_text = Snapdeal.product_page.stars.get_attribute('ratings')
        if stars_text:
            return float(stars_text)
        else:
            return ''

    @classmethod
    def get_result_price(cls, element):
        price_text = super(Snapdeal, cls).get_result_price(element)
        if price_text:
            return price_text.split()[1]
        return price_text

    @classmethod
    def get_result_reviews_num(cls, element):
        num_text = super(Snapdeal, cls).get_result_reviews_num(element)
        if num_text:
            return int(num_text[1:-1])
        return num_text
