from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    actions = ActionChains(browser)
    url = 'https://parsinger.ru/selenium/5.10/2/index.html'
    browser.get(url)
    wait = WebDriverWait(browser, 10)

    squares = browser.find_elements(By.CSS_SELECTOR, '.draganddrop')

    for square in squares:
        actions.drag_and_drop_by_offset(square, xoffset=1167, yoffset=0).perform()

    message = browser.find_element(By.ID, 'message')
    wait.until(lambda x: message.text != '')
    print(message.text)
