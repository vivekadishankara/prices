import time
from selenium.webdriver.common.by import By
from framework.base_element import Element, Elements
from framework.page import Page
from framework.shop import ShopResults, Shop


class SnapdealResults(ShopResults):
    results = Elements("//*[contains(@class, 'product-tuple-listing')]")
    results.set_sub_elements(
        name="//*[contains(@class,'product-title')]",
        # image="//img[contains(@class,'product-image')]",
        # price="//span[contains(@class,'product-price')]",
        # stars="//*[@class='rating-stars ']",
        # reviews_num="//*[contains(@class,'product-rating-count')]", #example: (3)
        # link="//*[contains(@class,'product-title')]/parent::a"
    )
    see_more_link = Element(By.ID, "see-more-products")

    @classmethod
    def get_result_stars(cls, element):
        stars_path = cls.results.sub_elements.get('stars')
        link_path = cls.results.sub_elements.get('link')
        link_loc = element.locator.split(stars_path)[0] + link_path
        element_link = Element(By.XPATH, link_loc)
        for i in Page.open_in_new_tab(element_link):
            stars_text = Snapdeal.product_page.stars.get_attribute('ratings')
        if stars_text:
            return float(stars_text)
        else:
            return ''

    @classmethod
    def get_result_price(cls, element):
        price_text = super(SnapdealResults, cls).get_result_price(element)
        if price_text:
            return price_text.split()[1]
        return price_text

    @classmethod
    def get_result_reviews_num(cls, element):
        num_text = super(SnapdealResults, cls).get_result_reviews_num(element)
        if num_text:
            return int(num_text[1:-1])
        return num_text


class Product(object):
    stars = Element(By.XPATH, "//*[@ratings]")


class Snapdeal(Shop):
    url = 'https://www.snapdeal.com/'
    search_box = Element(By.ID, "inputValEnter")
    search_button = Element(By.XPATH, "//*[contains(@class, 'searchformButton')]")

    results_page = SnapdealResults()
    product_page = Product()

    # @classmethod
    # def search_results(cls, item, num=None):
    #     # consider case for less searches appearing on page
    #     cls.search(item)
    #     results_info = []
    #     while True:
    #         for result in cls.results_page.results(num):
    #             info = cls.get_result_info(result)
    #             results_info.append(info)
    #             # print(cls.results_page.results.get_i(), len(results_info), info)
    #             if len(results_info) >= num:
    #                 cls.results_page.results.set_i()
    #                 return results_info
    #         see_more = getattr(cls.results_page, 'see_more', None)
    #         if not see_more:
    #             cls.results_page.results.set_i()
    #             if not cls.results_page.next_page_link.click():
    #                 break
    #         elif not see_more.click():
    #             break
