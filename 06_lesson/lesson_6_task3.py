from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 20)


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


waiter.until(EC.presence_of_all_elements_located(
    (By.CSS_SELECTOR, "#landscape")))


art = driver.find_elements(By.CSS_SELECTOR, 'img')

print(art[3].get_attribute('src'))


driver.quit()
