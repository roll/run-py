import unittest
from unittest.mock import Mock
from run.stack import Stack

#Tests

class StackTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.stack = Stack()
        self.attribute1 = Mock(
            meta_module='module1',
            meta_name='attribute1',
            meta_qualname='module1.attribute1')
        self.attribute2 = Mock(
            meta_module='module2',
            meta_name='attribute2',
            meta_qualname='module2.attribute2')        
    
    def test_push(self):
        self.stack.push('attribute')
        self.assertEqual(self.stack, ['attribute'])

    def test_pop(self):
        self.stack.push('attribute')
        self.assertEqual(self.stack.pop(), 'attribute')
        self.assertFalse(self.stack)
        
    def test___str___0_attributes(self):
        self.assertEqual(str(self.stack), '')
        
    def test___str___1_attributes(self):
        self.stack.push(self.attribute1)
        self.assertEqual(str(self.stack), 'module1.attribute1')
        
    def test___str___attributes_with_same_modules(self):
        self.stack.push(self.attribute1)
        self.stack.push(self.attribute1)
        self.assertEqual(str(self.stack), 
                         'module1.attribute1/attribute1')
        
    def test___str___attributes_with_different_modules(self):
        self.stack.push(self.attribute1)
        self.stack.push(self.attribute2)
        self.assertEqual(str(self.stack), 
                         'module1.attribute1/module2.attribute2')                    