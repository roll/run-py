import unittest
from unittest.mock import Mock
from run.attribute.attribute import Attribute

#Tests

class AttributeTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.attribute = MockAttribute(module=None)

    def test(self):
        self.assertIsInstance( self.attribute, Attribute)
   
    def test___repr__(self):
        self.assertTrue(repr( self.attribute))  
    
    def test_meta_basedir(self):
        self.assertEqual(self.attribute.meta_basedir,
                         self.attribute.meta_module.meta_basedir)     
    
    def test_meta_dispatcher(self):
        self.assertEqual(self.attribute.meta_dispatcher,
                         self.attribute.meta_module.meta_dispatcher)     
    
    def test_meta_docstring(self):
        self.assertEqual(self.attribute.meta_docstring, 'docstring') 
        
    def test_meta_info(self):
        self.assertEqual(self.attribute.meta_info, 'docstring')
        
    def test_meta_is_bound(self):
        self.assertEqual(self.attribute.meta_is_bound, False)        
           
    def test_meta_module(self):
        #Null module
        self.assertNotEqual(self.attribute.meta_module, None)
        self.assertFalse(self.attribute.meta_module)
        
    def test_meta_module_setter(self):
        self.attribute.meta_module = 'module'
        self.assertEqual(self.attribute.meta_module, 'module')    
    
    def test_meta_name(self):
        self.assertEqual(self.attribute.meta_name, '')       
           
    def test_meta_qualname(self):
        self.assertEqual(self.attribute.meta_qualname, '') 
    
    def test_meta_signature(self):
        self.assertEqual(self.attribute.meta_signature, '')
    
    def test_meta_type(self):
        self.assertEqual(self.attribute.meta_type, 'MockAttribute')
        
        
class AttributeTest_with_module(AttributeTest):
    
    #Public
    
    def setUp(self):
        self.module = MockModule()
        self.attribute = MockAttribute(module=self.module)
        self.module.meta_attributes = {'attribute': self.attribute}
        
    def test_meta_info(self):
        self.assertEqual(self.attribute.meta_info, 
                         'module.attribute'+'\n'+'docstring') 
        
    def test_meta_is_bound(self):
        self.assertEqual(self.attribute.meta_is_bound, True)  
        
    def test_meta_module(self):
        self.assertEqual(self.attribute.meta_module, self.module)
        
    def test_meta_module_setter(self):
        self.assertRaises(AttributeError, 
            setattr, self.attribute, 'meta_module', 'value')
    
    def test_meta_name(self):
        self.assertEqual(self.attribute.meta_name, 'attribute')
        
    def test_meta_qualname(self):
        self.assertEqual(self.attribute.meta_qualname, 'module.attribute') 
         
    def test_meta_signature(self):
        self.assertEqual(self.attribute.meta_signature, 'module.attribute')
        
        
class AttributeTest_with_module_is_main(AttributeTest_with_module):
    
    #Public
    
    def setUp(self):
        self.module = MockMainModule()
        self.attribute = MockAttribute(module=self.module)
        self.module.meta_attributes = {'attribute': self.attribute}
          
    def test_meta_info(self):
        self.assertEqual(self.attribute.meta_info, 
                         '[module] attribute'+'\n'+'docstring')
        
    def test_meta_qualname(self):
        self.assertEqual(self.attribute.meta_qualname, '[module] attribute')
          
    def test_meta_signature(self):
        self.assertEqual(self.attribute.meta_signature, '[module] attribute')           


class AttributeTest_with_docstring(AttributeTest):
    
    #Public
    
    def setUp(self):
        self.docstring = 'new_docstring'
        self.attribute = MockAttribute(module=None, docstring=self.docstring)
    
    def test_meta_docstring(self):
        self.assertEqual(self.attribute.meta_docstring, self.docstring)
        
    def test_meta_info(self):
        self.assertEqual(self.attribute.meta_info, self.docstring)
        
        
class AttributeTest_with_signature_and_docstring(AttributeTest_with_docstring):
    
    #Public
    
    def setUp(self):
        self.docstring = 'new_docstring'
        self.signature = 'new_signature'
        self.attribute = MockAttribute(
            module=None, docstring=self.docstring, signature=self.signature)

    def test_meta_info(self):
        self.assertEqual(self.attribute.meta_info, 
                         self.signature+'\n'+self.docstring)
    
    def test_meta_signature(self):
        self.assertEqual(self.attribute.meta_signature, self.signature)
             
    
#Fixtures

class MockAttribute(Attribute):
    """docstring"""

    #Public

    __get__ = Mock()
    __set__ = Mock()
    
    
class MockModule:

    #Public

    meta_attributes = {}
    meta_basedir = 'basedir'
    meta_dispatcher = 'dispatcher'
    meta_is_main_module = False    
    meta_name = 'module'
    
    
class MockMainModule(MockModule):

    #Public

    meta_is_main_module = True