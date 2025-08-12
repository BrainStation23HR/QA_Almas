import sys

import pytest
from loguru import logger

from pages.add_to_cart_page import AddToCartPage
from pages.checkout_page import CheckoutPage
from pages.logout_page import LogoutPage
from pages.search_page import SearchPage
from utils.datareader import Data


class TestLogOut:
    td = Data()
    testdata = td.data()
    text = testdata['DARAZ-DATA']['verify_logout']

    @pytest.mark.order(6)
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_logout(self, new_page, config) -> None:
        logout = LogoutPage(new_page)
        logout.logout()
        logout.verify_logout(self.text)

