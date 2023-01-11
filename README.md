# DACNotes

## Notes for utilising technologies tailored to the requirements of clinical trial clients

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
