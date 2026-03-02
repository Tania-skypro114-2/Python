from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddressPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'first-name': 'Tatiana',
            'last-name': 'Ivanovich',
            'postal-code': '123456'
        }

    def address_form(self):
        for field, value in self.fields.items():
            self.wait.until(EC.visibility_of_element_located(
                (By.ID, field))).send_keys(value)

    def continue_click(self):
        self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '#continue'))).click()

    def total_summary(self):
        self.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, 'summary_total_label')))
        total = self.driver.find_element(
            By.CLASS_NAME, 'summary_total_label').text
        return total
