from selenium.webdriver.common.by import By
from lib.base_element import Elements


class Results:
    results = Elements("//div[@class='s-item-container']")
    results.set_sub_elements(
        text="//h2",
        image="//*[@class='s-access-image cfMarker']",
        price="//*[contains(@class,'s-price')]",
        stars="//*[contains(@class,'a-icon-star')]/span",  #example: 4.2 out of 5 stars
        reviews_num ="//*[contains(@class,'a-icon-star')]/following::a",
        link="//*[contains(@class,'s-access-detail-page')]"
    )