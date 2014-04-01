import unittest
from unittest.mock import Mock
from run.attribute.prototype import AttributePrototype

class AttributePrototypeTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.updates = []
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.MockAttribute = self._make_mock_attribute_class()
        self.MockPrototype = self._make_mock_prototype_class()
        self.prototype = self.MockPrototype(
            self.MockAttribute, self.updates, *self.args, **self.kwargs)
    
    def test___getattr__(self):
        self.assertEqual(self.prototype.attr1, 'value1') 
        
    def test___getattr___no_attribute(self):
        self.assertRaises(AttributeError, getattr, self.prototype, 'attr3')         
           
    def test___setattr__(self):
        self.prototype.attr2 = 'value2'
        self.prototype._set_class.assert_called_with('attr2', 'value2')
        self.assertEqual(self.updates, [self.prototype._set_class.return_value])

    def test___call__(self):
        self.prototype.attr2 = 'value2'
        attribute = self.prototype('module')
        self.assertIsInstance(attribute, self.MockAttribute)
        (attribute.__meta_init__.
            assert_called_with('module', *self.args, **self.kwargs))
        (self.prototype._set_class.return_value.apply.
            assert_called_with(attribute))
          
    #Protected
    
    def _make_mock_attribute_class(self):
        class MockAttribute:
            #Public
            __meta_init__ = Mock()
            attr1 = 'value1' 
        return MockAttribute  
    
    def _make_mock_prototype_class(self):
        class MockPrototype(AttributePrototype): 
            #Protected
            _set_class = Mock(return_value=Mock(apply = Mock()))
        return MockPrototype  