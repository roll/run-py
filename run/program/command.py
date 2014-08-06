import csv
import ast
from box.argparse import Command
from box.functools import cachedproperty
from ..settings import settings


class Command(Command):

    # Public

    default_task = settings.default_task

    @property
    def task(self):
        task = self._namespace.task
        if self.list:
            task = 'list'
        elif self.info:
            task = 'info'
        elif self.meta:
            task = 'meta'
        elif not task:
            task = self.default_task
        return task

    @property
    def arguments(self):
        task = self._namespace.task
        arguments = self._namespace.arguments
        if (self.list or self.info or self.meta) and task:
            arguments = [task] + arguments
        return arguments

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
        except Exception:
            value = literal
        return value
