from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import general

universal = general.General()
universal.run_unit_tests()
universal.set_silent_mode(False)
universal.debug('\nstarting the test', False)

some_strings = ('string1', 'string2', 'string3')
universal.debug(some_strings, False)

print list(general.OS)
print 'this OS is ' + str(universal.get_os())

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary, executable_path='C:\\Users\\Public\\Documents\\testautomation\\geckodriver.exe')
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
driver.quit()

universal.debug('\nending the test', False)

