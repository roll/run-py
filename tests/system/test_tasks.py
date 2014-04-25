import os
import unittest
from unittest.mock import patch
from io import StringIO
from run import Program

class ProgramTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        os.chdir(self._get_exampes_path())
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.stdout = self.patcher.start()
        self.addCleanup(patch.stopall)
    
    def test_default(self):
        result = self._run_program(['run', '-f', 'tasks.py'])
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
        
    def test_descriptor(self):
        result = self._run_program(['run', '-f', 'tasks.py', 'descriptor'])
        self.assertEqual(result, 'True\n')
        
    def test_find(self):
        result = self._run_program(['run', '-f', 'tasks.py', 'find'])
        self.assertEqual(result, 'find\n')        
        
    #Protected
    
    def _get_exampes_path(self, *args):
        return os.path.join(
            os.path.dirname(__file__), '..', '..', 'examples', *args)
        
    def _run_program(self, argv):
        program=Program(argv)
        program()
        return self.stdout.getvalue()