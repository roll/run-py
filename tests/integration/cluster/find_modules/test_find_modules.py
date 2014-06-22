import os
import unittest
from io import StringIO
from functools import partial
from unittest.mock import patch
from run.cluster import find_files, find_modules

class find_Test(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.stdout = patch('sys.stdout', new_callable=StringIO).start()
        self.addCleanup(patch.stopall)
        self.pfind_files = partial(find_files, basedir=self._basedir)
        self.pfind_modules = partial(find_modules, basedir=self._basedir)
    
    def test_find(self):
        files = list(self.pfind_files(file='runfile.py'))
        modules = list(self.pfind_modules(files=files))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module1')
        self.assertEqual(
            self.stdout.getvalue(), 
            'Hits runfile.py\n')
           
    def test_find_recursively(self):
        files = list(self.pfind_files(file='runfile.py', recursively=True))
        modules = list(self.pfind_modules(files=files))
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
        files = list(self.pfind_files(file='runfile.py', recursively=True))
        modules = list(self.pfind_modules(names=['name1'], files=files))        
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module1')

    def test_find_with_tags(self):
        files = list(self.pfind_files(file='runfile.py', recursively=True))
        modules = list(self.pfind_modules(tags=['tag2'], files=files))        
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module2')
        
    #Protected
    
    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')  