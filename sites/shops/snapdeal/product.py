from selenium.webdriver.common.by import By
from framework.base_element import Element


class Product(object):
    stars = Element(By.XPATH, "//*[@ratings]")