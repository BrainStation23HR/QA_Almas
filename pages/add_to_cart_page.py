import ast
import time, re
from playwright.sync_api import Page, expect, sync_playwright, Playwright


class AddToCartPage:
    def __init__(self, page):
        self.page = page

    def add_product_to_cart(self):

        self.page.locator("xpath=(//div[@data-qa-locator='product-item'])[1]").click()
        if self.page.locator("xpath=//div[@class='content-block sfo']").is_visible():
            self.page.locator("xpath=//i[@class='next-icon next-icon-close next-icon-small']").click()
            self.page.get_by_role("button", name="Add to Cart").click()
            self.page.locator("xpath=//i[@class='next-icon next-icon-close next-icon-small']").click()
            self.page.locator("xpath=//span[@class='cart-icon-daraz']").click()
        else:
            self.page.get_by_role("button", name="Add to Cart").click()
            self.page.locator("xpath=//i[@class='next-icon next-icon-close next-icon-small']").click()
            self.page.locator("xpath=//span[@class='cart-icon-daraz']").click()

    def verify_added_product(self, text):
        expect(self.page.locator("//a[@class='automation-link-from-title-to-prod title']").filter(has_text=re.compile(text)))


