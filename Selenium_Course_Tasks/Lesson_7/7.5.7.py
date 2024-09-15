import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')
a = []

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/blank/3/index.html')
    buttons = browser.find_elements(By.XPATH, "//input[@class='buttons']")
    for page in buttons:
        page.click()
    all_tabs = browser.window_handles
    current_handle = browser.current_window_handle
    for handle in all_tabs:
        if handle != current_handle:
            browser.switch_to.window(handle)
            a.append(int(browser.title))
    print(sum(a))


