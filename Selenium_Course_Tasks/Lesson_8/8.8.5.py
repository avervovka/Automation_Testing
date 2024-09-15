import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

ids_to_find = ['xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB', 'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I','jolHZqD1', 'ZM6Ms3tw',
               '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR']

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.9/3/index.html'
    browser.get(url)
    wait = WebDriverWait(browser, 300)
    for i in range(len(ids_to_find)):
        locator = (By.ID, f"{ids_to_find[i]}")
        element = wait.until(EC.visibility_of_element_located(locator))
        element.click()
    print(browser.switch_to.alert.text)
    time.sleep(10)


