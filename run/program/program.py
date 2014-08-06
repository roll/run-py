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
        self._machine.process(
            self._command.task,
            *self._command.args,
            **self._command.kwargs)

    @cachedproperty
    def _machine(self):
        machine = self._Machine(
            names=self._command.names,
            tags=self._command.tags,
            file=self._command.file,
            basedir=self._command.basedir,
            recursively=self._command.recursively,
            grayscale=self._command.grayscale,
            skip=self._command.skip,
            plain=self._command.plain)
        return machine


program = Program(sys.argv)
