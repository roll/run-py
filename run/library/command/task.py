from subprocess import Popen
from claire import Command, Operator
from ...task import Task


class CommandTask(Task):

    # Public

    @property
    def meta_docstring(self):
        return self.meta_inspect(
            name='docstring', lookup=True, default='Execute shell command.')

    def meta_invoke(self, *args, **kwargs):
        operator = Operator(Popen, shell=True)
        command = Command(*args, meta_operator=operator, **kwargs)
        process = command()
        returncode = process.wait()
        if returncode != 0:
            raise RuntimeError(
                'Command "{command}" exited with "{returncode}"'.
                format(command=command, returncode=returncode))
