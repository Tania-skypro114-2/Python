from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()


driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
try:
    images = WebDriverWait(driver, 30).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "img"))
    )

    if len(images) == 4:
        art = driver.find_element(By.CSS_SELECTOR, "#award")
        print(art.get_attribute('src'))
    else:
        print("Не все изображения загружены.")


#cart = driver.find_elements(By.CSS_SELECTOR, '.col-12')
#print(len(cart))

#art = driver.find_element(By.CSS_SELECTOR, '#award')
#print(art.get_attribute('src'))
finally:
    driver.quit()
