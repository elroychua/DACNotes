# Selenium Tutorial 1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = '/user/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
# select python programming
link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    # Click on beginner python tutorials
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.LINK_TEXT, "Beginner Python Tutorials"))
    )

    element.click()
    # Accesses a href
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "sow-button-19310003"))
    )
    element.click()
    # Goes back
    driver.back()
    # Goes forward
    driver.forward()
finally:
    driver.quit()
