import ast
import sys
from playwright.sync_api import Page

import pytest
from loguru import logger

from pages.login_page import LoginPage
from utils.datareader import Data


class TestLoginWithValidCredentials:
    td = Data()
    testdata = td.data()
    acc_name = testdata['DARAZ-DATA']['verify_acc_name']

    @pytest.mark.order(1)
    @logger.catch(onerror=lambda _: sys.exit(1))
    def test_login(self, new_page, config) -> None:
        login = LoginPage(new_page, config)

        login.navigate_to_daraz_website()
        login.daraz_login()
        login.verify_login(acc_name=self.acc_name)

