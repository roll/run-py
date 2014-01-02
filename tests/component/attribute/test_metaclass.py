import unittest
from abc import ABCMeta
from unittest.mock import Mock, MagicMock
from run.attribute.attribute import AttributeMetaclass

#Tests

class AttributeMetaclassTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.metaclass = MockAttributeMetaclass

    def test(self):
        self.assertTrue(issubclass(self.metaclass, ABCMeta))

    def test___call__(self):
        args = ('arg1',)
        kwargs = {'kwarg1': 'kwarg1'}
        attribute = MockAtrtibute(*args, **kwargs)
        self.assertIsInstance(attribute, Mock)
        (self.metaclass._builder_class.
            assert_called_with(MockAtrtibute, *args, **kwargs))
        self.assertFalse(self.metaclass._builder_class.return_value.called)
    
    def test___call___with_module(self):
        attribute = MockAtrtibute(module='module')
        self.assertIsInstance(attribute, MagicMock)
        (self.metaclass._builder_class.
            assert_called_with(MockAtrtibute, module='module'))
        self.metaclass._builder_class.return_value.assert_called_with()    
    
    
#Fixtures

class MockAttributeMetaclass(AttributeMetaclass):

    #Protected

    _builder_class = Mock(return_value=Mock(return_value=MagicMock()))
    
    
class MockAtrtibute(metaclass=MockAttributeMetaclass): pass