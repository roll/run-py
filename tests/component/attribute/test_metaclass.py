import unittest
from abc import ABCMeta
from unittest.mock import Mock
from run.attribute.attribute import AttributeMetaclass

class AttributeMetaclassTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.MockPrototype = Mock(return_value=Mock())
        self.MockMetaclass = self._make_mock_metaclass(self.MockPrototype)
        self.MockClass = self._make_mock_class(self.MockMetaclass)

    def test(self):
        self.assertTrue(issubclass(self.MockMetaclass, ABCMeta))

    def test___call__(self):
        instance = self.MockClass(*self.args, **self.kwargs)
        self.assertIsInstance(instance, Mock)
        self.MockPrototype.assert_called_with(
            self.MockClass, None, *self.args, **self.kwargs)
        self.assertFalse(self.MockPrototype.return_value.called)
    
    def test___call___with_module(self):
        instance = self.MockClass(module='module')
        self.assertIsInstance(instance, Mock)
        self.MockPrototype.assert_called_with(self.MockClass, None)
        self.MockPrototype.return_value.assert_called_with('module')
        
    #Protected
    
    def _make_mock_metaclass(self, mock_prototype_class):
        class MockMetaclass(AttributeMetaclass):
            #Protected
            _prototype_class = mock_prototype_class
        return MockMetaclass
    
    def _make_mock_class(self, mock_metaclass):
            class MockClass(metaclass=mock_metaclass): pass
            return MockClass