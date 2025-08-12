import ast
import time, re
from playwright.sync_api import Page, expect, sync_playwright, Playwright


class LoginPage:
    def __init__(self, page, config):
        self.page = page
        self.url = config['DARAZ-CONFIG']['base_url']
        self.login_data = ast.literal_eval(config['DARAZ-CONFIG']['login_credentials'])

    def navigate_to_daraz_website(self):
        self.page.goto(self.url)

    def daraz_login(self):
        self.page.get_by_role("link", name="Login").click()
        self.page.get_by_role("textbox", name="Please enter your Phone or").click()
        self.page.get_by_role("textbox", name="Please enter your Phone or").fill(self.login_data['mobile_number'])
        self.page.get_by_role("textbox", name="Please enter your password").click()
        self.page.get_by_role("textbox", name="Please enter your password").fill(self.login_data['password'])
        self.page.get_by_role("button", name="LOGIN").click()

    def verify_login(self, acc_name):
        expect(self.page.locator("#myAccountTrigger")).to_contain_text(acc_name)


