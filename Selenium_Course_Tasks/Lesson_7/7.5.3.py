import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


def click():
    browser.find_element(By.ID, 'check').click()


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    pin_codes = browser.find_elements(By.XPATH, "//span[@class='pin']")
    for pin in pin_codes:
        extracted_text = pin.text
        click()
        alert = browser.switch_to.alert
        alert.send_keys(extracted_text)
        alert.accept()
        result = browser.find_element(By.ID, 'result')
        if result.text == 'Неверный пин-код':
            continue
        else:
            print(result.text)
            break


