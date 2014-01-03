class Dispatcher:

    #Public
    
    def __init__(self):
        self._handlers = []
    
    def add_handler(self, handler):
        self._handlers.append(handler)
    
    def add_signal(self, signal):
        for handler in self._handlers:
            handler.handle(signal)
            
            
class NullDispatcher(Dispatcher):
    
    #Public
    
    def __bool__(self):
        return False    
    
    def add_handler(self, handler): pass
    def add_signal(self, signal): pass        