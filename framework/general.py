import inspect

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






    def run_unit_tests(self):
        self.set_silent_mode(self.get_silent_mode())
        self.set_detailed_debug_mode(self.get_detailed_debug_mode())
        self.get_stack_depth()
        self.debug('single string test', False)
        self.debug(('multiple', 'string', 'test'), False)





