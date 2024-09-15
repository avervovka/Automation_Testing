import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/1/index.html')
    buttons = browser.find_elements(By.XPATH, "//input[@class='buttons']")
    button_counter = 1
    for button in buttons:
        button.click()
        alert = browser.switch_to.alert
        alert.accept()
        text = browser.find_element(By.ID, 'result').text
        if text:
            print(text)
            break
