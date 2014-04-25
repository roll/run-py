import os
import unittest
from subprocess import check_output

class ProgramTest(unittest.TestCase):

    #Public
    
    def test_default(self):
        result = self._execute('-f tasks.py')
        self.assertEqual(
            result,
            'default\n'
            'derived\n' 
            'descriptor\n' 
            'find\n' 
            'function\n' 
            'info\n' 
            'input\n' 
            'list\n' 
            'meta\n' 
            'method\n' 
            'null\n'
            'render\n' 
            'subprocess\n' 
            'value\n')
        
    def test_derived(self):
        result = self._execute('derived')
        self.assertEqual(result, 'Hello World!\n')
        
    def test_descriptor(self):
        result = self._execute('descriptor')
        self.assertEqual(result, 'True\n')
        
    def test_find(self):
        result = self._execute('find')
        self.assertEqual(result, 'find\n')
        
    def test_function(self):
        result = self._execute('function path')
        self.assertRegex(result, '.*examples/path\n')
        
    def test_info(self):
        result = self._execute('info default')
        self.assertRegex(result, 'default.*')
        
    def test_input(self):
        #TODO: implement
        pass
    
    def test_list(self):
        result = self._execute('list')
        self.assertEqual(len(result.splitlines()), 14)
        
    def test_meta(self):
        result = self._execute('meta default')
        self.assertRegex(result, ".*'type': 'NullTask'}\n")                              
        
    #Protected
    
    def _execute(self, command):
        filedir = os.path.dirname(__file__)
        basedir = os.path.abspath(os.path.join(filedir, '..', '..', 'examples'))
        ecommand = 'python3 -c "from run import program; program()" '
        ecommand += '-b {basedir} '.format(basedir=basedir) 
        ecommand += '-f tasks.py '
        ecommand += command
        result = check_output(ecommand, shell=True)
        return result.decode()