from selenium.webdriver.common.by import By
from framework.base_element import Elements


class Results:
    results = Elements("//*[contains(@class, 'product-tuple-listing')]")
    results.set_sub_elements(
        name="//*[contains(@class,'product-title')]",
        image="//img[contains(@class,'product-image')]",
        price="//span[contains(@class,'product-price')]",
        stars="//*[@class='rating-stars ']",
        reviews_num="//*[contains(@class,'product-rating-count')]", #example: (3)
        link="//*[contains(@class,'product-title')]/parent::a"
    )
