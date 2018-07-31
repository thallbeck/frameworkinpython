import inspect
import time
from enum import Enum
import platform

class General:
    silent_mode = False
    detailed_debug_mode = False
    initial_stack_depth = 1
    DATA_PATH = '/Users/Public/Documents/testautomation/'

    def __init__(self):
        self.initial_stack_depth = self.get_stack_depth()

    def set_silent_mode(self, mode):
        prev = self.silent_mode
        self.silent_mode = mode
        return prev

    def get_silent_mode(self):
        return self.silent_mode

    def set_detailed_debug_mode(self, mode):
        prev = self.detailed_debug_mode
        self.detailed_debug_mode = mode
        return prev

    def get_detailed_debug_mode(self):
        return self.detailed_debug_mode

    def get_stack_depth(self):
        return len(inspect.stack())

    def debug(self, string_list, add_bullet_info):
        if (self.get_silent_mode()):
            return False

        if type(string_list) is str:
            print(string_list)
        else:
            for string in string_list:
                print(string)
        return True

    def sleep(self, time_in_seconds):
        if not (self.get_silent_mode()):
            self.debug('sleeping thread', False)
        time.sleep(time_in_seconds)
        return True

    def get_os(self):
        self.debug( 'raw os name is ' + platform.system(), False )
        if ( platform.system().startswith( "Windows" ) ):
            return OS.Windows
        elif ( platform.system().startswith( "Linux" ) ):
            return OS.Linux
        return OS.Mac



    def run_unit_tests(self):
        self.set_silent_mode(self.get_silent_mode())
        self.set_detailed_debug_mode(self.get_detailed_debug_mode())
        self.get_stack_depth()
        self.debug('single string test', False)
        self.debug(('multiple', 'string', 'test'), False)
        self.sleep(1)
        self.get_os()


class OS(Enum):
    Mac = 1
    Windows = 2
    Linux = 3


