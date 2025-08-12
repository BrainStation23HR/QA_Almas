import sys

import pytest
from loguru import logger

from pages.add_to_cart_page import AddToCartPage
from utils.datareader import Data


class TestAddItemToCart:
    td = Data()
    testdata = td.data()
    product_name = testdata['DARAZ-DATA']['product_name']
    text = testdata['DARAZ-DATA']['product_text']

    @pytest.mark.order(3)
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_add_item_to_cart(self, new_page, config) -> None:
        add_to_cart = AddToCartPage(new_page)
        add_to_cart.add_product_to_cart()
        add_to_cart.verify_added_product(self.text)

