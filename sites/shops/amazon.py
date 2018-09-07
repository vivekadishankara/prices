from framework.shop import ShopResults, Shop


class AmazonResults(ShopResults):
    results_locator = "//div[@class='s-item-container']"
    next_page_link_locator = 'pagnNextString'
    sub_element_locators = dict(
            name="//h2",
            image="//*[@class='s-access-image cfMarker']",
            price="//*[contains(@class,'s-price')]",
            stars="//*[contains(@class,'a-icon-star')]/span",  # example: 4.2 out of 5 stars
            reviews_num="//*[contains(@class,'a-icon-star')]/following::a",
            link="//*[contains(@class,'s-access-detail-page')]"
        )

    def __init__(self, driver):
        super(AmazonResults, self).__init__(driver)
        self.next_page_link = self.element_by_id(self.next_page_link_locator)

    def get_result_stars(self, element):
        stars_text = super(AmazonResults, self).get_result_stars(element)
        if stars_text:
            return float(stars_text[0])
        return stars_text

    def get_result_price(self, element):
        price_text = super(AmazonResults, self).get_result_price(element)
        if price_text:
            if '-' in price_text:
                price_text = price_text.split('-')[0]
            return int(float(price_text))
        return price_text

    def get_result_reviews_num(self, element):
        num_text = super(AmazonResults, self).get_result_reviews_num(element)
        if num_text:
            return int(num_text)
        return num_text


class Amazon(Shop):
    url = 'http://www.amazon.in'
    search_box_locator = 'twotabsearchtextbox'
    search_button_locator = ('value', 'Go')

    def __init__(self, driver):
        super(Amazon, self).__init__(driver)
        self.search_box = self.element_by_id(self.search_box_locator)
        self.search_button = self.element_by_attr(*self.search_button_locator)

        if self.__class__ == Amazon:
            self.results_page = AmazonResults(driver)
