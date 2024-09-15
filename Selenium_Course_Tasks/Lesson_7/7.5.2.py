import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    buttons = browser.find_elements(By.XPATH, "//input[@class='buttons']")
    button_counter = 1
    for button in buttons:
        button.click()
        alert = browser.switch_to.alert
        text = alert.text
        alert.accept()
        browser_input = browser.find_element(By.XPATH, "//input[@id='input']")
        browser_input.send_keys(text)
        checker = browser.find_element(By.XPATH, '//input[@id="check"]')
        checker.click()
        result = browser.find_element(By.ID, 'result')
        if result.text == 'Неверный пин-код':
            continue
        else:
            print(result.text)
            break
