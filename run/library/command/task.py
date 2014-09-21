from subprocess import Popen
from clyde import Command
from ...task import Task


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
        return self.meta_inspect(
            name='docstring', lookup=True, default='Execute shell command.')
