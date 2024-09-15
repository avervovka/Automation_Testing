import math
import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('https://suninjuly.github.io/redirect_accept.html')
    time.sleep(2)

    browser.find_element(By.TAG_NAME, 'button').click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    count = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(count))
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(3)

    alert2 = browser.switch_to.alert
    print(alert2.text.split(': ')[-1])
    time.sleep(2)
