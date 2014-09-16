import csv
import ast
from box.argparse import Command
from box.functools import cachedproperty


class Command(Command):

    # Public

    @cachedproperty
    def attribute(self):
        attribute = self._namespace.attribute
        if self.list:
            attribute = 'list'
        elif self.info:
            attribute = 'info'
        elif self.meta:
            attribute = 'meta'
        return attribute

    @cachedproperty
    def arguments(self):
        attribute = self._namespace.attribute
        arguments = self._namespace.arguments
        if (self.list or self.info or self.meta) and attribute:
            arguments = [attribute] + arguments
        parsed_arguments = self.__parse_arguments(arguments)
        return parsed_arguments

    # Private

    def __parse_arguments(self, arguments):
        args = []
        kwargs = {}
        for element in next(csv.reader([''.join(arguments)])):
            parts = [self.__parse_literal(item.strip()) for item in
                     next(csv.reader([element], delimiter='='))]
            if len(parts) == 1:
                args.append(parts[0])
            elif len(parts) == 2:
                kwargs[parts[0]] = parts[1]
        return {'args': args, 'kwargs': kwargs}

    def __parse_literal(self, literal):
        try:
            value = ast.literal_eval(literal)
        except Exception:
            value = literal
        return value
