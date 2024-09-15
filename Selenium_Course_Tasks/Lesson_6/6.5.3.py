import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException as NS


with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/infiniti_scroll_2/'
    browser.get(url)
    actions = ActionChains(browser)
    scroll_containter = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    scroll_containter2 = browser.find_element(By.XPATH, "//*[@id='scroll-container']")
    a = []

    while True:
        actions.move_to_element(scroll_containter).scroll_by_amount(0, 100).perform()
        try:
            print(scroll_containter2.find_element(By.CLASS_NAME, 'last-of-list').text)
            break
        except NS:
            continue

    elements = scroll_containter2.find_elements(By.XPATH, "//p[contains(@id, 'Infi')]")
    for element in elements:
        if element.text.isdigit():
            a.append(int(element.text))
    print(sum(a))
