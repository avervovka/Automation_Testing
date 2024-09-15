from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    #1
    url = 'https://parsinger.ru/expectations/4/index.html'
    browser.get(url)

    #2
    wait = WebDriverWait(browser, timeout=20, poll_frequency=0.1)
    button_locator = (By.ID, 'btn')

    #3
    button = wait.until(EC.element_to_be_clickable(button_locator))
    button.click()

    #4
    title = wait.until(EC.title_contains('JK8HQ'))

    #5
    if title:
        print(browser.title)
