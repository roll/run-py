import unittest
from unittest.mock import Mock
from run.attribute.attribute import Attribute

#Tests

class AttributeTest(unittest.TestCase):

    #Public

    def test_with_module_is_none(self):
        module=None
        attribute = MockAttribute(module=module)
        self.assertIsInstance(attribute, Attribute)
        self.assertTrue(repr(attribute))
        self.assertEqual(attribute.meta_module, module)
        attribute.meta_module = module
        self.assertEqual(attribute.meta_module, module)
        self.assertEqual(attribute.meta_type, 'MockAttribute')
        self.assertEqual(attribute.meta_qualname, '')
        self.assertEqual(attribute.meta_name, '')
        self.assertEqual(attribute.meta_info, 'docstring')
        self.assertEqual(attribute.meta_signature, '')
        self.assertEqual(attribute.meta_docstring, 'docstring')
        
    def test_with_module_is_not_main(self):
        module = MockModule()
        attribute = MockAttribute(module=module)
        module.meta_attributes = {'attribute': attribute}
        self.assertEqual(attribute.meta_module, module)
        self.assertEqual(attribute.meta_qualname, 'module.attribute')
        self.assertEqual(attribute.meta_name, 'attribute')
        
    def test_with_module_is_main(self):
        module = MockMainModule()
        attribute = MockAttribute(module=module)
        module.meta_attributes = {'attribute': attribute}
        self.assertEqual(attribute.meta_qualname, '[module] attribute')
    
    def test_with_module_is_none_and_docstring(self):
        module=None
        docstring = 'new_docstring'
        attribute = MockAttribute(module=module, docstring=docstring)
        self.assertEqual(attribute.meta_info, docstring)
        self.assertEqual(attribute.meta_docstring, docstring)
        
    def test_with_module_is_none_and_signature_and_docstring(self):
        module=None
        signature = 'new_signature'
        docstring = 'new_docstring'
        attribute = MockAttribute(
            module=module, signature=signature, docstring=docstring)
        self.assertEqual(attribute.meta_info, signature+'\n'+docstring)
        self.assertEqual(attribute.meta_signature, signature)
        self.assertEqual(attribute.meta_docstring, docstring)     
        
    
#Fixtures

class MockAttribute(Attribute):
    """docstring"""

    #Public

    __get__ = Mock()
    __set__ = Mock()
    
    
class MockModule:

    #Public

    meta_name = 'module'
    meta_is_main_module = False
    meta_attributes = {}
    
    
class MockMainModule(MockModule):

    #Public

    meta_is_main_module = True