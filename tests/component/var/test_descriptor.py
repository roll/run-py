import unittest
from unittest.mock import Mock
from run.var.descriptor import DescriptorVar

#Tests

class PropertyVarTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.descriptor = MockDescriptor()
        self.var = DescriptorVar(self.descriptor, module=None)

    def test_retrieve(self):
        self.assertEqual(self.var.retrieve(), 'value')
        self.descriptor.__get__.assert_called_with(
            self.var.meta_module, type(self.var.meta_module))

    def test_meta_docstring(self):
        self.assertEqual(self.var.meta_docstring, 'docstring')
        
    
#Fixtures

class MockDescriptor:
    """docstring"""
    
    __get__ =  Mock(return_value='value')   