import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.10/8/index.html'
    browser.get(url)
    action = ActionChains(browser)
    wait = WebDriverWait(browser, 300)

    all_colors = browser.find_elements(By.XPATH, f"//div[contains(@class, 'ui-draggable')]")

    all_lines = browser.find_elements(By.XPATH, f"//div[contains(@class, 'ui-droppable')]")
    counter = 0

    every_color = dict(zip(all_colors, all_lines))

    for color, line in every_color.items():
        action.drag_and_drop(color, line).perform()

    wait.until(lambda x: browser.find_element(By.ID, 'message').text != '')
    print(browser.find_element(By.ID, 'message').text)