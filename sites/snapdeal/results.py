from selenium.webdriver.common.by import By
from lib.base_element import Elements


class Results:
    results = Elements("//*[contains(@class, 'product-tuple-listing')]")
    results.set_sub_elements(dict(
        text=(By.XPATH, "//*[contains(@class,'product-title')]"),
        image=(By.XPATH, "//img[contains(@class,'product-image')]"),
        price=(By.XPATH, "//span[contains(@class,'product-price')]"),
        stars=(By.XPATH, ""),   
        reviews_num = (By.XPATH, "//*[contains(@class,'product-rating-count')]") #example: (3)
    ))