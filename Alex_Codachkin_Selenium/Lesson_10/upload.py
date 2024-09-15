import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

with browser:
    browser.get("https://demoqa.com/upload-download")
    time.sleep(2)
    upload_button = browser.find_element(By.ID, "uploadFile")
    upload_button.send_keys(f"{os.getcwd()}/downloads/photo.jpeg")
    time.sleep(4)
