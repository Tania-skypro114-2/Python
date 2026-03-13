from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:
    def __init__(self, driver):
        """Конструктор класса CalcPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы калькулярора")
    def open(self):
        """Открывает страницу калькулятора"""
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/'
            'slow-calculator.html'
        )

    @allure.step("Установка задержки {value} секунд")
    def delay(self, value):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param value: int — время задержки в секундах.
        """
        dl = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        dl.clear()
        dl.send_keys(value)

    @allure.step("Нажатие кнопки '{value}'")
    def click_button(self, value):
        """Нажимает на кнопки калькулятора.
        :param value: str — текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, f'//span[text()="{value}"]').click()

    @allure.step("Получение результата '{expected_result}'")
    def result(self, expected_result):
        """Ожидает появления ожидаемого результата на экране калькулярора.
        Возвращает текущий результат с экрана калькулятора.
        :param expected_result: str — ожидаемый результат.
        :return: str — текст результата на экране калькулятора.
        """
        waiter = WebDriverWait(self.driver, 45)
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), expected_result))
        result = self.driver.find_element(By.CSS_SELECTOR, '.screen').text
        return result
