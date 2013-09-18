from .message import CommonMessage

class Request(CommonMessage):
    
    #Public
    
    def __init__(self, arguments, options):
        self._arguments = arguments
        self._option = options
        
    @property
    def arguments(self):
        return self._arguments
    
    @property
    def options(self):
        return self._options    