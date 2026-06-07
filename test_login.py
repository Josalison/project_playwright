from playwright.sync_api import Page
from login_page import LoginPage

def test_login_successful(page: Page):
    login = LoginPage(page)
    login.open_website()
    login.do_login("standard_user","secret_sauce")

    assert page.url == "https://www.saucedemo.com/inventory.html"