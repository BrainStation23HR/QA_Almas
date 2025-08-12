import ast
import time, re
from playwright.sync_api import Page, expect, sync_playwright, Playwright


class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.locator("xpath=(//input[@type='checkbox'])[1]").check()
        self.page.locator("xpath=//button[contains(text(), 'PROCEED TO CHECKOUT')]").click()

    def verify_checkout_details(self, text):
        expect(self.page.locator("//a[@class='automation-link-from-title-to-prod title']").filter(has_text=re.compile(text)))


