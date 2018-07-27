from selenium.webdriver.common.by import By
from framework.base_element import Element
from framework.page import Page
from sites.google.results import Results


class Google(Page):
    url = 'http://www.google.com'
    search_box = Element(By.NAME, 'q')
    search_button = Element(By.XPATH, "//input[@type='submit'][@value='Google Search']")

    result_page = Results()
