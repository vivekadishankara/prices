from selenium.webdriver.common.by import By
from lib.base_element import Elements


class Results:
    results = Elements("//div[@class='s-item-container']")
    results.set_sub_elements(dict(
        text=(By.XPATH, "//h2"),
        image=(By.CLASS_NAME, "s-access-image cfMarker"),
        price=(By.XPATH, "//*[contains(@class,'s-price')]"),
        stars=(By.XPATH, "//*[contains(@class,'a-icon-star')]/span"),  #example: 4.2 out of 5 stars
        reviews_num = (By.XPATH, "//*[contains(@class,'a-icon-star')]/following::a")
    ))