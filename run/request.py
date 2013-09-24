from .message import Message

class Request(Message):
    
    #Public
    
    def __init__(self, method, args=[], kwargs={}):
        self._method = method
        self._args = args
        self._kwargs = kwargs
    
    @property
    def content(self):
        content = {}
        content['method'] = self.method
        if self.args:
            content['args'] = self.args
        if self.kwargs:
            content['kwargs'] = self.kwargs
        return content         
     
    @property
    def method(self):
        return self._method  
    
    @property
    def args(self):
        return self._args
    
    @property
    def kwargs(self):
        return self._kwargs    