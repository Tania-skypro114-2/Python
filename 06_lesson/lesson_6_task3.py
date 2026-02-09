from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


time = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#landscape')))


art = driver.find_element(By.ID, 'award')
print(art.get_attribute('src'))


driver.quit()
