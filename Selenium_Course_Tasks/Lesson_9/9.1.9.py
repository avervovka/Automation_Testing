import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    actions = ActionChains(browser)
    url = 'https://parsinger.ru/draganddrop/2/index.html'
    browser.get(url)
    wait = WebDriverWait(browser, 10)

    red_square = browser.find_element(By.ID, 'draggable')
    squares_gray = browser.find_elements(By.CLASS_NAME, 'box')

    for square in squares_gray:
        if square.text == '1':
            actions.drag_and_drop_by_offset(red_square, xoffset=533, yoffset=18).perform()
        elif square.text == '2':
            actions.drag_and_drop_by_offset(red_square, xoffset=110, yoffset=10).perform()
        elif square.text == '3':
            actions.drag_and_drop_by_offset(red_square, xoffset=-90, yoffset=110).perform()
        else:
            actions.drag_and_drop_by_offset(red_square, xoffset=110, yoffset=10).perform()

    text = browser.find_element(By.ID, 'message').text
    wait.until(lambda x: text != '')
    print(text)
