import unittest
from unittest.mock import Mock, ANY
from run.attribute.draft import AttributeDraft

class AttributeBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1', 'updates': Mock()}
        self.mock_set = Mock(apply = Mock())
        self.MockAttribute = self._make_mock_attribute_class()
        self.MockDraft = self._make_mock_draft_class(
            self.MockAttribute, self.mock_set)
        self.draft = self.MockDraft(
            self.MockAttribute, *self.args, **self.kwargs)
    
    def test___getattr__(self):
        self.assertEqual(self.draft.attr1, 'value1') 
        
    def test___getattr___no_attribute(self):
        self.assertRaises(AttributeError, getattr, self.draft, 'attr3')         
           
    def test___setattr__(self):
        self.draft.attr2 = 'value2'
        self.draft._set_class.assert_called_with('attr2', 'value2')
        self.kwargs['updates'].append.assert_called_with(self.mock_set)

    def test___call__(self):
        self.draft.attr2 = 'value2'
        obj = self.draft()
        self.assertIsInstance(obj, self.MockAttribute)
        obj.__meta_build__.assert_called_with(ANY, 'arg1', kwarg1='kwarg1')
        obj.__meta_init__.assert_called_with(None)
        
    def test_meta_draft(self):
        self.assertEqual(
            self.draft.meta_draft, 
            self.draft)
          
    #Protected
    
    def _make_mock_draft_class(self, MockAttribute, mock_set):
        class MockDraft(AttributeDraft): 
            #Protected
            _set_class = Mock(return_value=mock_set)
        return MockDraft
    
    def _make_mock_attribute_class(self):
        class MockAttribute:
            #Public
            __meta_build__ = Mock()
            __meta_init__ = Mock()
            attr1 = 'value1' 
        return MockAttribute    