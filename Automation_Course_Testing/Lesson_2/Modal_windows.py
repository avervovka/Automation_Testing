import math
import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/alert_accept.html')
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)

    alert = browser.switch_to.alert
    alert.accept()

    count = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(count))

    browser.find_element(By.TAG_NAME, 'button').click()
    alert2 = browser.switch_to.alert
    print(alert2.text.split(': ')[-1])
    time.sleep(2)

