from selenium.webdriver.common.by import By
from lib.base_element import Element
from lib.page import Page
from sites.flipkart.results import Results


class Flipkart(Page):
    url = 'https://www.flipkart.com'
    search_box = Element(By.NAME, 'q')
    search_button = Element(By.XPATH, "//*[@type='submit']")
    close_login_notification = Element(By.XPATH, "//*[@tabindex]/div/button")

    results_page = Results()