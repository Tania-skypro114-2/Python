from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():

    driver = webdriver.Firefox()
    waiter = WebDriverWait(driver, 20)
    driver.get('https://www.saucedemo.com/')

    driver.find_element(By.NAME, 'user-name').send_keys('standard_user')
    driver.find_element(By.NAME, 'password').send_keys('secret_sauce')
    driver.find_element(By.NAME, 'login-button').click()

    waiter.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[name="add-to-cart-sauce-labs-onesie"]')))

    fields = ['button[name="add-to-cart-sauce-labs-backpack"]',
              'button[name="add-to-cart-sauce-labs-bolt-t-shirt"]',
              'button[name="add-to-cart-sauce-labs-onesie"]']
    for locator in fields:
        field = driver.find_element(By.CSS_SELECTOR, locator)
        field.click()
    driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    driver.find_element(By.ID, 'checkout').click()

    driver.find_element(By.ID, 'first-name').send_keys('Tatiana')
    driver.find_element(By.ID, 'last-name').send_keys('Ivanovich')
    driver.find_element(By.ID, 'postal-code').send_keys('123456')
    driver.find_element(By.ID, 'continue').click()

    waiter.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label')))
    total = driver.find_element(By.CLASS_NAME, 'summary_total_label').text
    assert total == 'Total: $58.29'

    driver.quit()
