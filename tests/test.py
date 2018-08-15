import os
import pytest
from pylint import epylint as lint
from framework.driver import driver
import configuration
from sites.shops.amazon.home import Amazon
from sites.shops.flipkart.home import Flipkart
from sites.shops.snapdeal.home import Snapdeal
from api.models import Item, Result
from api import db


@pytest.fixture(scope='class')
def price_fixture():
    driver.start_driver()
    yield
    driver.quit()


class TestCode(object):
    def test_pylint_review(self):
        lint_stdout, lint_stderr = lint.py_run('..', return_std=True)
        for line in lint_stdout:
            if not line.isspace():
                spaced = line.split()
                assert not 'error' in spaced
        score = float(spaced[6].split('/')[0])
        assert score > 5.0
        print(line)


#@pytest.mark.usefixtures('price_fixture')
class TestPrice(object):
    @pytest.mark.parametrize('item', (['Redmi 5']))
    def test_search_basic(self, item):
        item_num = configuration.SEARCH_RESERVE
        fp = 'results'
        with open(fp, 'w') as f, driver:
            for shop in [Amazon, Flipkart, Snapdeal]:
                shop.navigate()
                results = []
                for result in shop.search_results(item, item_num):
                    f.write(str(result) + '\n')
                    results.append(result)
                    for sub in shop.results_page.results.sub_elements:
                        assert result.get(sub) is not None
                assert len(results) == item_num


class TestApi(object):
    def test_db(self):
        item = 'Redmi 5'
        fp = 'results'
        if not os.path.exists(fp):
            test_price_obj = TestPrice()
            test_price_obj.test_search_basic(item)

        results = []
        with open(fp) as f:
            for line in f:
                result = eval(line)
                if not result['stars']:
                    result['stars'] = 0.0
                results.append(result)

        it = Item.query.filter_by(itemname=item).first()
        if it:
            it.results.delete()
            db.session.commit()
        else:
            it = Item(itemname=item)
            db.session.add(it)
            db.session.commit()

        for i in range(len(results)):
            result_db = Result(shop='Snapdeal', search_item=it, **results[i])
            db.session.add(result_db)

        db.session.commit()

        it.results.delete()
        it.query.delete()
        db.session.commit()
