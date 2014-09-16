import sys
from box.functools import cachedproperty
from box.logging import Program
from ..machine import Machine
from ..settings import settings
from .command import Command


class Program(Program):

    # Protected

    _Command = Command  # override
    _settings = settings  # override

    def _execute(self):
        self._machine.run(
            self._command.attribute,
            *self._command.arguments['args'],
            **self._command.arguments['kwargs'])

    @cachedproperty
    def _machine(self):
        machine = Machine(
            filepath=self._command.filepath,
            compact=self._command.compact,
            plain=self._command.plain)
        return machine


program = Program(sys.argv)
