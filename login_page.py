from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_name = page.get_by_placeholder("Username")
        self.password_keys = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")

    def open_website(self):
        self.page.goto("https://www.saucedemo.com/")

    def do_login(self, user:str, keyword:str):
        self.user_name.fill(user)
        self.password_keys.fill(keyword)
        self.login_button.click()


        

        