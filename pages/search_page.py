import ast
import time, re
from playwright.sync_api import Page, expect, sync_playwright, Playwright


class SearchPage:
    def __init__(self, page):
        self.page = page

    def search_product(self, product_name):
        self.page.get_by_role("searchbox", name="Search in Daraz").click()
        self.page.get_by_role("searchbox", name="Search in Daraz").fill(product_name)
        self.page.get_by_role("link", name="SEARCH").click()

    # def product_selection(self, product_name):
    #     self.page.get_by_role("link", name=product_name).first.click()

    def verify_searched_result(self, product_name):
        expect(self.page.locator("h1")).to_contain_text(product_name)
        expect(self.page.locator("#root")).to_contain_text(product_name)


