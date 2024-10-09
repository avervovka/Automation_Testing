import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    all_buttons = list

    def clicker(one, two, three):
        for item in [one, two, three]:
            item.click()
            try:
                assert 'active' in item.get_attribute('class')
            except AssertionError:
                print('Уже не нажата')

    url = 'https://demoqa.com/selectable'
    browser.get(url)
    browser.find_element(By.ID, 'demo-tab-grid').click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    one_button = browser.find_element(By.XPATH, "//div[@id='row1']/li[text()='One']")
    five_button = browser.find_element(By.XPATH, "//div[@id='row2']/li[text()='Five']")
    nine_button = browser.find_element(By.XPATH, "//div[@id='row3']/li[text()='Nine']")

    for i in range(2):
        clicker(one_button, five_button, nine_button)
