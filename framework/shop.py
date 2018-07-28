"""
This module defines the Shop class which is to be inherited by the home pages of all shops
"""
from framework.page import Page


class Shop(Page):
    """
    Home pages of all sites inherit from this class
    """
    @staticmethod
    def get_result_link(element):
        """
        Takes the link sub_element of the result and extracts the link
        :param element: link element
        :return: link
        """
        return element.get_attribute('href')

    @staticmethod
    def get_result_image(element):
        """
        Takes the image sub_element of the result and returns the image source
        :param element: image element
        :return: image source
        """
        return element.get_attribute('src')

    @staticmethod
    def get_result_stars(element):
        """
        Takes the stars sub_element of the result and returns the stars
        :param element:stars element
        :return: stars in text
        """
        stars_text = element.get_text()
        if stars_text:
            return stars_text
        return ''

    @staticmethod
    def get_result_price(element):
        """
        Takes the price sub_element of the result and return the price
        :param element: price element
        :return: price in text
        """
        price_text = element.get_text()
        if price_text:
            return price_text.replace(',', '')
        return ''

    @staticmethod
    def get_result_reviews_num(element):
        """
        Takes the reviews_num sub_element of the result and return the text in the element
        :param element: reviews_num element
        :return: number of reviews in text
        """
        num_text = element.get_text()
        if num_text:
            return num_text.replace(',', '')
        return ''

    @staticmethod
    def get_result_name(element):
        """
        Takes the name sub_element of the result and returns the name of the result
        :param element: name element
        :return: name
        """
        name_text = element.get_text()
        if name_text:
            return name_text
        return ''

    @classmethod
    def get_result_info(cls, result):
        """
        Collects the information from a result and returns as a dictionary
        :param result: result from the results_page
        :return: info from results
        """
        info = {}
        result.find_element().location_once_scrolled_into_view
        for key in result.sub_elements.keys():
            element = result.get_sub_element(key)
            info[key] = getattr(cls, 'get_result_' + key)(element)
            if not info.get(key):
                info[key] = ''
        return info

    @classmethod
    def search_results(cls, item):
        cls.search(item)
        results = []
        for result in cls.results_page.results():
            info = cls.get_result_info(result)
            results.append(info)
        return results
