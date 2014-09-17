import os
import unittest
from subprocess import Popen, PIPE


class ExamplesTest(unittest.TestCase):

    # Actions

    __test__ = False

    # Helpers

    def execute(self, command='', messages=[None], **kwargs):
        result = ''
        ecommand = 'python3 -c "from run.program import program; program()" '
        ecommand += '--filepath {filepath} '.format(filepath=self.filepath)
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
    def filepath(self):
        return os.path.join(self.dirpath, self.filename)

    @property
    def dirpath(self):
        filedir = os.path.dirname(__file__)
        dirpath = os.path.abspath(os.path.join(filedir, '..', '..', 'examples'))
        return dirpath

    @property
    def filename(self):
        return 'runfile.py'
