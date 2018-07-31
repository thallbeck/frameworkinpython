from enum import Enum
import general
import environment

class LoginType(Enum):

    SAMPLE_MOVIEDB = (
        "",
        environment.Environment.Prod,
        "",
        "",
        "",
        "",
        "",
        "http://www.themoviedb.org"
        )

    SAMPLE_CARBONBLACK = (
        "",
        environment.Environment.Prod,
        "",
        "",
        "",
        "",
        "",
        "https://www.carbonblack.com"
        )

    def __init__(self, displayName, environment, username, password, usernameXpath, passwordXpath, loginButtonXpath, startingUrl):
        self.displayName = displayName
        self.environment = environment
        self.username = username
        self.password = password
        self.usernameXpath = usernameXpath
        self.passwordXpath = passwordXpath
        self.loginButtonXpath = loginButtonXpath
        self.startingUrl = startingUrl

