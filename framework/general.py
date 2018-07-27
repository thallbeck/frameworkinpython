import inspect

class General:
    silentMode = False
    detailedDebugMode = False
    initialStackDepth = 1
    DATA_PATH = '/Users/Public/Documents/testautomation/'

    def __init__(self):
        self.initialStackDepth = len(inspect.stack())

    def set_silent_mode(self, mode):
        prev = mode
        silentMode = mode
        return prev



