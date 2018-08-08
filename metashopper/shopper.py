from framework.driver import driver
from framework.shop import ShopResults
from sites.shops.amazon.home import Amazon
from sites.shops.flipkart.home import Flipkart
from sites.shops.snapdeal.home import Snapdeal


SHOPS = {'Amazon': Amazon,
         'Flipkart': Flipkart,
         'Snapdeal': Snapdeal}
ITEM_ATTR = ShopResults.results.sub_elements.keys()


def simple_search(item, shops, nums):
    results = {}
    with driver:
        for shop, num in zip(shops, nums):
            shopclass = SHOPS[shop]
            shopclass.navigate()
            result = shopclass.search_results(item, num)
            results[shop] = result
    return results