from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/draganddrop/3/index.html")
    actions = ActionChains(driver)
    element = driver.find_element(By. ID, 'block1')
    actions.click_and_hold(element).perform()
    for point in driver.find_elements(By.CLASS_NAME, 'controlPoint'):
        actions.move_to_element(point)
    actions.release(element).perform()
    print(driver.find_element(By.ID, 'message').text)