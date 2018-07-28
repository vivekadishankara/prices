from selenium.webdriver.common.by import By
from framework.base_element import Elements


class Results:
    results = Elements("//*[contains(@data-tkid,'SEARCH')]")
    results.set_sub_elements(
        name="//a[2]",
        image="//a//img",
        price="//a[3]/div/div",
        stars="//span[contains(@id, 'productRating')]/div",  #example: '4.2 *'
        reviews_num="//div[2]/span[2]",    #example: (3,19,899)
        link="//a[2]"
    )