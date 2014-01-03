import unittest
from run.stack import Stack

#Tests

class StackTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.stack = Stack()
    
    def test_push(self):
        self.stack.push('attribute')
        self.assertEqual(self.stack, ['attribute'])

    def test_pop(self):
        self.stack.push('attribute')
        self.assertEqual(self.stack.pop(), 'attribute')
        self.assertFalse(self.stack)
        
    def test_formatted_0_attributes(self):
        self.assertEqual(self.stack.formatted, '')
        
    def test_formatted_1_attributes(self):
        self.stack.push(MockAttribute1())
        self.assertEqual(self.stack.formatted, 'module1.attribute1')
        
    def test_formatted_attributes_with_same_modules(self):
        self.stack.push(MockAttribute1())
        self.stack.push(MockAttribute1())
        self.assertEqual(self.stack.formatted, 
                         'module1.attribute1/attribute1')
        
    def test_formatted_attributes_with_different_modules(self):
        self.stack.push(MockAttribute1())
        self.stack.push(MockAttribute2())
        self.assertEqual(self.stack.formatted, 
                         'module1.attribute1/module2.attribute2')                 
        
        
#Fixtures

class MockAttribute1:
    
    meta_module = 'module1'
    meta_name = 'attribute1'
    meta_qualname = 'module1.attribute1'
    
    
class MockAttribute2:
    
    meta_module = 'module2'
    meta_name = 'attribute2'
    meta_qualname = 'module2.attribute2'    