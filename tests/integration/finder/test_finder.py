import os
import unittest
from run.finder import Finder

class FinderTest(unittest.TestCase):

    #Public
    
    def test_find(self):
        finder = Finder()
        modules = list(finder.find(
            'runfile.py', basedir=self._basedir))
        self.assertEqual(len(modules), 3)
        self.assertEqual(modules[0].__name__, 'Module1')
           
    def test_find_recursively(self):
        finder = Finder()
        modules = list(finder.find(
            'runfile.py', basedir=self._basedir, recursively=True))
        self.assertEqual(len(modules), 3)
        self.assertEqual(modules[0].__name__, 'Module1')
        self.assertEqual(modules[1].__name__, 'Module2')
        self.assertEqual(modules[2].__name__, 'Module3')
    
    def test_find_with_names(self):
        finder = Finder(names=['name1'])
        modules = list(finder.find(
            'runfile.py', basedir=self._basedir, recursively=True))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module1')

    def test_find_with_tags(self):
        finder = Finder(tags=['tag2'])
        modules = list(finder.find(
            'runfile.py', basedir=self._basedir, recursively=True))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module2')
        
    #Protected
    
    @property
    def _basedir(self):
        return os.path.join(os.path.dirname(__file__), 'fixtures')  