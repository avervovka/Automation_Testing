from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://parsinger.ru/selenium/5.7/4/index.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    # time.sleep(10)
    actions = ActionChains(browser)
    container = browser.find_element(By.XPATH, "//*[@id='main_container']")

    while True:
        actions.move_to_element(container).scroll_by_amount(0, 200).perform()
