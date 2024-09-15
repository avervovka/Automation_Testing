import math
import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


def func(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('https://SunInJuly.github.io/execute_script.html')
    time.sleep(1)

    input_value = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(func(input_value))
    time.sleep(1)

    browser.find_element(By.ID, 'robotCheckbox').click()

    button = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(30)
