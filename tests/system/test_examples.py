import os
import unittest
from subprocess import check_output

class ExamplesTest(unittest.TestCase):

    #Public
    
    __test__ = False
    
    #Protected
    
    def _execute(self, command):
        ecommand = 'python3 -c "from run import program; program()" '
        ecommand += '-b {basedir} '.format(basedir=self._basedir) 
        ecommand += '-f {filename} '.format(filename=self._filename)
        ecommand += command
        result = check_output(ecommand, shell=True)
        return result.decode()
    
    @property
    def _basedir(self):
        filedir = os.path.dirname(__file__)
        basedir = os.path.abspath(os.path.join(filedir, '..', '..', 'examples'))
        return basedir
    
    @property
    def _filename(self):
        return 'runfile.py'