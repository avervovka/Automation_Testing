import math
import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://omayo.blogspot.com/'
    browser.get(url)
    wait = WebDriverWait(browser, 300)

    text_locator = (By.ID, 'delayedText')
    wait.until(EC.visibility_of_element_located(text_locator))
    print('OK')

    Button3_locator = (By.ID, 'timerButton')
    wait.until(EC.element_to_be_clickable(Button3_locator))
    print('OK')

    tryit_button_locator = (By.XPATH, "//button[contains(text(), 'Try')]")
    browser.find_element(*tryit_button_locator).click()
    print('OK')

    button3 = EC.element_to_be_clickable(Button3_locator)
    wait.until(lambda x: button3 is not True)
