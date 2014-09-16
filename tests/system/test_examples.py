import os
import unittest
from subprocess import Popen, PIPE


class ExamplesTest(unittest.TestCase):

    # Public

    __test__ = False

    # Protected

    def _execute(self, command='', messages=[None], **kwargs):
        result = ''
        ecommand = 'python3 -c "from run.program import program; program()" '
        ecommand += '--filepath {filepath} '.format(filepath=self._filepath)
        ecommand += '--plain '
        ecommand += command
        process = Popen(ecommand,
            shell=True, universal_newlines=True,
            stdin=PIPE, stdout=PIPE, stderr=PIPE, **kwargs)
        for message in messages:
            stdout, stderr = process.communicate(message)
            if stderr:
                raise RuntimeError(stderr)
            result += stdout
        return stdout

    @property
    def _filepath(self):
        return os.path.join(self._dirpath, self._filename)

    @property
    def _dirpath(self):
        filedir = os.path.dirname(__file__)
        dirpath = os.path.abspath(os.path.join(filedir, '..', '..', 'examples'))
        return dirpath

    @property
    def _filename(self):
        return 'runfile.py'
