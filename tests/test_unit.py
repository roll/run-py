import unittest
from run import UnitName

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