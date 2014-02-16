import os
import unittest
from box.findtools import find_objects
from run import version

class SetupTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.basedir = self._get_repository_path()

    def test(self):
        package = find_objects(
            objname='package', 
            filename='setup.py', 
            basedir=self.basedir, 
            maxdepth=1,
            getfirst=True)
        self.assertEqual(package['name'], 'runpack')
        self.assertEqual(package['version'], version)
        
    #Protected
    
    def _get_repository_path(self, *args):
        return os.path.join(os.path.dirname(__file__), '..', '..')