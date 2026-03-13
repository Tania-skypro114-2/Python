from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AddressPage:
    def __init__(self, driver):
        """
        Конструктор класса AddressPage.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'first-name': 'Tatiana',
            'last-name': 'Ivanovich',
            'postal-code': '123456'
        }

    @allure.step("Заполнение адреса")
    def address_form(self):
        for field, value in self.fields.items():
            self.wait.until(EC.visibility_of_element_located(
                (By.ID, field))).send_keys(value)

    @allure.step("Нажатие кнопки 'продолжить'")
    def continue_click(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#continue'))).click()

    @allure.step("Проверка итоговой стоимости заказа")
    def total_summary(self):
        """
        Возвращает итоговую стоимость заказа.
        :return: str.
        """
        self.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, 'summary_total_label')))
        total = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text
        return total
