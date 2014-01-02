import unittest
from unittest.mock import Mock
from run.module.module import Module

#Tests

class ModuleTest(unittest.TestCase):

    #Public

    #TODO: split for small tests?
    def test_with_module_is_none(self):
        module = MockModule(module=None)
        self.assertIs(module.__get__(None), module)
        self.assertRaises(AttributeError, module.__set__, None, 'value')
        self.assertEqual(getattr(module, '__getattr__.__doc__'), None)
        self.assertRaises(AttributeError, getattr, module, 'no_attr')
        self.assertEqual(module.meta_name, '__main__')
        self.assertIs(module.meta_main_module, module)
        self.assertTrue(module.meta_is_main_module)
        self.assertEqual(module.meta_tags, [])
        self.assertEqual(len(module.meta_attributes), 5)
        module.list()
        module.info()
        module.meta()
        
    def test_with_module(self):
        pass        
    
    
#Fixtures

class MockModule(Module):

    #Public

    attr1 = 'value1'
    
    #Protected
    
    _meta_formatted_print_operator = Mock()
    _meta_print_operator = Mock()