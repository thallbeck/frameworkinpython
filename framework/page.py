from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import general
import logintype

class page:

    TIMEOUT_IN_SECS = None
    SLEEP_IN_SECS = None

    def __init__(self):
        isJenkins = False

        login = logintype.LoginType.SAMPLE_MOVIEDB
        bLoggedIn = False
        driver = None

        standardPageSleep = 2

