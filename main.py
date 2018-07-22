from sites.amazon.home import Amazon
from sites.flipkart.home import Flipkart
from sites.snapdeal.home import Snapdeal
from globals import *


driver.start_driver()
item = 'Redmi 5'
Amazon.navigate()
results = Amazon.search_results(item)

Flipkart.navigate()
Flipkart.close_notification()
results += Flipkart.search_results(item)

Snapdeal.navigate()
results += Snapdeal.search_results(item)

fp = 'results'
with open(fp, 'w') as f:
    for result in results:
        f.write(str(result)+'\n')

driver.quit()
