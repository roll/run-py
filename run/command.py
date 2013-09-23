import ast
import csv
from lib31.console import Command

class Command(Command):
    
    #Public
      
    #TODO: use cachedproperty 
    @property
    def arguments(self):
        return self._parsed_parameters[0]
    
    #TODO: use cachedproperty    
    @property    
    def options(self):
        return self._parsed_parameters[1]
    
    #Protected
    
    #TODO: use cachedproperty 
    @property
    def _parsed_parameters(self):
        arguments = []
        options = {}
        for element in csv.reader([''.join(self.parameters)]):
            parts = [self._parse_literal(item) for item in 
                     next(csv.reader([element], delimiter='='))]
            if len(parts) == 1:
                arguments.append(parts[0])
            elif len(parts) == 2:
                options[parts[0]] = parts[1]
        return (arguments, options)
    
    def _parse_literal(self, literal):
        try:
            value = ast.literal_eval(literal)
        except ValueError:
            return literal
        return value