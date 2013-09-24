import ast
import csv
from lib31.console import Command
from .settings import settings

class Command(Command):
    
    #Public
    
    schema = settings.command_schema
      
    #TODO: use cachedproperty 
    @property
    def args(self):
        return self._parsed_parameters[0]
    
    #TODO: use cachedproperty    
    @property    
    def kwargs(self):
        return self._parsed_parameters[1]
    
    #Protected
    
    #TODO: use cachedproperty 
    @property
    def _parsed_parameters(self):
        args = []
        kwargs = {}
        for element in next(csv.reader([''.join(self.parameters)])):
            parts = [self._parse_literal(item.strip()) for item in 
                     next(csv.reader([element], delimiter='='))]
            if len(parts) == 1:
                args.append(parts[0])
            elif len(parts) == 2:
                kwargs[parts[0]] = parts[1]
        return (args, kwargs)
    
    def _parse_literal(self, literal):
        try:
            value = ast.literal_eval(literal)
        except ValueError:
            return literal
        return value