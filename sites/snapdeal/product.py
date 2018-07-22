from lib.base_element import Element
from selenium.webdriver.common.by import By


class Product(object):
    stars = Element(By.XPATH, "//*[@ratings]")