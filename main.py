from sites.shops.amazon import Amazon
from sites.shops.snapdeal import Snapdeal
from sites.shops.flipkart import Flipkart
from framework.driver import Driver


item = 'Redmi 5'

fp = 'results'

driver_new = Driver()
with open(fp, 'w') as f, driver_new as d:
    for cls in [Amazon, Flipkart, Snapdeal]:
        shop = cls(d)
        shop.navigate()
        for result in shop.search_results(item, 5):
            f.write(str(result)+'\n')
