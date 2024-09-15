import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException as NS
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.7/1/index.html'
    browser.get(url)

    buttons = browser.find_elements(By.CLASS_NAME, 'clickMe')
    for button in buttons:
        button.click()

    alert = browser.switch_to.alert
    print(alert.text)
