from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import allure


class LoginPage:
    def __init__(self, driver):
        """
        Конструктор класса LoginPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы магазина")
    def open(self):
        """
        Открывает страницу магазина.
        """
        self.driver.get('https://www.saucedemo.com/')

    @allure.step("Авторизация")
    def login(self):
        """
        Заполняет поля формы авторизации.
        Нажимает на кнопку входа.
        """
        self.driver.find_element(
            By.NAME, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.NAME, 'login-button').click()
