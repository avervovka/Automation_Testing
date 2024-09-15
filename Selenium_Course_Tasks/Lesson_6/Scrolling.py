import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    time.sleep(0.5)
    container = browser.find_elements(By.TAG_NAME, 'span')
    for element in container:
        element.send_keys(Keys.DOWN)
