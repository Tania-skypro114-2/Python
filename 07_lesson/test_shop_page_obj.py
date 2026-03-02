import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ShopPage import ShopPage
from pages.CartPage import CartPage
from pages.AddressPage import AddressPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_shop_page(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login()
    shop_page = ShopPage(driver)
    shop_page.add_cart()
    cart_page = CartPage(driver)
    cart_items = cart_page.get_cart_items()
    expected_items = [
        {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
        {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
        {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
    ]
    assert cart_items == expected_items, \
        "Items in cart do not match expected items"
    cart_page.checkout()
    address_page = AddressPage(driver)
    address_page.address_form()
    address_page.continue_click()
    total_summary = address_page.total_summary()
    assert total_summary == 'Total: $58.29'
