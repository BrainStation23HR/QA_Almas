import ast
import time, re
from playwright.sync_api import Page, expect, sync_playwright, Playwright


class LogoutPage:
    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.locator("xpath=//span[@id='myAccountTrigger']").click()
        self.page.get_by_role("link", name="Logout").click()

    def verify_logout(self, text):
        expect(self.page.locator("#container")).to_contain_text(text)


