import sys

import pytest
from loguru import logger

from pages.add_to_cart_page import AddToCartPage
from pages.checkout_page import CheckoutPage
from pages.search_page import SearchPage
from utils.datareader import Data


class TestCheckOut:
    td = Data()
    testdata = td.data()
    text = testdata['DARAZ-DATA']['verify_product']

    @pytest.mark.order(5)
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_checkout(self, new_page, config) -> None:
        checkout = CheckoutPage(new_page)
        checkout.checkout()
        checkout.verify_checkout_details(self.text)

