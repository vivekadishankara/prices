from selenium.webdriver.common.by import By
from framework.base_element import Element
from framework.shop import Shop
from sites.shops.flipkart.results import Results


class Flipkart(Shop):
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
    def close_notification(cls):
        try:
            cls.close_login_notification.click()
        except:
            pass

    @classmethod
    def get_result_stars(cls, element):
        stars_text = super(Flipkart, cls).get_result_stars(element)
        if stars_text:
            return float(stars_text.split()[0])
        else:
            return stars_text

    @classmethod
    def get_result_price(cls, element):
        price_text = super(Flipkart, cls).get_result_price(element)
        if price_text:
            return int(price_text[1:])
        else:
            return price_text

    @classmethod
    def get_result_reviews_num(cls, element):
        num_text = super(Flipkart, cls).get_result_reviews_num(element)
        if num_text:
            return int(num_text[1:-1])
        else:
            return num_text
