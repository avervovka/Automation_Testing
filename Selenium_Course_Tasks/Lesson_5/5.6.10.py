import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.5/5/test/test.html")
    colors = browser.find_elements(By.XPATH, "//div[@id='main-container']/div/div/button[@data-hex]")

    divs = browser.find_elements(By.XPATH, "//div[@id='main-container']/div")
    dropdowns = browser.find_elements(By.TAG_NAME, 'select')
    checkboxes = browser.find_elements(By.XPATH, f"//input[@type='checkbox']")
    poles = browser.find_elements(By.XPATH, f"//input[@type='text']")
    # elements = browser.find_elements(By.XPATH, f"//button[text()='Проверить']")
    counter = 0
    for i in colors:
        i.click()

    for i in range(len(divs)):
        text = divs[i].find_element(By.TAG_NAME, 'span').text
        select = Select(dropdowns[i])
        select.select_by_visible_text(text)
        time.sleep(3)
        checkboxes[i].click()
        time.sleep(3)
        poles[i].send_keys(f"{text}")
        time.sleep(30)
        browser.find_element(By.XPATH, f"//button[text()='Проверить']").click()
        time.sleep(2)