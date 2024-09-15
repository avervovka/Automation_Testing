from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.10/4/index.html'
    browser.get(url)
    action = ActionChains(browser)
    wait = WebDriverWait(browser, 300)

    balls_red = browser.find_elements(By.XPATH, f"//div[contains (@class, 'red_ball')]")
    balls_blue = browser.find_elements(By.XPATH, f"//div[contains (@class, 'blue_ball')]")
    balls_green = browser.find_elements(By.XPATH, f"//div[contains (@class, 'green_ball')]")
    balls_black = browser.find_elements(By.XPATH, f"//div[contains (@class, 'black_ball')]")
    boxes = browser.find_elements(By.XPATH, f"//div[contains (@class, 'basket_color')]")

    all_boxes = [balls_red, balls_blue, balls_green, balls_black]
    counter = 0


    def box_colors(balls_color):
        for balls in balls_color:
            action.drag_and_drop(balls, boxes[counter]).perform()


    for i in all_boxes:
        box_colors(i)
        counter += 1

    wait.until(lambda x: browser.find_element(By.CLASS_NAME, 'message').text != '')

    print(browser.find_element(By.CLASS_NAME, 'message').text)
