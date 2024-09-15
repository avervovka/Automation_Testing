import math
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://suninjuly.github.io/math.html')
a = driver.find_element('xpath', "//span[@class='nowrap' and @id='input_value']")
time.sleep(2)

driver.find_element(By.ID, 'answer').send_keys(calc(a.text))
# calc(a.text)
# time.sleep(2)

driver.find_element(By.ID, 'robotCheckbox').click()
driver.find_element(By.ID, 'robotsRule').click()
driver.find_element(By.TAG_NAME, 'button').click()
time.sleep(30)
