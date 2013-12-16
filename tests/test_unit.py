import unittest
from run import UnitName, UnitHelp

class UnitNameTest(unittest.TestCase):

    #Public
        
    def test_full(self):
        unitname = UnitName('namespace', 'attribute')
        self.assertEqual(unitname, 'namespace.attribute')
        self.assertEqual(unitname.namespace, 'namespace')
        self.assertEqual(unitname.attribute, 'attribute')
        
    def test_partial(self):
        unitname = UnitName('', 'attribute')
        self.assertEqual(unitname, 'attribute')
        self.assertEqual(unitname.namespace, '')
        self.assertEqual(unitname.attribute, 'attribute')        
        
        
class UnitNameHelp(unittest.TestCase):

    #Public

    def test_full(self):
        unithelp = UnitHelp('signature', 'docstring')
        self.assertEqual(unithelp, 'signature\ndocstring')
        self.assertEqual(unithelp.signature, 'signature')
        self.assertEqual(unithelp.docstring, 'docstring')
        
    def test_partial(self):
        unithelp = UnitHelp('signature', '')
        self.assertEqual(unithelp, 'signature')
        self.assertEqual(unithelp.signature, 'signature')
        self.assertEqual(unithelp.docstring, '')                                