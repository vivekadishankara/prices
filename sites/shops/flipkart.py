from framework.shop import ShopResults, Shop


class FlipkartResults(ShopResults):
    def __init__(self, driver):
        super(FlipkartResults, self).__init__(driver)
        self.results = self.element_by_attr_partial('data-tkid', 'SEARCH', True)
        self.results.set_sub_elements(
            name="//*[contains(@class, '_3wU53n') or contains(@class,'_2cLu-l')]",
            image="//img[contains(@class,'_1Nyybr')]",
            price="//div[contains(@class, '_1vC4OE')]",
            stars="//span[contains(@id, 'productRating')]/div",  # example: '4.2 *'
            reviews_num="//span[contains(@class, '_38sUEc')]",    # example: (3,19,899)
            link="//a"
        )
        self.next_page_link = self.text_element('Next')

    def get_result_stars(self, element):
        stars_text = super(FlipkartResults, self).get_result_stars(element)
        if stars_text:
            return float(stars_text.split()[0])
        return stars_text

    def get_result_price(self, element):
        price_text = super(FlipkartResults, self).get_result_price(element)
        if price_text:
            return int(price_text[1:])
        return price_text

    def get_result_reviews_num(self, element):
        num_text = super(FlipkartResults, self).get_result_reviews_num(element)
        num_text = num_text.split()[0]
        num_text = num_text.replace('(', '').replace(')', '')
        if num_text:
            return int(num_text)
        return num_text


class Flipkart(Shop):
    def __init__(self, driver):
        super(Flipkart, self).__init__(driver)
        self.url = 'https://www.flipkart.com'
        self.search_box = self.element_by_name('q')
        self.search_button = self.element_by_attr('type', 'submit')
        self.close_login_notification = self.element_by_xpath("//*[@tabindex]/div/button")

        self.results_page = FlipkartResults(driver)

    def navigate(self):
        super(Flipkart, self).navigate()
        self.close_notification()

    def close_notification(self):
        try:
            self.close_login_notification.click()
        except Exception:
            pass
