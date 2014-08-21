import csv
import ast
from box.argparse import Command
from box.functools import cachedproperty
from ..settings import settings


class Command(Command):

    # Public

    default_task = settings.default_task

    @cachedproperty
    def attribute(self):
        attribute = self._namespace.attribute
        if self.list:
            attribute = 'list'
        elif self.info:
            attribute = 'info'
        elif self.meta:
            attribute = 'meta'
        elif not attribute:
            attribute = self.default_task
        return attribute

    @cachedproperty
    def arguments(self):
        attribute = self._namespace.attribute
        arguments = self._namespace.arguments
        if (self.list or self.info or self.meta) and attribute:
            arguments = [attribute] + arguments
        parsed_arguments = self._parse_arguments(arguments)
        return parsed_arguments

    # Protected

    def _parse_arguments(self, arguments):
        args = []
        kwargs = {}
        for element in next(csv.reader([''.join(arguments)])):
            parts = [self._parse_literal(item.strip()) for item in
                     next(csv.reader([element], delimiter='='))]
            if len(parts) == 1:
                args.append(parts[0])
            elif len(parts) == 2:
                kwargs[parts[0]] = parts[1]
        return {'args': args, 'kwargs': kwargs}

    def _parse_literal(self, literal):
        try:
            value = ast.literal_eval(literal)
        except Exception:
            value = literal
        return value
