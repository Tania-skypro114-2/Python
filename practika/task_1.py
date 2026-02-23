from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

sleep(15)


print(f'Заголовок страницы: {driver.title}')

driver.quit()
