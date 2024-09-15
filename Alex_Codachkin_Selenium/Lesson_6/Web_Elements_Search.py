import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('id', 'wikipedia-icon')
driver.find_element('id', 'wikipedia-search-input')
driver.find_element('tag name', 'div')
