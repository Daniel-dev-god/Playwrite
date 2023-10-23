from main import ShoppingCartTest
from Login import Login

shopping_item = ShoppingCartTest()
Login_test = Login()


def test_run_test():
    Login_test.login("standard_user", "secret_sauce")
    shopping_item.add_all_items_to_cart()
    shopping_item.remove_all_items_to_cart()
    shopping_item.add_all_items_to_cart()
    shopping_item.checkout()
    shopping_item.fill_shipping_info("Steven", "Smith", 77653)
    shopping_item.finalize_order(True)
    shopping_item.navigate_back_to_products()