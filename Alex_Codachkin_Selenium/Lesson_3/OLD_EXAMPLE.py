import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_1/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
    spans = browser.find_elements(By.TAG_NAME, 'span')
    count = [int(i.text) for i in spans if i.text.isdigit()]
    print(sum(count))