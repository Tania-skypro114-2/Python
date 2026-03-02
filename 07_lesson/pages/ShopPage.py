from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_cart(self):
        self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 'button[name="add-to-cart-sauce-labs-onesie"]')))

        fields = ['button[name="add-to-cart-sauce-labs-backpack"]',
                  'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]',
                  'button[name="add-to-cart-sauce-labs-onesie"]']
        for locator in fields:
            field = self.driver.find_element(By.CSS_SELECTOR, locator)
            field.click()
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
