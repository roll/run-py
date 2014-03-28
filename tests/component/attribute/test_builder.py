import unittest
from unittest.mock import Mock, ANY
from run.attribute.builder import AttributeBuilder

class AttributeBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.mock_set = Mock(apply = Mock())
        self.MockAttribute = self._make_mock_attribute_class()
        self.builder = AttributeBuilder(
            self.MockAttribute, *self.args, **self.kwargs)

    def test_build(self):
        self.builder.attr2 = 'value2'
        obj = self.builder.build()
        self.assertIsInstance(obj, self.MockAttribute)
        obj.__meta_build__.assert_called_with(ANY)
        obj.__meta_bind__.assert_called_with(None)
        obj.__meta_init__.assert_called_with()
        obj.__meta_update__.assert_called_with()
        
    def test_args(self):
        self.assertEqual(self.builder.args, list(self.args))
        
    def test_kwargs(self):
        self.assertEqual(self.builder.kwargs, self.kwargs)
         
    #Protected
    
    def _make_mock_attribute_class(self):
        class MockAttribute:
            #Public
            __meta_build__ = Mock()
            __meta_bind__ = Mock()
            __meta_init__ = Mock()
            __meta_update__ = Mock()
            attr1 = 'value1' 
        return MockAttribute