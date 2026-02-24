import pytest
from selenium import webdriver
from pages.FormaPage import FormaPage


@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_forma(driver):
    forma_page = FormaPage(driver)
    forma_page.open()
    forma_page.fill_form()
    forma_page.submit()
    forma_page.check_form_submission()
