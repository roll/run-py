import unittest
from run.attribute.update import AttributeBuilderSet, AttributeBuilderCall

#Tests

class AttributeBuilderSetTest(unittest.TestCase):

    #Public

    def test(self):
        update = AttributeBuilderSet('name', 'value')
        obj = MockObject()
        update.apply(obj)
        self.assertEqual(obj.name, 'value')
      

class AttributeBuilderCallTest(unittest.TestCase):

    #Public

    def test(self):
        update = AttributeBuilderCall('method', 'value')
        obj = MockObject()
        update.apply(obj)
        self.assertEqual(obj.name, 'value')
        
        
#Fixtures

class MockObject:

    #Public
    
    def method(self, value):
        self.name = value