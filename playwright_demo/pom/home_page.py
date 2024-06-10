

class HomePage:

    def __init__(self, page):
        self.shopping_cart_link = page.locator("[data-test=\"shopping-cart-link\"]")
        self.menu = page.get_by_role("button", name="Open Menu")
        self.menu_all_items = page.locator("[data-test=\"inventory-sidebar-link\"]")
        self.menu_about = page.locator("[data-test=\"about-sidebar-link\"]")
        self.menu_logout = page.locator("[data-test=\"logout-sidebar-link\"]")
        self.menu_reset_app_state = page.locator("[data-test=\"reset-sidebar-link\"]")
        self.close_menu = page.get_by_role("button", name="Close Menu")
        self.filter = page.locator("[data-test=\"product-sort-container\"]")
        self.catalog = page.locator("[data-test=\"inventory-container\"]")
        self.footer = page.locator("[data-test=\"footer\"]")
        self.footer_twitter = page.locator("[data-test=\"social-twitter\"]")
        self.footer_facebook = page.locator("[data-test=\"social-facebook\"]")
        self.footer_linkedin = page.locator("[data-test=\"social-linkedin\"]")