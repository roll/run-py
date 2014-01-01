from getpass import getpass
from jinja2 import Template
from run import Var

#TODO: improve templates
class InputVar(Var):
    
    #Public
    
    def __init__(self, text, default='', options=[], attempts=None,
                 input_operator=None, print_operator=None, 
                 prompt_template=None, error_template=None):
        self._text = text
        self._default = default
        self._options = options
        self._attempts = attempts or self._default_attempts
        self._input_operator = input_operator or self._default_input_operator
        self._print_operator = print_operator or self._default_print_operator
        self._prompt_template = prompt_template or self._default_prompt_template
        self._error_template = error_template or self._default_error_template
        
    def retrieve(self):
        for _ in range(0, self._attempts):
            result = self._input_operator(self._prompt)
            if not result:
                result = self._default
            if self._options:
                if result not in self._options:
                    self._print_operator(self._error)
                    continue 
            return result
        else:
            raise ValueError(
                'Input error in all of {attempts} attempts '
                'where options are "{options}"'.format(
                    attempts=self._attempts,
                    options=self._options))
    
    #Protected
    
    _default_attempts = 3    
    _default_input_operator = input
    _default_print_operator = print
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