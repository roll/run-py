import subprocess
from .task import Task


class SubprocessTask(Task):

    # Public

    def meta_invoke(self, command='', *, prefix='', separator=' '):
        ecommand = separator.join(filter(None, [prefix, command]))
        process = subprocess.Popen(ecommand, shell=True)
        returncode = process.wait()
        if returncode != 0:
            raise RuntimeError(
                'Command "{ecommand}" exited with "{returncode}"'.
                format(ecommand=ecommand, returncode=returncode))

    @property
    def meta_docstring(self):
        return self._meta_params.get(
            'docstring', 'Execute shell command.')
