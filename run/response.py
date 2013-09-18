from .message import Message

class Response(Message):
    
    #Public
    
    def __init__(self, result, error=None):
        self._result = result
        self._error = error
    
    @property    
    def result(self):
        return self._result

    @property    
    def error(self):
        return self._error