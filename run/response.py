from .message import Message

class Response(Message):
    
    #Public
    
    def __init__(self, result, error=''):
        self._result = result
        self._error = error
    
    @property
    def content(self):
        content = {}
        content['result'] = self.result
        if self.error:
            content['error'] = self.error
        return content
        
    @property    
    def result(self):
        return self._result

    @property    
    def error(self):
        return self._error