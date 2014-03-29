import unittest
from unittest.mock import Mock, ANY
from run.attribute.prototype import AttributePrototype

class AttributePrototypeTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1', 'updates': Mock()}
        self.mock_set = Mock(apply = Mock())
        self.MockAttribute = self._make_mock_attribute_class()
        self.MockPrototype = self._make_mock_prototype_class(
            self.MockAttribute, self.mock_set)
        self.prototype = self.MockPrototype(
            self.MockAttribute, *self.args, **self.kwargs)
    
    def test___getattr__(self):
        self.assertEqual(self.prototype.attr1, 'value1') 
        
    def test___getattr___no_attribute(self):
        self.assertRaises(AttributeError, getattr, self.prototype, 'attr3')         
           
    def test___setattr__(self):
        self.prototype.attr2 = 'value2'
        self.prototype._set_class.assert_called_with('attr2', 'value2')
        self.kwargs['updates'].append.assert_called_with(self.mock_set)

    def test___call__(self):
        self.prototype.attr2 = 'value2'
        obj = self.prototype()
        self.assertIsInstance(obj, self.MockAttribute)
        #obj.__meta_build__.assert_called_with(ANY, *self.args, **self.kwargs)
        obj.__meta_init__.assert_called_with(None)
        
    def test_meta_prototype(self):
        self.assertEqual(
            self.prototype.meta_prototype, 
            self.prototype)
          
    #Protected
    
    def _make_mock_prototype_class(self, MockAttribute, mock_set):
        class MockPrototype(AttributePrototype): 
            #Protected
            _set_class = Mock(return_value=mock_set)
        return MockPrototype
    
    def _make_mock_attribute_class(self):
        class MockAttribute:
            #Public
            __meta_build__ = Mock()
            __meta_init__ = Mock()
            attr1 = 'value1' 
        return MockAttribute    