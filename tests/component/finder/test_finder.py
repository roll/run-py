import os
import unittest
from run import Finder

class FinderTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.finder = Finder()
        self.path = self._get_path()
        
    def test__find_files(self):
        files = self.finder._find_files(self.path, names=['runfile.py'])
        self.assertEqual(len(files), 2)
        self.assertEqual(files[0], self._get_path('runfile.py'))
        self.assertEqual(files[1], self._get_path('folder', 'runfile.py')) 
        
    #Protected
    
    def _get_path(self, *args):
        return os.path.join(os.path.dirname(__file__), 'fixtures', *args)         