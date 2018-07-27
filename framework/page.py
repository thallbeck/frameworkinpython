from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import general

universal = general.General()
universal.set_silent_mode(False)
binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\Users\\Public\\Documents\\testautomation\\geckodriver.exe')
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
driver.quit()

