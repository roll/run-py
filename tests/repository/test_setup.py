import os
import unittest
from box.findtools import find_objects
from run import version

class SetupTest(unittest.TestCase):

    #Public

    def test(self):
        package = find_objects(
            objname='package', 
            filename='setup.py', 
            basedir=self._basedir, 
            maxdepth=1,
            getfirst=True)
        self.assertEqual(package['name'], 'runpack')
        self.assertEqual(package['version'], version)
        
    #Protected
    
    @property
    def _basedir(self, *args):
        return os.path.join(os.path.dirname(__file__), '..', '..')