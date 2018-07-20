from selenium.webdriver.common.by import By
from lib.base_element import Elements


class Results:
    results = Elements("//*[contains(@data-tkid,'SEARCH')]")
    results.set_sub_elements(dict(
        text=(By.XPATH, "//a[2]"),
        image=(By.CLASS_NAME, "//a//img"),
        price=(By.XPATH, "//a[3]/div/div"),
        stars=(By.XPATH, "//span[contains(@id, 'productRating')]/div"),  #example: '4.2 *'
        reviews_num = (By.XPATH, "//div[2]/span[2]")    #example: (3,19,899)
    ))