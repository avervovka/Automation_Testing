from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    #1
    url = 'https://parsinger.ru/selenium/5.9/2/index.html'
    browser.get(url)
    wait = WebDriverWait(browser, 100)

    #2
    block_locator = (By.ID, 'qQm9y1rk')

    #3 #4
    wait.until(EC.presence_of_element_located(block_locator)).click()

    #5
    alert = browser.switch_to.alert
    print(alert.text)
