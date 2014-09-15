from subprocess import Popen
from box.collections import merge_dicts
from clyde import Command
from ..module import Module
from ..task import Task
from ..var import Var


class CommandModule(Module):

    # Public

    def __init__(self, mapping=None, *args, **kwargs):
        if mapping is None:
            mapping = {}
        emapping = merge_dicts(self._default_mapping, mapping)
        for name, command in emapping.items():
            if not hasattr(type(self), name):
                task = CommandTask(command, meta_module=self)
                setattr(type(self), name, task)
        super().__init__(*args, **kwargs)

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', 'CommandModule')

    # Protected

    _default_mapping = {}


class CommandTask(Task):

    # Public

    def meta_invoke(self, *args, **kwargs):
        command = Command(*args, **kwargs)
        process = command(operator=Popen, shell=True)
        returncode = process.wait()
        if returncode != 0:
            raise RuntimeError(
                'Command "{command}" exited with "{returncode}"'.
                format(command=command, returncode=returncode))

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', 'Execute shell command.')


class CommandVar(Var, CommandTask): pass
