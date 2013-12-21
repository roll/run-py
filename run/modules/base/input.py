from getpass import getpass
from jinja2 import Template
from ...var import Var

class InputVar(Var):
    
    #Public
    
    def __init__(self, text, default=None, options=[], 
                 operator=None, prompt_template=None, error_template=None,
                 **kwargs):
        self._text = text
        self._default = default
        self._options = options
        self._operator = operator or self._default_operator
        self._prompt_template = prompt_template or self._default_prompt_template
        self._error_template = error_template or self._default_error_template
        
    def retrieve(self):
        while True:
            result = self._operator(self._prompt)
            if not result:
                result = self._default
            if self._options:
                if result not in self._options:
                    print(self._error)
                    continue 
            return result           
    
    #Protected
    
    _default_operator = input
    _default_prompt_template = '{{ text }}'
    _default_error_template = 'Try again..'
    
    @property
    def _prompt(self):
        template = Template(self._prompt_template)
        prompt = template.render(self._context)
        return prompt

    @property
    def _error(self):
        template = Template(self._error_template)
        error = template.render(self._context)
        return error
    
    @property
    def _context(self):
        return {'text': self._text,
                'default': self._default,
                'options': self._options,}
   
    
class HiddenInputVar(InputVar):    
    
    #Protected
    
    _default_operator = getpass    