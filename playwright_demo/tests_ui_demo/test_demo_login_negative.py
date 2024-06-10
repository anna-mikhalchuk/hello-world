from playwright.sync_api import Playwright, sync_playwright, expect
from pom.login_page import LoginPage
from pom.home_page import HomePage


def test_login_negative(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.username.click()
    login_page.username.fill("standard_user")

    login_page.password.click()
    login_page.password.fill("wrong_password")
    login_page.login_button.click()

    home_page = HomePage(page)

    # Check for an exact match of the error message ???
    error_message = "Epic sadface: Username and password do not match any user in this service"
    expect(login_page.login_alert).to_have_text(error_message)
    # print("Proper error message appears.")

    # Check that the shopping cart icon is not visible
    expect(home_page.shopping_cart_link).to_be_hidden()
    # print("The user was not logged in. Shopping cart icon did not appear.")

    # Clean up
    context.close()
    browser.close()
