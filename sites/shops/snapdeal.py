from framework.shop import ShopResults, Product, Shop


class SnapdealResults(ShopResults):
    results_locator = ('class', 'product-tuple-listing', True)
    sub_element_locators = dict(
            name="//*[contains(@class,'product-title')]",
            image="//img[contains(@class,'product-image')]",
            price="//span[contains(@class,'product-price')]",
            stars="//*[@class='rating-stars ']",
            reviews_num="//*[contains(@class,'product-rating-count')]",  # example: (3)
            link="//*[contains(@class,'product-title')]/parent::a"
        )
    see_more_link_locator = 'see-more-products'

    def __init__(self, driver, shop):
        super(SnapdealResults, self).__init__(driver)
        self.results = self.element_by_attr_partial(*self.results_locator)
        self.results.set_sub_elements(**self.sub_element_locators)
        self.see_more_link = self.element_by_id(self.see_more_link_locator)
        self.shop = shop

    def get_result_stars(self, element):
        stars_path = self.results.sub_elements.get('stars')
        link_path = self.results.sub_elements.get('link')
        link_loc = element.locator.split(stars_path)[0] + link_path
        element_link = self.element_by_xpath(link_loc)
        with self.shop.open_in_new_tab(element_link):
            stars_text = self.shop.product_page.stars.get_attribute('ratings')
        if stars_text:
            return float(stars_text)
        else:
            return ''

    def get_result_price(self, element):
        price_text = super(SnapdealResults, self).get_result_price(element)
        if price_text:
            return price_text.split()[1]
        return price_text

    def get_result_reviews_num(self, element):
        num_text = super(SnapdealResults, self).get_result_reviews_num(element)
        if num_text:
            return int(num_text[1:-1])
        return num_text


class SnapdealProduct(Product):
    stars_locators = '//*[@ratings]'

    def __init__(self, driver):
        super(SnapdealProduct, self).__init__(driver)
        self.stars = self.element_by_xpath(self.stars_locators)


class Snapdeal(Shop):
    url = 'https://www.snapdeal.com/'
    search_box_locator = 'inputValEnter'
    search_button_locator = ('class', 'searchformButton')

    def __init__(self, driver):
        super(Snapdeal, self).__init__(driver)
        self.search_box = self.element_by_id(self.search_box_locator)
        self.search_button = self.element_by_attr_partial(*self.search_button_locator)

        if self.__class__ == Snapdeal:
            self.results_page = SnapdealResults(driver, self)
            self.product_page = SnapdealProduct(driver)
