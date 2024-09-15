import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

browser.get('https://www.freeconferencecall.com/login')

browser.find_element("ID", 'loginformsubmit')