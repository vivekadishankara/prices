from framework.shop import ShopResults, Shop


class FlipkartResults(ShopResults):
    results = ShopResults.element_by_attr_partial('data-tkid', 'SEARCH', True)
    results.set_sub_elements(
        name="//a[2]",
        image="//a//img",
        price="//a[3]/div/div",
        stars="//span[contains(@id, 'productRating')]/div",  #example: '4.2 *'
        reviews_num="//div[2]/span[2]",    #example: (3,19,899)
        link="//a[2]"
    )
    next_page_link = ShopResults.text_element('Next')

    @classmethod
    def get_result_stars(cls, element):
        stars_text = super(FlipkartResults, cls).get_result_stars(element)
        if stars_text:
            return float(stars_text.split()[0])
        return stars_text

    @classmethod
    def get_result_price(cls, element):
        price_text = super(FlipkartResults, cls).get_result_price(element)
        if price_text:
            return int(price_text[1:])
        return price_text

    @classmethod
    def get_result_reviews_num(cls, element):
        num_text = super(FlipkartResults, cls).get_result_reviews_num(element)
        if num_text:
            return int(num_text[1:-1])
        return num_text


class Flipkart(Shop):
    url = 'https://www.flipkart.com'
    search_box = Shop.element_by_name('q')
    search_button = Shop.element_by_attr('type', 'submit')
    close_login_notification = Shop.element_by_xpath("//*[@tabindex]/div/button")

    results_page = FlipkartResults()

    @classmethod
    def navigate(cls):
        super(Flipkart, cls).navigate()
        cls.close_notification()

    @classmethod
    def close_notification(cls):
        try:
            cls.close_login_notification.click()
        except Exception:
            pass
