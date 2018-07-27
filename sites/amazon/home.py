from selenium.webdriver.common.by import By
from framework.base_element import Element
from framework.shop import Shop
from sites.amazon.results import Results


class Amazon(Shop):
    url = 'http://www.amazon.in'
    search_box = Element(By.ID, "twotabsearchtextbox")
    search_button = Element(By.XPATH, "//*[@value='Go']")

    results_page = Results()

    @classmethod
    def get_result_stars(cls, element):
        stars_text = super(Amazon, cls).get_result_stars(element)
        if stars_text:
            return float(stars_text[0])
        else:
            return stars_text

    @classmethod
    def get_result_price(cls, element):
        price_text = super(Amazon, cls).get_result_price(element)
        if price_text:
            return int(price_text)
        else:
            return price_text

    @classmethod
    def get_result_reviews_num(cls, element):
        num_text = super(Amazon, cls).get_result_reviews_num(element)
        if num_text:
            return int(num_text)
        else:
            return num_text
