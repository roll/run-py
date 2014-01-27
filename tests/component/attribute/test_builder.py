import unittest
from unittest.mock import Mock, call
from run.attribute.builder import AttributeBuilder

class AttributeBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1', 'arg2')
        self.kwargs = {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2'}
        self.mock_set = Mock(apply = Mock())
        MockBuilder = self._make_mock_builder_class(self.mock_set)
        self.MockAttribute = self._make_mock_attribute_class()
        self.builder = MockBuilder(self.MockAttribute, *self.args, **self.kwargs)

    def test___call__(self):
        self.builder.attr2 = 'value2'
        obj1 = self.builder()
        obj2 = self.builder()
        self.assertIsInstance(obj1, self.MockAttribute)
        self.assertIsInstance(obj2, self.MockAttribute)
        obj1.__init__.assert_called_with('arg1', kwarg1='kwarg1')
        obj2.__init__.assert_called_with('arg1', kwarg1='kwarg1')
        self.mock_set.apply.assert_has_calls([call(obj1), call(obj2)])
    
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
            __init__ = Mock(return_value=None)
            attr1 = 'value1' 
            def __meta_init__(self, builder, args, kwargs):
                args.remove('arg2')
                kwargs.pop('kwarg2')
        return MockAttribute
    
    def _make_mock_builder_class(self, mock_set):             
        class MockBuilder(AttributeBuilder): 
            #Protected
            _set_class = Mock(return_value=mock_set)
        return MockBuilder