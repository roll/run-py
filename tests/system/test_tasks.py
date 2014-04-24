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
        Program(['run', '-f', 'tasks.py'])()
        result = self.stdout.getvalue()
        self.assertEqual(
            result.splitlines(), 
            ['default',
             'derived', 
             'descriptor', 
             'find', 
             'function', 
             'info', 
             'input', 
             'list', 
             'meta', 
             'method', 
             'null',
             'render', 
             'subprocess', 
             'value'])
        
    #Protected
    
    def _get_exampes_path(self, *args):
        return os.path.join(
            os.path.dirname(__file__), '..', '..', 'examples', *args)