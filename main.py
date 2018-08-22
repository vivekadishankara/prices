from sites.shops.amazon import Amazon
from sites.shops.snapdeal import Snapdeal
from sites.shops.flipkart import Flipkart
from framework.driver import driver


item = 'Redmi 5'

fp = 'results'
with open(fp, 'w') as f:
    with driver:
        for cls in [Amazon, Flipkart, Snapdeal]:
            cls.navigate()
            for result in cls.search_results(item, 5):
                f.write(str(result)+'\n')
