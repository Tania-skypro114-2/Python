import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.ShopPage import ShopPage
from pages.CartPage import CartPage
from pages.AddressPage import AddressPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.title("Тестирование онлайн-магазина")
@allure.description("Проверка корректности работы онлайн-магазина")
@allure.feature("Онлайн-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_page(driver):
    """Тест проверяет работу онлайн-магазина"""
    login_page = LoginPage(driver)
    with allure.step("Открытие страницы магазина"):
        login_page.open()
    with allure.step("Авторизация"):
        login_page.login()
    shop_page = ShopPage(driver)
    with allure.step("Добавление товаров в корзину"):
        shop_page.add_cart()
    cart_page = CartPage(driver)
    with allure.step("Проверка содержимого корзины"):
        cart_items = cart_page.get_cart_items()
        expected_items = [
            {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
            {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
            {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
         ]
        assert cart_items == expected_items, \
            "Items in cart do not match expected items"
        cart_page.checkout()
    with allure.step("Заполнение адресата"):
        address_page = AddressPage(driver)
        address_page.address_form()
        address_page.continue_click()
    with allure.step("Проверка итоговой стоимости заказа"):
        total_summary = address_page.total_summary()
        assert total_summary == 'Total: $58.29'
