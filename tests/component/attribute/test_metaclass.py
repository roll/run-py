import unittest
from abc import ABCMeta
from unittest.mock import Mock, MagicMock
from run.attribute.attribute import AttributeMetaclass

class AttributeMetaclassTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.MockAttributeMetaclass = self._make_mock_attribute_metaclass()
        self.MockAttribute = self._make_mock_attribute_class(
            self.MockAttributeMetaclass)

    def test(self):
        self.assertTrue(issubclass(self.MockAttributeMetaclass, ABCMeta))

    def test___call__(self):
        args = ('arg1',)
        kwargs = {'kwarg1': 'kwarg1'}
        attribute = self.MockAttribute(*args, **kwargs)
        self.assertIsInstance(attribute, Mock)
        (self.MockAttributeMetaclass._draft_class.
            assert_called_with(self.MockAttribute, *args, **kwargs))
        (self.assertFalse(self.MockAttributeMetaclass._draft_class.
            return_value.called))
    
    def test___call___with_module(self):
        attribute = self.MockAttribute(module='module')
        self.assertIsInstance(attribute, MagicMock)
        (self.MockAttributeMetaclass._draft_class.
            assert_called_with(self.MockAttribute, module='module'))
        (self.MockAttributeMetaclass._draft_class.
            return_value.meta_builder.build.assert_called_with())
        
    #Protected
    
    def _make_mock_attribute_metaclass(self):
        class MockAttributeMetaclass(AttributeMetaclass):
            #Protected
            _draft_class = Mock(return_value=Mock(
                meta_builder=Mock(build=MagicMock())))
        return MockAttributeMetaclass
    
    def _make_mock_attribute_class(self, mock_attribute_metaclass):
            class MockAtrtibute(metaclass=mock_attribute_metaclass): pass
            return MockAtrtibute