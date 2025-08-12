import sys

import pytest
from loguru import logger

from pages.add_to_cart_page import AddToCartPage
from pages.search_page import SearchPage
from utils.datareader import Data


class TestAddItemToCart:
    td = Data()
    testdata = td.data()
    product_name = testdata['DARAZ-DATA']['another_product_name']
    text = testdata['DARAZ-DATA']['another_product_text']

    @pytest.mark.order(4)
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_add_item_to_cart(self, new_page, config) -> None:
        search = SearchPage(new_page)
        search.search_product(self.product_name)
        add_to_cart = AddToCartPage(new_page)
        add_to_cart.add_product_to_cart()
        add_to_cart.verify_added_product(self.text)

