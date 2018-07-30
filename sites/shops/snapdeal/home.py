from framework.shop import ShopResults, Product, Shop


class SnapdealResults(ShopResults):
    results = ShopResults.element_by_attr_partial('class', 'product-tuple-listing', True)
    results.set_sub_elements(
        name="//*[contains(@class,'product-title')]",
        image="//img[contains(@class,'product-image')]",
        price="//span[contains(@class,'product-price')]",
        stars="//*[@class='rating-stars ']",
        reviews_num="//*[contains(@class,'product-rating-count')]", #example: (3)
        link="//*[contains(@class,'product-title')]/parent::a"
    )
    see_more_link = ShopResults.element_by_id('see-more-products')

    @classmethod
    def get_result_stars(cls, element):
        stars_path = cls.results.sub_elements.get('stars')
        link_path = cls.results.sub_elements.get('link')
        link_loc = element.locator.split(stars_path)[0] + link_path
        element_link = ShopResults.element_by_xpath(link_loc)
        with Shop.open_in_new_tab(element_link):
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


class SnapdealProduct(Product):
    stars = Product.element_by_xpath('//*[@ratings]')


class Snapdeal(Shop):
    url = 'https://www.snapdeal.com/'
    search_box = Shop.element_by_id('inputValEnter')
    search_button = Shop.element_by_attr_partial('class', 'searchformButton')

    results_page = SnapdealResults()
    product_page = SnapdealProduct()
