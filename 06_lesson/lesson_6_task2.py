from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
waiter = WebDriverWait(driver, 10)


driver.get("http://uitestingplayground.com/textinput")


search_box = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_box.send_keys("SkyPro")


driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()


waiter.until(EC.text_to_be_present_in_element(
    (By.ID, "updatingButton"), "SkyPro"))
green = driver.find_element(By.CSS_SELECTOR, ".btn-primary").text


print(green)


driver.quit()
