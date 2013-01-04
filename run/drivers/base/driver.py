from run.concepts.driver import Driver

class Driver(Driver):
    
    def __init__(self, command):
        self._command = command
    
    def process(self): 
        pass