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
        browser.find_element(By.XPATH, f"//div[@data-index={i}]").click()
        browser.find_element(By.ID, 'close_ad').click()
        banner = wait.until(EC.invisibility_of_element_located((By.ID, 'ad_window')))
        time.sleep(10)
        text = browser.find_element(By.XPATH, f"//div[@data-index={i}]").text
        if i != 8:
            text += '-'
        a += text
    print(a)



