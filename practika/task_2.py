from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

driver.find_element(By.LINK_TEXT, "Donate").click()

sleep(15)


driver.quit()
