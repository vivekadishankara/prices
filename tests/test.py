import pytest
from pylint import epylint as lint
from lib.driver import driver
from commons.constants import PriceConstants
from sites.amazon.home import Amazon
from sites.snapdeal.home import Snapdeal


@pytest.fixture(scope='class')
def price_fixture():
    driver.start_driver()
    yield
    driver.quit()


class TestPrice(object):
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
    def test_search_basic(self):
        item = 'Redmi 5'
        Amazon.navigate()
        results = Amazon.search_results(item)
        len_results = len(Amazon.results_page.results)
        assert len(results) == len_results
        for result in results:
            for sub in PriceConstants.PRODUCT_ATTRIBUTES:
                assert result.get(sub) is not None
