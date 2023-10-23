# from playwright.sync_api import Page
# from playwright.sync_api import sync_playwright


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
        self.backpack_add = self.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.bike_light_add = self.page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        self.fleece_jacket_add = self.page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        self.bolt_tshirt_add = self.page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        self.onesie_add = self.page.locator("[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        self.red_tshirt_add = self.page.locator(
            "[data-test=\"add-to-cart-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]")
        self.backpack_remove = self.page.locator("[data-test=\"remove-sauce-labs-backpack\"]")
        self.bike_light_remove = self.page.locator("[data-test=\"remove-sauce-labs-bike-light\"]")
        self.fleece_jacket_remove = self.page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]")
        self.bolt_tshirt_remove = self.page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]")
        self.onesie_remove = self.page.locator("[data-test=\"remove-sauce-labs-onesie\"]")
        self.red_tshirt_remove = self.page.locator("[data-test=\"remove-test\\.allthethings\\(\\)-t-shirt-\\(red\\)\"]")
        self.shopping_cart = self.page.locator("a").filter(has_text="6")
        self.checkout_button = self.page.locator("[data-test=\"checkout\"]")
        self.shipping_name = self.page.locator("[data-test=\"firstName\"]")
        self.shipping_lastname = self.page.locator("[data-test=\"lastName\"]")
        self.shipping_postcode = self.page.locator("[data-test=\"postalCode\"]")
        self.confirm_order = self.page.locator("[data-test=\"finish\"]")
        self.cancel_order = self.page.locator("[data-test=\"cancel\"]")
        self.back_home = self.page.locator("[data-test=\"back-to-products\"]")

    def add_all_items_to_cart(self):
        # adds ALL items available in shop to cart
        self.backpack_add().click()
        self.bike_light_add.click()
        self.fleece_jacket_add.click()
        self.bolt_tshirt_add.click()
        self.onesie_add.click()
        self.red_tshirt_add.click()

    def remove_all_items_to_cart(self):
        # removes ALL items available in shop to cart
        self.backpack_remove().click()
        self.bike_light_remove.click()
        self.fleece_jacket_remove.click()
        self.bolt_tshirt_remove.click()
        self.onesie_remove.click()
        self.red_tshirt_remove.click()

    def checkout(self):
        self.shopping_cart().click()
        self.checkout_button().click()

    def fill_shipping_info(self, firstname: str, lastname: str, postalcode: int):
        self.shipping_name.fill(firstname)
        self.shipping_lastname.fill(lastname)
        self.shipping_postcode.fill(postalcode)

    def finalize_order(self, complete_order: bool):
        if complete_order:
            self.confirm_order.click()
        else:
            self.cancel_order.click()

    def navigate_back_to_products(self):
        self.back_home.click()



