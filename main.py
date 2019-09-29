from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
print('Browser has opened. Scan the qr code and get in.')
time.sleep(30)
print('Name of person or group to which you want to send the message:')
target = str(input())
print('Whats the message?')
msg = str(input())
search = driver.find_element_by_class_name('_2zCfw')
time.sleep(5)
search.send_keys(target)
search.send_keys(Keys.ENTER)
inp = driver.find_element_by_class_name('_3u328')
time.sleep(5)
inp.send_keys(msg, Keys.ENTER)
print('Sent the msg "' + msg + '" to ' + target)


