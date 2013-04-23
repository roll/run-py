class BaseDriver(object):
    
    def __init__(self, command):
        self._command = command
    
    def process(self): 
        pass