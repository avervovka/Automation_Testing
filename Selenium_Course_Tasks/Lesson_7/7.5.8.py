import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

sites = ['http://parsinger.ru/blank/1/1.html',
         'http://parsinger.ru/blank/1/2.html',
         'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html',
         'http://parsinger.ru/blank/1/5.html',
         'http://parsinger.ru/blank/1/6.html']

chrome_options = Options()
a = []

with webdriver.Chrome(options=chrome_options) as browser:
    for i in sites:
        browser.execute_script(f"window.open('{i}')")
        time.sleep(0.5)
    all_tabs = browser.window_handles
    for i in range(1, len(all_tabs)):
        browser.switch_to.window(all_tabs[i])
        checkbox = browser.find_element(By.XPATH, '//input[@type="checkbox"]')
        checkbox.click()
        time.sleep(0.5)
        result = int(browser.find_element(By.ID, 'result').text)
        a.append(pow(result, 0.5))
    print(round(sum(a), 9))
