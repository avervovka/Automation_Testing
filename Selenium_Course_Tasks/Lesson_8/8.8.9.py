from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.9/7/index.html'
    browser.get(url)
    wait = WebDriverWait(browser, 20)

    all_contaner = browser.find_elements(By.CLASS_NAME, 'container')

    for item in all_contaner:
        input_field = item.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')
        button = item.find_element(By.TAG_NAME, 'button')

        if wait.until(EC.element_to_be_selected(input_field)):
            button.click()
            wait.until(lambda _: item.get_attribute('style') == 'background-color: green;')

            continue

    result = browser.find_element(By.ID, 'result')
    print(result.text)
