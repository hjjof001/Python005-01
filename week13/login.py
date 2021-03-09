import time

from selenium import webdriver


browser = webdriver.Chrome()

browser.get('https://shimo.im/login?from=home')
username = browser.find_element_by_xpath('//input[@name="mobileOrEmail"]')
username.send_keys('15446068888')
password = browser.find_element_by_xpath('//input[@name="password"]')
password.send_keys('password')
button = browser.find_element_by_xpath('//button[@type="black"]')
button.click()
time.sleep(30)