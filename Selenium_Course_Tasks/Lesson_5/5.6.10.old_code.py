import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.5/5/1.html")
    color_list = [i.text for i in browser.find_elements(By.TAG_NAME, 'span')]
    dropdowns = browser.find_elements(By.TAG_NAME, 'select')
    buttons = browser.find_elements(By.XPATH, f"//div/button[@data-hex]")
    checkboxes = browser.find_elements(By.XPATH, f"//div/input[@type='checkbox']")
    inputs = browser.find_elements(By.XPATH, f"//div/input[@type='text']")
    check_buttons = browser.find_elements(By.XPATH, f"//div/button[text()]")
    check_all_elements_button = browser.find_element(By.XPATH, f"//button[text()='Проверить все элементы']")
    counter = 0
    for i in range(len(color_list)):
        select = Select(dropdowns[i])
        select.select_by_visible_text(color_list[i])
        ten_buttons = buttons[counter:counter + 10]
        for button in ten_buttons:
            button.click()
            if button.text == 'ОК':
                break
        counter += 10
        checkboxes[i].click()
        inputs[i].send_keys(f"{color_list[i]}")
        check_buttons[i].click()
    check_all_elements_button.click()
    alert = browser.switch_to.alert
    print(alert.text)
    time.sleep(3)