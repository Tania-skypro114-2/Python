from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():

    driver = webdriver.Chrome()

    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    dl = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
    dl.clear()
    dl.send_keys('45')
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()
    driver.find_element(By.XPATH, '//span[text()="="]').click()

    waiter = WebDriverWait(driver, 45)
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), '15'))
    summa = driver.find_element(By.CSS_SELECTOR, '.screen').text
    assert summa == '15'

    driver.quit()
