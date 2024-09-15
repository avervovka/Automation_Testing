import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.9/4/index.html'
    browser.get(url)

    banner_close = browser.find_element(By.CSS_SELECTOR, '.close')
    banner_close.click()

    wait = WebDriverWait(browser, 300)

    banner = wait.until(EC.invisibility_of_element_located((By.ID, 'ad')))
    if banner:
        browser.find_element(By.CSS_SELECTOR, 'button').click()
        print(browser.find_element(By.ID, 'message').text)



