from .message import CommonMessage

class Request(CommonMessage):
    
    #Public
    
    def __init__(self, method, arguments, options):
        self._method = method
        self._arguments = arguments
        self._options = options
    
    @property
    def method(self):
        return self.method  
    
    @property
    def arguments(self):
        return self._arguments
    
    @property
    def options(self):
        return self._options    