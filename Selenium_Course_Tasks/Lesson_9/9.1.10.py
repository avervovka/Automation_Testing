import time
from re import fullmatch
from webcolors import rgb_to_name
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def get_block_color(block_style):
    style = block_style.split(';')[0].split(': ')[1]
    match_obj = fullmatch(r'rgb\((\d{1,3}), (\d{1,3}), (\d{1,3})\)', style)
    rgb = tuple(map(int, match_obj.group(1, 2, 3))) if match_obj else None
    color = rgb_to_name(rgb) if rgb else style
    return color


with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get('https://parsinger.ru/selenium/5.10/3/index.html')
    browser.implicitly_wait(10)
    actions = ActionChains(browser)
    waiter = WebDriverWait(browser, 10)
    blocks = browser.find_elements(By.CLASS_NAME, 'draganddrop')

    for block in blocks:
        color = get_block_color(block.get_attribute('style'))
        selector = f'div[style *= "border-color: {color}"]'
        box = browser.find_element(By.CSS_SELECTOR, selector)
        actions.click_and_hold(block)
        actions.move_to_element(box)
        actions.perform()

    res = waiter.until(EC.visibility_of_element_located((By.ID, 'message')))
    print(res.text)