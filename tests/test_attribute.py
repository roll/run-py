import unittest
from run import AttributeName, AttributeHelp

class UnitNameTest(unittest.TestCase):

    #Public
        
    def test_full(self):
        attrname = AttributeName('module', 'attribute')
        self.assertEqual(attrname, 'module.attribute')
        self.assertEqual(attrname.module, 'module')
        self.assertEqual(attrname.attribute, 'attribute')
        
    def test_partial(self):
        attrname = AttributeName(attribute='attribute')
        self.assertEqual(attrname, 'attribute')
        self.assertEqual(attrname.module, '')
        self.assertEqual(attrname.attribute, 'attribute')        
        
        
class UnitNameHelp(unittest.TestCase):

    #Public

    def test_full(self):
        attrhelp = AttributeHelp('signature', 'docstring')
        self.assertEqual(attrhelp, 'signature\ndocstring')
        self.assertEqual(attrhelp.signature, 'signature')
        self.assertEqual(attrhelp.docstring, 'docstring')
        
    def test_partial(self):
        attrhelp = AttributeHelp(signature='signature')
        self.assertEqual(attrhelp, 'signature')
        self.assertEqual(attrhelp.signature, 'signature')
        self.assertEqual(attrhelp.docstring, '')                                