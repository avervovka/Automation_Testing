import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://demoqa.com/text-box')

username = driver.find_element('id', 'userName')
username.clear()
time.sleep(1)
username.send_keys('AVER')
time.sleep(1)

email_text = driver.find_element('id', 'userEmail')
email_text.clear()
time.sleep(1)
email_text.send_keys('avervov@gmail.com')
time.sleep(1)

address = driver.find_element('id', 'currentAddress')
address.clear()
time.sleep(1)
address.send_keys('Minsk, Belarus')
time.sleep(1)

permament_adress = driver.find_element('id', 'permanentAddress')
permament_adress.clear()
time.sleep(1)
permament_adress.send_keys('Minsk, Belarus')
time.sleep(1)

elements = [username, email_text, address, permament_adress]
b = 0
keys = ['AVER', 'avervov@gmail.com', 'Minsk, Belarus', 'Minsk, Belarus']
for element in elements:
    assert element.get_attribute('value') == keys[b]
    b += 1
