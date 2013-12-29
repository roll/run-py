import unittest
from unittest.mock import Mock
from run.var.property import PropertyVar

#Tests

class PropertyVarTest(unittest.TestCase):

    #Public

    def test(self):
        prop = MockProperty()
        var = PropertyVar(prop, module=None)
        self.assertEqual(var.meta_docstring, 'docstring')
        self.assertEqual(var.retrieve(), 'value')
        prop.__get__.assert_called_with(None, type(None))
        
    
#Fixtures

class MockProperty:
    """docstring"""
    
    __get__ =  Mock(return_value='value')
    