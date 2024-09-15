import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://the-internet.herokuapp.com/status_codes')
status_codes = driver.find_elements(By.XPATH, '//li/a')
time.sleep(3)

for i in range(len(status_codes)):
    links = driver.find_elements('xpath', "//ul/li/a")
    link = links[i]
    link_text = link.text
    link.click()
    time.sleep(1)
    driver.back()
