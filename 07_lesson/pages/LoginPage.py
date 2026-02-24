from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get('https://www.saucedemo.com/')

    def login(self):
        self.driver.find_element(
            By.NAME, 'user-name').send_keys('standard_user')
        self.driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.NAME, 'login-button').click()
