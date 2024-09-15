import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
prefs = {"download.default_directory": f"{os.getcwd()}/downloads"}

chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

with driver as browser:
    browser.get("http://the-internet.herokuapp.com/download")
    elements = browser.find_elements(By.TAG_NAME, 'a')
    for i in range(1, len(elements)):
        elements[i].click()
        time.sleep(1)
