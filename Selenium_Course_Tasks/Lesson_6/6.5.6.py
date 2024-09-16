import math
import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.7/5/index.html'
    browser.get(url)

    buttons = browser.find_elements(By.CLASS_NAME, 'timer_button')
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 300)

    for button in buttons:
        actions.click_and_hold(button).perform()
        time.sleep(float(button.text))
        actions.release(button).perform()

    alert = browser.switch_to.alert
    wait.until(lambda x: alert.text != '')

    print(alert.text)
