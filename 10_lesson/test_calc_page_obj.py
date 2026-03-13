import pytest
from selenium import webdriver
from pages.CalcPage import CalcPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Проверка корректности работы калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calc(driver):
    """
    Тест проверяет работу калькулятора с различными операциями.
    """
    calc_page = CalcPage(driver)
    with allure.step("Открытие страницы калькулятора"):
        calc_page.open()
    with allure.step("Установка задержки"):
        calc_page.delay("45")
    with allure.step("Нажатие кнопок"):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")
    with allure.step("Проверка результата"):
        assert calc_page.result("15")
