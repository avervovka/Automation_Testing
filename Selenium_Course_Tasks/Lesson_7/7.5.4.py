import time
from selenium.webdriver import Keys, ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.set_window_size(555, 694)
    browser.get('https://parsinger.ru/window_size/1/')
    time.sleep(2)
    # width_in = 1200
    # height_in = 640
    # height_out = browser.get_window_size()["height"]
    # width_out = browser.get_window_size()["width"]
    # sum_height = height_out - height_in
    # sum_width = width_out - width_in
    # print(sum_width, sum_height, height_out, width_out)

    text = browser.find_element(By.ID, 'result')
    print(text.text)
