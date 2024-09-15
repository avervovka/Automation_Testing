import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.9/5/index.html'
    browser.get(url)
    wait = WebDriverWait(browser, 300)
    a = str()

    for i in range(9):
        element_locator = (By.XPATH, f"//div[@data-index={i}]")
        element = browser.find_element(*element_locator)
        element.click()
        browser.find_element(By.ID, 'close_ad').click()
        banner = wait.until(EC.invisibility_of_element_located((By.ID, 'ad_window')))
        wait.until(lambda text_timer: element.text != '')
        a += element.text + '-'
    print(a[:len(a) - 1:])
