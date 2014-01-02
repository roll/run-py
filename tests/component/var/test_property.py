import unittest
from unittest.mock import Mock
from run.var.property import PropertyVar

#Tests

class PropertyVarTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.prop = MockProperty()
        self.var = PropertyVar(self.prop, module=None)

    def test_retrieve(self):
        self.assertEqual(self.var.retrieve(), 'value')
        self.prop.__get__.assert_called_with(None, type(None))

    def test_meta_docstring(self):
        self.assertEqual(self.var.meta_docstring, 'docstring')
        
    
#Fixtures

class MockProperty:
    """docstring"""
    
    __get__ =  Mock(return_value='value')   