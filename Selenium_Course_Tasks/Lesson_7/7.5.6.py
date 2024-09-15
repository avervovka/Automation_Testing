import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]
# window_dict = dict(zip(window_size_x, window_size_y))
chrome_options = Options()
# chrome_options.add_argument('--headless')

with webdriver.Chrome(options=chrome_options) as browser:
    browser.get('https://parsinger.ru/window_size/2/index.html')
    time.sleep(2)
    for width in window_size_x:
        for height in window_size_y:
            browser.set_window_size(width, height + 139)
            text = browser.find_element(By.ID, 'result')
            if text.text.isdigit():
                print(browser.get_window_size())
