import unittest
from subprocess import check_output

class ProgramTest(unittest.TestCase):

    #Public
    
    def test_default(self):
        self.assertEqual(
            self._execute('-f tasks.py'),
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
        self.assertEqual(self._execute('derived'), 'Hello World!\n')
        
    def test_descriptor(self):
        self.assertEqual(self._execute('descriptor'), 'True\n')
        
    def test_find(self):
        self.assertEqual(self._execute('find'), 'find\n')
        
    def test_function(self):
        self.assertRegex(self._execute('function path'), '.*examples/path\n')
        
    def test_info(self):
        self.assertRegex(self._execute('info default'), 'default.*')
        
    def test_input(self):
        #TODO: implement
        pass
    
    def test_list(self):
        result = self._execute('list')
        self.assertEqual(len(result.splitlines()), 14)                                 
        
    #Protected
    
    def _execute(self, command):
        ecommand = 'cd ../../examples; '
        ecommand += 'python3 -c "from run import program; program()" '
        ecommand += '-f tasks.py '
        ecommand += command
        result = check_output(ecommand, shell=True)
        return result.decode()