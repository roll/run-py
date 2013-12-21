from ...var import Var

class InputVar(Var):
    
    #Public
    
    def __init__(self, prompt, options=[]):
        self._prompt = prompt
        self._options = options
        
    def retrieve(self):
        while True:
            result = input(self._prompt)
            if (not self._options or
                result in self._options):
                return result                    