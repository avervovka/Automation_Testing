import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with open("test.txt", "w") as file:
    content = file.write("automationbypython")

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/file_input.html')

    def first_name_sending(name):
        first_name = browser.find_element(By.XPATH, "//input[@name='firstname']")
        first_name.send_keys(name)


    def last_name_sending(last_name):
        first_name = browser.find_element(By.XPATH, "//input[@name='lastname']")
        first_name.send_keys(last_name)


    def email_sending(email):
        first_name = browser.find_element(By.XPATH, "//input[@name='email']")
        time.sleep(1)
        first_name.click()
        first_name.send_keys(email)


    def file_sender():
        file_choose = browser.find_element(By.ID, 'file')
        file_choose.send_keys('/Users/uladzimirzadarozhny/PycharmProjects/Automation_Testing/Automation_Course_Testing/Lesson_2/test.txt')


    def submit():
        submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

    first_name_sending('Vovka')
    last_name_sending('Avervovka')
    email_sending('avervovka@gmail.com')
    file_sender()
    submit()
    time.sleep(1)

    alert = browser.switch_to.alert
    print(alert.text)
