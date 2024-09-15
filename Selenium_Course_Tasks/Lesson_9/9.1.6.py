from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://parsinger.ru/draganddrop/1/index.html"

# Инициализация драйвера
with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    start = browser.find_element(By.ID, 'draggable')
    stop = browser.find_element(By.ID, 'field2')
    action.drag_and_drop(start, stop).perform()

    wait.until(lambda x: browser.find_element(By.ID, 'result').text != '')
    text = browser.find_element(By.ID, 'result').text
    print(text)
