import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException

chrome_options = Options()

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/selenium/5.8/5/index.html')
    for i in range(1, 10):
        iframe = browser.find_element(By.ID, f"iframe{i}")
        browser.switch_to.frame(iframe)
        browser.find_element(By.TAG_NAME, 'button').click()
        count = browser.find_element(By.ID, 'numberDisplay').text
        browser.switch_to.default_content()
        time.sleep(0.5)
        pole = browser.find_element(By.ID, 'guessInput')
        pole.send_keys(count)
        time.sleep(0.5)
        browser.find_element(By.ID, 'checkBtn').click()
        try:
            print(browser.switch_to.alert.text)
        except NoAlertPresentException:
            pole.clear()

