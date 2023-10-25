from main import ShoppingCartTest
from Login import Login


def test_add_to_cart(page, playwright):
    shopping_item = ShoppingCartTest(page, playwright)
    login_test = Login(page)

    page.goto("https://www.saucedemo.com/")
    login_test.login("standard_user", "secret_sauce")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    shopping_item.add_all_items_to_cart()
    assert page.locator("[data-test=\"product_sort_container\"]").exists()
    assert page.locator("[data-test=\"inventory_item\"]").count == 6
    shopping_item.remove_all_items_to_cart()
    shopping_item.add_all_items_to_cart()
    assert page.locator("[data-test=\"product_sort_container\"]").exists()
    assert page.locator("[data-test=\"inventory_item\"]").count == 6
    shopping_item.checkout()
    shopping_item.fill_shipping_info("Steven", "Smith", "77653")
    shopping_item.finalize_order()
    shopping_item.navigate_back_to_products()
    assert page.url == "https://www.saucedemo.com/inventory.html"


def test_fail_login(page, playwright):
    page.goto("https://www.saucedemo.com/")
    login = Login(page, playwright)
    login.login("wrong_user", "password123")
    assert page.get_by_test_id("error")
