from sites.amazon.home import Amazon
from sites.flipkart.home import Flipkart
from sites.snapdeal.home import Snapdeal
from lib.driver import driver


driver.start_driver()
item = 'Redmi 5'

fp = 'results'
with open(fp, 'w') as f:
    for cls in [Amazon, Flipkart, Snapdeal]:
        cls.navigate()
        for result in cls.search_results(item):
            f.write(str(result)+'\n')

driver.quit()
