import time
import pickle
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

with webdriver.Chrome() as browser:
    url = 'https://parsinger.ru/selenium/5.10/6/index.html'