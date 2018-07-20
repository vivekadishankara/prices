from selenium.webdriver.common.by import By
from lib.base_element import Element
from lib.page import Page
from sites.amazon.results import Results


class Amazon(Page):
    url = 'http://www.amazon.in'
    search_box = Element(By.ID, "twotabsearchtextbox")
    search_button = Element(By.XPATH, "//*[@value='Go']")

    results_page = Results()

