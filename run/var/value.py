from .var import Var

class ValueVar(Var):
    
    #Public
    
    def __init__(self, value):
        self._value = value
 
    def retrieve(self):
        return self._value