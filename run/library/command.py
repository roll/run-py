from subprocess import Popen
from ..task import Task
from ..var import Var


class CommandTask(Task):

    # Public

    def meta_invoke(self, command='', *, prefix='', separator=' '):
        ecommand = separator.join(filter(None, [prefix, command]))
        process = Popen(ecommand, shell=True)
        returncode = process.wait()
        if returncode != 0:
            raise RuntimeError(
                'Command "{ecommand}" exited with "{returncode}"'.
                format(ecommand=ecommand, returncode=returncode))

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', 'Execute shell command.')


class CommandVar(Var, CommandTask): pass