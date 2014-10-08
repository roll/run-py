import sys
import ast
import csv
import logging.config
from box.argparse import Program
from box.functools import cachedproperty
from .machine import Machine
from .settings import settings


class program(Program):

    # Public

    default_config = settings.argparse  # override

    def __call__(self):
        self.__init_logging()
        self.__execute()

    @cachedproperty
    def attribute(self):
        attribute = self['attribute']
        if self.list:
            attribute = 'list'
        elif self.info:
            attribute = 'info'
        elif self.meta:
            attribute = 'meta'
        return attribute

    @cachedproperty
    def arguments(self):
        attribute = self['attribute']
        arguments = self['arguments']
        if (self.list or self.info or self.meta) and attribute:
            arguments = [attribute] + arguments
        parsed_arguments = self.__parse_arguments(arguments)
        return parsed_arguments

    # Private

    def __init_logging(self):
        logging.config.dictConfig(settings.logging_config)
        logger = logging.getLogger()
        if self.debug:
            logger.setLevel(logging.DEBUG)
        if self.verbose:
            logger.setLevel(logging.INFO)
        if self.quiet:
            logger.setLevel(logging.ERROR)

    def __execute(self):
        try:
            self.__machine.run(
                self.attribute,
                *self.arguments['args'],
                **self.arguments['kwargs'])
        except Exception as exception:
            logging.getLogger(__name__).error(
                str(exception), exc_info=self.debug)
            sys.exit(1)

    @cachedproperty
    def __machine(self):
        machine = Machine(
            filepath=self.filepath,
            compact=self.compact,
            plain=self.plain)
        return machine

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
