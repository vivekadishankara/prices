from selenium.webdriver.common.by import By
from lib.base_element import Elements


class Results:
    results = Elements("")
    results.set_sub_elements(dict(
        text=(By.XPATH, ""),
        image=(By.CLASS_NAME, ""),
        price=(By.XPATH, ""),
        stars=(By.XPATH, ""),
        reviews_num = (By.XPATH, "")
    ))