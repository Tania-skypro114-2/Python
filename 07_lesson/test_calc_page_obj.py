import pytest
from selenium import webdriver
from pages.CalcPage import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_calc(driver):
    calc_page = CalcPage(driver)
    calc_page.open()
    calc_page.delay("45")
    calc_page.click()
    summa = calc_page.result()
    assert summa == "15"
