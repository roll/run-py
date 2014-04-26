import os
import unittest
from subprocess import Popen, PIPE

class ExamplesTest(unittest.TestCase):

    #Public
    
    __test__ = False
    
    #Protected
    
    def _execute(self, command='', message=None, **kwargs):
        ecommand = 'python3 -c "from run import program; program()" '
        ecommand += '-b {basedir} '.format(basedir=self._basedir) 
        ecommand += '-f {filename} '.format(filename=self._filename)
        ecommand += command
        process = Popen(ecommand, shell=True, universal_newlines=True,
            stdin=PIPE, stdout=PIPE, stderr=PIPE, **kwargs)
        stdout, _ = process.communicate(message)
        return stdout
    
    @property
    def _basedir(self):
        filedir = os.path.dirname(__file__)
        basedir = os.path.abspath(os.path.join(filedir, '..', '..', 'examples'))
        return basedir
    
    @property
    def _filename(self):
        return 'runfile.py'