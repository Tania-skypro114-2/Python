from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

crt = "img"
waiter = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, crt)))
cart = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "#landscape")))

art = driver.find_elements(By.CSS_SELECTOR, crt)

print(art[3].get_attribute('src'))

driver.quit()
