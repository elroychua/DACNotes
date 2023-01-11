# DACNotes

## Notes for utilising technologies tailored to the requirements of clinical trial clients

### Tutorial 1

Selenium
To install selenium

- navigate to folder
- pip3 install
- pipenv shell
- pipenv shell selenium

Actions:

```Python
# Path of chromedriver in local machine
PATH = '/user/local/bin/chromedriver'
driver = webdriver.Chrome(PATH)
# you can go and check a website
driver.get("https://techwithtim.net/")
# closes current tab
driver.close()
# closes the entire browser
driver.quit()
```

### Tutorial 2

Ways to access:

1. id
2. name
3. class
4. tag

Returns first element on a page, class may not be unique.

```Python
#One way to find - main = driver.find_element("id", "main")
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
```

### Tutorial 3

- element.clear() - Clears info inside of a search field

```Python
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

```

### Tutorial 4

#### Action chain

```Python
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

```
