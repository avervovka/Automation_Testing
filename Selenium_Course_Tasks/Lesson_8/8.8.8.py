import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.9/6/index.html'
    browser.get(url)
    wait = WebDriverWait(browser, 300)
    locator = (By.ID, 'myCheckbox')
    checkbox = wait.until(EC.element_located_to_be_selected(locator))
    if checkbox:
        browser.find_element(By.CSS_SELECTOR, 'button').click()
    print(browser.find_element(By.ID, 'result').text)
