from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'cart_item_label')))
        items = []
        cart_item_elements = self.driver.find_elements(
            By.CLASS_NAME, 'cart_item_label')
        for item in cart_item_elements:
            name = item.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price = item.find_element(
                By.CLASS_NAME, 'inventory_item_price').text
            items.append({'name': name, 'price': price})
        return items

    def checkout(self):
        self.driver.find_element(By.ID, 'checkout').click()
