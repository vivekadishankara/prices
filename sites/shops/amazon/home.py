from selenium.webdriver.common.by import By
from framework.base_element import Element, Elements
from framework.shop import ShopResults, Shop


class AmazonResults(ShopResults):
    results = Elements("//div[@class='s-item-container']")
    results.set_sub_elements(
        name="//h2",
        image="//*[@class='s-access-image cfMarker']",
        price="//*[contains(@class,'s-price')]",
        stars="//*[contains(@class,'a-icon-star')]/span",  #example: 4.2 out of 5 stars
        reviews_num="//*[contains(@class,'a-icon-star')]/following::a",
        link="//*[contains(@class,'s-access-detail-page')]"
    )
    next_page_link = Element(By.ID, "pagnNextString")

    @classmethod
    def get_result_stars(cls, element):
        stars_text = super(AmazonResults, cls).get_result_stars(element)
        if stars_text:
            return float(stars_text[0])
        return stars_text

    @classmethod
    def get_result_price(cls, element):
        price_text = super(AmazonResults, cls).get_result_price(element)
        if price_text:
            return int(price_text)
        return price_text

    @classmethod
    def get_result_reviews_num(cls, element):
        num_text = super(AmazonResults, cls).get_result_reviews_num(element)
        if num_text:
            return int(num_text)
        return num_text


class Amazon(Shop):
    url = 'http://www.amazon.in'
    search_box = Element(By.ID, "twotabsearchtextbox")
    search_button = Element(By.XPATH, "//*[@value='Go']")

    results_page = AmazonResults()
