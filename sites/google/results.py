from selenium.webdriver.common.by import By
from lib.base_element import Element


class Results:
    results = Element(By.XPATH, "//div/h3/a")