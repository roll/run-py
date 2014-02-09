import unittest
from unittest.mock import Mock, call
from run.attribute.builder import AttributeBuilder

class AttributeBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.mock_set = Mock(apply = Mock())
        MockBuilder = self._make_mock_builder_class(self.mock_set)
        self.MockAttribute = self._make_mock_attribute_class()
        self.builder = MockBuilder(self.MockAttribute, *self.args, **self.kwargs)

    def test___call__(self):
        self.builder.attr2 = 'value2'
        obj = self.builder()
        self.assertIsInstance(obj, self.MockAttribute)
        obj.__meta_build__.assert_called_with(
            self.builder, [self.mock_set], 'arg1', kwarg1='kwarg1')
        obj.__meta_bind__.assert_called_with(None)
        obj.__meta_init__.assert_called_with()
        obj.__meta_update__.assert_called_with()
        obj.__meta_ready__.assert_called_with()
    
    def test___getattr__(self):
        self.assertEqual(self.builder.attr1, 'value1') 
        
    def test___getattr___no_attribute(self):
        self.assertRaises(AttributeError, getattr, self.builder, 'attr3')         
           
    def test___setattr__(self):
        self.builder.attr2 = 'value2'
        self.builder._set_class.assert_called_with('attr2', 'value2')
        
    #Protected
    
    def _make_mock_attribute_class(self):
        class MockAttribute:
            #Public
            __meta_build__ = Mock()
            __meta_bind__ = Mock()
            __meta_init__ = Mock()
            __meta_update__ = Mock()
            __meta_ready__ = Mock()
            attr1 = 'value1' 
        return MockAttribute
    
    def _make_mock_builder_class(self, mock_set):             
        class MockBuilder(AttributeBuilder): 
            #Protected
            _set_class = Mock(return_value=mock_set)
        return MockBuilder