from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/'
            'slow-calculator.html'
        )

    def delay(self, value):
        dl = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        dl.clear()
        dl.send_keys(value)

    def click_button(self, value):
        self.driver.find_element(By.XPATH, f'//span[text()="{value}"]').click()

    def result(self, expected_result):
        waiter = WebDriverWait(self.driver, 45)
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), expected_result))
        result = self.driver.find_element(By.CSS_SELECTOR, '.screen').text
        return result
