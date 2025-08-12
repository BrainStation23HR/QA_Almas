import sys
import pytest
from loguru import logger

from pages.search_page import SearchPage
from utils.datareader import Data


class TestSearchForAProduct:
    td = Data()
    testdata = td.data()
    product_name = testdata['DARAZ-DATA']['product_name']

    @pytest.mark.order(2)
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_product_search(self, new_page, config) -> None:
        search = SearchPage(new_page)
        search.search_product(self.product_name)
        search.verify_searched_result(self.product_name)

