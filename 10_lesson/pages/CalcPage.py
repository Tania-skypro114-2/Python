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

    @allure.step("Установка задержки {delay} секунд")
    def delay(self, delay):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        :param delay: int — время задержки в секундах.
        """
        dl = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        dl.clear()
        dl.send_keys(delay)

    @allure.step("Нажатие кнопки '{value}'")
    def click_button(self, value):
        """Нажимает на кнопки калькулятора.
        :param value: str — текст на кнопке, которую нужно нажать.
        """
        self.driver.find_element(By.XPATH, f'//span[text()="{value}"]').click()

    @allure.step("Ожидание результата '{expected_result}'")
    def wait_for_result(self, expected_result, delay):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.
        :param expected_result: str — ожидаемый результат.
        :param delay: int — время задержки в секундах.
        """
        WebDriverWait(self.driver, delay).until(
            EC.text_to_be_present_in_element((
                By.CLASS_NAME, "screen"), expected_result)
        )

    @allure.step("Получение результата с экрана калькулятора")
    def get_result(self):
        """
        Возвращает текущий результат с экрана калькулятора.
        :return: str — текст результата на экране калькулятора.
        """
        return self.driver.find_element(By.CLASS_NAME, "screen").text
