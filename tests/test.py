import pytest
from pylint import epylint as lint
from framework.driver import driver
from sites.amazon.home import Amazon
from sites.snapdeal.home import Snapdeal


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


@pytest.mark.usefixtures('price_fixture')
class TestPrice(object):
    def test_search_basic(self):
        item = 'Redmi 5'
        shop = Amazon
        shop.navigate()
        results = shop.search_results(item)
        len_results = len(shop.results_page.results)
        assert len(results) == len_results
        for result in results:
            for sub in shop.results_page.results.sub_elements.keys():
                assert result.get(sub) is not None
