from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    #1
    url = 'https://parsinger.ru/expectations/6/index.html'
    browser.get(url)

    #2
    button_locator = (By.CSS_SELECTOR, '#btn')
    wait = WebDriverWait(browser, 20)
    wait.until(EC.element_to_be_clickable(button_locator)).click()

    #3 #4
    element_locator = (By.CLASS_NAME, 'BMH21YY')
    element = wait.until(EC.presence_of_element_located(element_locator))
    if element:
        print(element.text)
