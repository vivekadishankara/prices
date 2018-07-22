from selenium.webdriver.common.by import By
from lib.base_element import Element
from lib.page import Page
from sites.snapdeal.results import Results


class Snapdeal(Page):
    url = 'https://www.snapdeal.com/'
    search_box = Element(By.ID, "inputValEnter")
    search_button = Element(By.XPATH, "//*[contains(@class, 'searchformButton')]")

    results_page = Results()

