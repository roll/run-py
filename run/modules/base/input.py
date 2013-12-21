from ...var import Var

class InputVar(Var):
    
    #Public
    
    def __init__(self, prompt):
        self._prompt = prompt
        
    def retrieve(self):
        return input(self._prompt)