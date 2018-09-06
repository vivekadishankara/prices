from framework.driver import Driver
from framework.shop import RESULT_SUB_ELEMENTS
from sites.shops.amazon import Amazon
from sites.shops.flipkart import Flipkart
from sites.shops.snapdeal import Snapdeal


SHOPS = {'Amazon': Amazon,
         'Flipkart': Flipkart,
         'Snapdeal': Snapdeal}


def simple_search(item, shops, nums):
    results = {}
    driver = Driver()
    with driver as d:
        for shop, num in zip(shops, nums):
            shopobj = SHOPS[shop](d)
            shopobj.navigate()
            result = shopobj.search_results(item, num)
            results[shop] = result
    return results