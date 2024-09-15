from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/expectations/3/index.html'
    browser.get(url)
    button_locator = (By.ID, 'btn')

    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(button_locator))
    button.click()

    title = WebDriverWait(browser, 20).until(EC.title_is('345FDG3245SFD'))
    if title:
        print(browser.find_element(By.ID, 'result').text)
