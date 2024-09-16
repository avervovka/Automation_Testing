import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.10/6/index.html'
    browser.get(url)
    action = ActionChains(browser)
    wait = WebDriverWait(browser, 300)

    slider = browser.find_elements(By.CLASS_NAME, 'volume-slider')

    target_values = [int(i.text) for i in browser.find_elements(By.CLASS_NAME, 'target-value')]
    current_values = [int(i.text) for i in browser.find_elements(By.CLASS_NAME, 'current-value')]
    sum_values = []
    for i in range(10):
        sum_values.append(target_values[i] - current_values[i])

    for i in range(10):
        width = slider[i].size['width']
        offset = width / 100
        if sum_values[i] < 0:
            for _ in range(abs(sum_values[i])):
                slider[i].send_keys(Keys.ARROW_LEFT)
                time.sleep(0.01)

        else:
            for _ in range(abs(sum_values[i])):
                slider[i].send_keys(Keys.ARROW_RIGHT)
                time.sleep(0.01)

    print(browser.find_element(By.ID, 'message').text)
