import sys
from box.functools import cachedproperty
from box.logging import Program
from ..machine import Machine
from ..settings import settings
from .command import Command


class Program(Program):

    # Protected

    _Command = Command
    _Machine = Machine
    _settings = settings

    def _execute(self):
        self._machine.run(
            self._command.attribute,
            *self._command.arguments['args'],
            **self._command.arguments['kwargs'])

    @cachedproperty
    def _machine(self):
        machine = self._Machine(
            key=self._command.key,
            tags=self._command.tags,
            file=self._command.file,
            exclude=self._command.exclude,
            basedir=self._command.basedir,
            recursively=self._command.recursively,
            plain=self._command.plain,
            skip=self._command.skip,
            compact=self._command.compact)
        return machine


program = Program(sys.argv)
