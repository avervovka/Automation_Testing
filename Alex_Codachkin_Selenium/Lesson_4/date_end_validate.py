import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://ru.wikipedia.org/')
print(f'Current Title: {driver.title}')
time.sleep(2)

driver.get('https://ya.ru')
print(f'Current Title: {driver.title}')
time.sleep(2)

driver.back()
assert 'https://ru.wikipedia.org/' in driver.current_url, 'ТЫ ПУДЕЛЬ!!!'
driver.refresh()
print(f'Current URL {driver.current_url}')
driver.forward()

print(f'Current URL {driver.current_url}')
time.sleep(5)

assert 'https://ya.ru' in driver.current_url, 'ФАИЛЕД!!!'
# url = driver.current_url
# print(f'URL page: {url}')
#
# current_title = driver.title
# print(f'Current Title: {current_title}')
#
# assert url == 'https://ru.wikipedia.org/', 'НЕВЕРНЫЙ URL'

# print(driver.page_source)
#
# time.sleep(3)
