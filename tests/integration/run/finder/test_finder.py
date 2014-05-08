import os
import unittest
from io import StringIO
from unittest.mock import patch
from run.run.finder import RunFinder

class FinderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.stdout = self.patcher.start()
        self.addCleanup(patch.stopall)    
    
    def test_find(self):
        finder = RunFinder()
        modules = list(finder.find(
            'runfile.py', basedir=self._basedir))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module1')
        self.assertEqual(
            self.stdout.getvalue(), 
            'Hits runfile.py\n')
           
    def test_find_recursively(self):
        finder = RunFinder()
        modules = list(finder.find(
            'runfile.py', basedir=self._basedir, recursively=True))
        self.assertEqual(len(modules), 3)
        self.assertEqual(modules[0].__name__, 'Module1')
        self.assertEqual(modules[1].__name__, 'Module2')
        self.assertEqual(modules[2].__name__, 'Module3')
        self.assertEqual(
            self.stdout.getvalue(),
            'Hits runfile.py\n'
            'Hits dir/runfile.py\n'
            'Hits dir/subdir/runfile.py\n')
    
    def test_find_with_names(self):
        finder = RunFinder(names=['name1'])
        modules = list(finder.find(
            'runfile.py', basedir=self._basedir, recursively=True))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module1')

    def test_find_with_tags(self):
        finder = RunFinder(tags=['tag2'])
        modules = list(finder.find(
            'runfile.py', basedir=self._basedir, recursively=True))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module2')
        
    #Protected
    
    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')  