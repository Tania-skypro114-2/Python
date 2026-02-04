from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")

search_box = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
search_box.send_keys("Sky")
search_box.clear()
search_box.send_keys("Pro")


driver.quit()
