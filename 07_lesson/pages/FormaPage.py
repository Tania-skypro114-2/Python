from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormaPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'e-mail': "test@skypro.com",
            'phone': "7985899998787",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def open(self):
        self.driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    def fill_form(self):
        for field, value in self.fields.items():
            self.wait.until(EC.presence_of_element_located(
                (By.NAME, field))).send_keys(value)

    def submit(self):
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[type="submit"]'))).click()

    def class_element(self, field_id):
        element = self.wait.until(EC.presence_of_element_located(
            (By.ID, field_id))).get_attribute('class')
        return element

    def check_zip_code(self):
        return 'alert-danger' in self.class_element('zip-code')

    def check_fields_green(self):
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for field in fields:
            if "success" not in self.class_element(field):
                return False
        return True
