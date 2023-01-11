# Selenium Tutorial 1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path of chromedriver in local machine
PATH = '/user/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)
# you can go and check a website
driver.get("https://techwithtim.net")
print(driver.title)
# Finds "s" based on name
search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = main.find_elements(By.TAG_NAME, "article")
    for article in articles:
        header = article.find_element(By.CLASS_NAME, "entry-summary")
        print(header.text)
finally:
    driver.quit()
# One way to find - main = driver.find_element("id", "main")
