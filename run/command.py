import csv
import ast
from lib31.console import Command
from lib31.python import cachedproperty
from .settings import settings

class Command(Command):
    
    #Public
    
    schema = settings.command_schema

    @property
    def attribute(self):
        attribute = self._namespace.attribute        
        if self.help and attribute:
            attribute = 'help'
        return attribute
    
    @property
    def arguments(self):
        attribute = self._namespace.attribute
        arguments = self._namespace.arguments
        if self.help and attribute:
            arguments = [attribute]+arguments
        return arguments

    @property
    def args(self):
        return self._parsed_arguments[0]
    
    @property    
    def kwargs(self):
        return self._parsed_arguments[1]
    
    #Protected
    
    @cachedproperty
    def _parsed_arguments(self):
        args = []
        kwargs = {}
        for element in next(csv.reader([''.join(self.arguments)])):
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