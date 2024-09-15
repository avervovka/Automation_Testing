import math
import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/get_attribute.html')
    a = browser.find_element(By.TAG_NAME, 'img').get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calc(a))
    time.sleep(1)

    browser.find_element(By.ID, 'robotCheckbox').click()
    time.sleep(1)

    browser.find_element(By.ID, 'robotsRule').click()
    time.sleep(1)

    browser.find_element(By.XPATH, "//button[text()='Submit']").click()
    time.sleep(30)
