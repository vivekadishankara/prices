import pytest
from pylint import epylint as lint
from framework.driver import driver
from sites.shops.amazon.home import Amazon
from sites.shops.flipkart.home import Flipkart
from sites.shops.snapdeal.home import Snapdeal


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
    def test_search_basic(self):
        item = 'Redmi 5'
        item_num = 5
        fp = 'results'
        with open(fp, 'w') as f:
            with driver:
                for shop in [Amazon, Flipkart, Snapdeal]:
                    shop.navigate()
                    results = []
                    for result in shop.search_results(item, item_num):
                        f.write(str(result) + '\n')
                        results.append(result)
                        for sub in shop.results_page.results.sub_elements:
                            assert result.get(sub) is not None
                    assert len(results) == item_num
