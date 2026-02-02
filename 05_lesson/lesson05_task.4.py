from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

search_username = driver.find_element(By.CSS_SELECTOR, "#username")
search_password = driver.find_element(By.CSS_SELECTOR, "#password")
search_username.send_keys("tomsmith")
search_password.send_keys("SuperSecretPassword!")


driver.find_element(By.CLASS_NAME, "radius").click()


text = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(text)


driver.quit()
