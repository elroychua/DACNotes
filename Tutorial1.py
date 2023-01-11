# Selenium Tutorial 1
from selenium import webdriver
# Path of chromedriver in local machine
PATH = '/user/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)
# you can go and check a website
driver.get("https://techwithtim.net/")
# closes current tab
driver.close()
# closes the entire browser
driver.quit()
