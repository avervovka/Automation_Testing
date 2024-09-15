import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/selects1.html')
    first = browser.find_element(By.XPATH, "//span[@id='num1']").text
    second = browser.find_element(By.XPATH, "//span[@id='num2']").text

    sum_all = str(int(first) + int(second))
    # list_dropdown = browser.find_elements(By.ID, "dropdown")
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum_all)
    time.sleep(1)
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(20)
