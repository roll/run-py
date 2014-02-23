from subprocess import Popen, PIPE
from .task import Task

class SubprocessTask(Task):

    #Public

    def __init__(self, prefix='', separator=' '):
        self._prefix = prefix
        self._separator = separator
        
    def invoke(self, command=''):
        ecommand = self._separator.join(
            filter([self._prefix, command]))
        process = Popen(ecommand, shell=True, 
            stdin=PIPE, stdout=PIPE, stderr=PIPE)
        returncode = process.wait()
        if returncode != 0:
            raise RuntimeError(
                'Command "{ecommand}" exited with "{returncode}"'.
                format(ecommand=ecommand, returncode=returncode))