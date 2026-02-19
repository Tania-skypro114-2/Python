from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():

    driver = webdriver.Edge()
    waiter = WebDriverWait(driver, 20)

    try:
        driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

        waiter.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button[type="submit"]')))

        driver.find_element(By.NAME, 'first-name').send_keys('Иван')
        driver.find_element(By.NAME, 'last-name').send_keys('Петров')
        driver.find_element(By.NAME, 'address').send_keys('Ленина, 55-3')
        driver.find_element(By.NAME, 'e-mail').send_keys('test@skypro.com')
        driver.find_element(By.NAME, 'phone').send_keys('+7985899998787')
        driver.find_element(By.NAME, 'city').send_keys('Москва')
        driver.find_element(By.NAME, 'country').send_keys('Россия')
        driver.find_element(By.NAME, 'job-position').send_keys('QA')
        driver.find_element(By.NAME, 'company').send_keys('SkyPro')

        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        red = driver.find_element(
            By.CSS_SELECTOR, '#zip-code').get_attribute('class')
        assert red == 'alert py-2 alert-danger'

        forms = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                 'city', 'country', 'job-position', 'company']
        for form in forms:
            green = driver.find_element(
                    By.CSS_SELECTOR, f'#{form}').get_attribute('class')
            assert green == 'alert py-2 alert-success'
    finally:
        driver.quit()
