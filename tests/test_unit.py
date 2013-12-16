import unittest
from run import UnitName, UnitHelp

class UnitNameTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.unitname = UnitName('namespace', 'attribute')
        
    def test_name(self):
        self.assertEqual(self.unitname, 'namespace.attribute')
        
    def test_namespace(self):
        self.assertEqual(self.unitname.namespace, 'namespace')
        
    def test_attribute(self):
        self.assertEqual(self.unitname.attribute, 'attribute')
        
        
class UnitNameHelp(unittest.TestCase):

    #Public

    def setUp(self):
        self.unithelp = UnitHelp('signature', 'docstring')
        
    def test_help(self):
        self.assertEqual(self.unithelp, 'signature\ndocstring')
        
    def test_signature(self):
        self.assertEqual(self.unithelp.signature, 'signature')
        
    def test_docstring(self):
        self.assertEqual(self.unithelp.docstring, 'docstring')                        