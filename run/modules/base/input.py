from ...var import Var

class InputVar(Var):
    
    #Public
    
    def __init__(self, question, default=None, options=[], operator=input):
        self._question = question
        self._default = default
        self._options = options
        self._operator = operator
        
    def retrieve(self):
        while True:
            result = self._operator(self._prompt)
            if not result:
                result = self._default
            if self._options:
                if result in self._options:
                    return result
                else:
                    print()            
            else:
                return result
    
    #Protected
            
    @property
    def _prompt(self):
        return '{0} [{1}]'.format(self._question, self._help)
    
    @property
    def _help(self):
        items = []
        if self._options:
            for option in self._options:
                if option == self._default:
                    option = option + '*'
                items.append[option]
        else:
            items.append[self._default]
        return ', '.join(items)