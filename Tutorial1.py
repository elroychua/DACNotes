# Selenium Tutorial 1
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
PATH = '/user/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")
# wont pass this line until 5 sec is up.
driver.implicitly_wait(5)
language = driver.find_element(By.ID, "langSelect-EN")
cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice"+str(i))
         for i in range(1, -1, -1)]  # start at most expensive till last.

# Sets up chain of actions to run
selectLanguageAction = ActionChains(driver)
selectLanguageAction.click(language)
selectLanguageAction.perform()

driver.implicitly_wait(20)

actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.perform()
    count = cookie_count.text
    print(count)
