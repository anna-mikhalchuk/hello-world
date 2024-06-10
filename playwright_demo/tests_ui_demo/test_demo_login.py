from playwright.sync_api import Playwright, expect
from pom.login_page import LoginPage
from pom.home_page import HomePage

def test_check_page_is_open(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    response = page.request.get('https://www.saucedemo.com/')
    expect(response).to_be_ok()

    # Clean up
    context.close()
    browser.close()


def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(5000)
    page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(page)
    login_page.username.click()
    login_page.username.fill("standard_user")

    login_page.password.click()
    login_page.password.fill("secret_sauce")
    login_page.login_button.click()

    home_page = HomePage(page)

    # Check the login button is not displayed
    expect(login_page.login_button).to_be_hidden()
    # print("The user is successfully logged in. Login button is hidden.")

    # Check the shopping cart is now available
    expect(home_page.shopping_cart_link).to_be_visible()
    # print("The user is successfully logged in. Shopping cart icon appears.")

    # Clean up
    context.close()
    browser.close()
