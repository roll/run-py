import csv
import ast
from box.argparse import Command
from box.functools import cachedproperty
from ..settings import settings

class Command(Command):

    # Public

    default_attribute = settings.default_attribute

    @property
    def attribute(self):
        attribute = self._namespace.attribute
        if self.list:
            attribute = 'list'
        elif self.info:
            attribute = 'info'
        elif self.meta:
            attribute = 'meta'
        elif not attribute:
            attribute = self.default_attribute
        return attribute

    @property
    def args(self):
        return self._parsed_arguments[0]

    @property
    def kwargs(self):
        return self._parsed_arguments[1]

    # Protected

    @cachedproperty
    def _parsed_arguments(self):
        args = []
        kwargs = {}
        for element in next(csv.reader([''.join(self._arguments)])):
            parts = [self._parse_literal(item.strip()) for item in
                     next(csv.reader([element], delimiter='='))]
            if len(parts) == 1:
                args.append(parts[0])
            elif len(parts) == 2:
                kwargs[parts[0]] = parts[1]
        return (args, kwargs)

    @property
    def _arguments(self):
        attribute = self._namespace.attribute
        arguments = self._namespace.arguments
        if (self.list or self.info or self.meta) and attribute:
            arguments = [attribute] + arguments
        return arguments

    def _parse_literal(self, literal):
        try:
            value = ast.literal_eval(literal)
        except Exception:
            value = literal
        return value
