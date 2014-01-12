import os
import unittest
from run.finder import Finder

class FinderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.basedir = self._get_fixtures_path()
        
    def test_find(self):
        finder = Finder()
        modules = list(finder.find('runfile.py', self.basedir, True))
        self.assertEqual(len(modules), 3)
        self.assertEqual(modules[0].__name__, 'Module1')
        self.assertEqual(modules[1].__name__, 'Module2')
        self.assertEqual(modules[2].__name__, 'Module3')
    
    def test_find_with_names(self):
        finder = Finder(names=['name1'])
        modules = list(finder.find('runfile.py', self.basedir, True))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module1')

    def test_find_with_tags(self):
        finder = Finder(tags=['tag2'])
        modules = list(finder.find('runfile.py', self.basedir, True))
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0].__name__, 'Module2')
        
    #Protected
    
    def _get_fixtures_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)  