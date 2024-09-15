import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException as NS


with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/infiniti_scroll_3/'
    browser.get(url)
    actions = ActionChains(browser)
    counter = 1
    a = []
    b = []
    result = 0
    for i in range(1, 6):
        scroll_container = browser.find_element(By.XPATH, f"//*[@id='scroll-container_{i}']/div")
        a.append(scroll_container)

    for i in range(5):
        container = browser.find_element(By.ID, f"scroll-container_{i + 1}")
        while True:
            actions.move_to_element(a[i]).scroll_by_amount(0, 100).perform()
            try:
                container.find_element(By.CLASS_NAME, 'last-of-list')
                break
            except NS:
                continue

    elements = browser.find_elements(By.XPATH, "//span[contains(@id, 'Infi')]")
    for element in elements:
        if element.text.isdigit():
            b.append(int(element.text))

    print(sum(b))
