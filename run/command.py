import sys
import csv
import ast
from lib31.python import cachedproperty
from packgram.console import Command
from .settings import settings

class Command(Command):
    
    #Public
    
    schema = settings.command_schema
    
    @cachedproperty
    def method(self):
        if not self.help:
            return self._namespace.method
        else:
            if self._namespace.method:
                return 'help'
            else:
                print(self._parser.format_help().strip())
                sys.exit()
    
    @cachedproperty
    def args(self):
        if not self.help:
            return self._parsed_arguments[0]
        else:
            return [self._namespace.method]
    
    @cachedproperty    
    def kwargs(self):
        if not self.help:
            return self._parsed_arguments[1]
        else:
            return {}       
    
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