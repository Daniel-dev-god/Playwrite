from playwright.sync_api import Page
from playwright.sync_api import sync_playwright


class Login:

    def __init__(self, page):
        self.page = page

    def sign_in(self):
        self.page.goto("https://www.saucedemo.com/")
        self.page.locator("[data-test=\"username\"]").click()
        self.page.locator("[data-test=\"username\"]").fill("standard_user")
        self.page.locator("[data-test=\"password\"]").click()
        self.page.locator("[data-test=\"password\"]").fill("secret_sauce")
        self.page.locator("[data-test=\"login-button\"]").click()


def test_checkout_items(page):
    page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]").click()
    page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]").click()
    page.locator("a").filter(has_text="5").click()
    page.locator("[data-test=\"remove-sauce-labs-onesie\"]").click()
    page.locator("[data-test=\"checkout\"]").click()
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("steven")
    page.locator("[data-test=\"firstName\"]").press("Tab")
    page.locator("[data-test=\"lastName\"]").fill("willlow")
    page.locator("[data-test=\"lastName\"]").press("Tab")
    page.locator("[data-test=\"postalCode\"]").fill("77988")
    page.locator("[data-test=\"continue\"]").click()
    page.get_by_text("Total: $77.72").click()
    page.locator("[data-test=\"finish\"]").click()
    page.locator("[data-test=\"back-to-products\"]").click()


class ShoppingCartTest:
    def __init__(self, page):
        self.page = page

    def login(self, username: str, password: str):
        self.page.goto(url="https://www.saucedemo.com/")
        self.page.locator("[data-test=\"username\"]").click()
        self.page.locator("[data-test=\"username\"]").fill(username)
        self.page.locator("[data-test=\"password\"]").click()
        self.page.locator("[data-test=\"password\"]").fill(password)
        self.page.locator("[data-test=\"login-button\"]").click()

    def add_all_items_to_cart(self):
        # adds ALL items available in shop to cart
        items_to_add = [
            "[data-test=\"add-to-cart-sauce-labs-backpack\"]",
            "[data-test=\"add-to-cart-sauce-labs-bike-light\"]",
            "[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]",
            "[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]",
            "[data-test=\"add-to-cart-sauce-labs-onesie\"]",
            "[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]",
        ]

        for item in items_to_add:
            self.page.locator(item).click()

    def remove_all_items_to_cart(self):
        # removes ALL items available in shop to cart
        items_to_add = [
            "[data-test=\"remove-sauce-labs-backpack\"]",
            "[data-test=\"remove-sauce-labs-bike-light\"]",
            "[data-test=\"remove-sauce-labs-bolt-t-shirt\"]",
            "[data-test=\"remove-sauce-labs-fleece-jacket\"]",
            "[data-test=\"remove-sauce-labs-onesie\"]",
            "[data-test=\"remove-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]",
        ]

        for item in items_to_add:
            self.page.locator(item).click()

    def checkout(self):
        self.page.locator("a").filter(has_text="6").click()
        self.page.locator("[data-test=\"checkout\"]").click()

    def fill_shipping_info(self, firstname, lastname, postalcode: int):
        self.page.locator("[data-test=\"firstName\"]").click()
        self.page.locator("[data-test=\"firstName\"]").fill(firstname)
        self.page.locator("[data-test=\"firstName\"]").press("Tab")
        self.page.locator("[data-test=\"lastName\"]").fill(lastname)
        self.page.locator("[data-test=\"lastName\"]").press("Tab")
        self.page.locator("[data-test=\"postalCode\"]").fill(postalcode)

    def finalize_order(self, complete_order: bool):
        if complete_order:
            self.page.locator("[data-test=\"finish\"]").click()
        else:
            self.page.locator("[data-test=\"cancel\"]").click()

    def navigate_back_to_products(self):
        self.page.locator("[data-test=\"back-to-products\"]").click()

    def test_run_test(self):
        self.login("standard_user", "secret_sauce")
        self.add_all_items_to_cart()
        self.remove_all_items_to_cart()
        self.add_all_items_to_cart()
        self.checkout()
        self.fill_shipping_info("Steven", "Smith", 77653)
        self.finalize_order(True)
        self.navigate_back_to_products()


with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    test = ShoppingCartTest(page)
    test.test_run_test()

    browser.close()
