

class LoginPage:

    def __init__(self, page):
        self.username = page.locator("[data-test=\"username\"]")
        self.password = page.locator("[data-test=\"password\"]")
        self.login_button = page.locator("[data-test=\"login-button\"]")
        self.login_alert = page.locator("[data-test=\"error\"]")
