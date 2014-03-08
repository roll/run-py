import unittest
from unittest.mock import Mock
from run.attribute.draft import AttributeDraft

class AttributeBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.mock_set = Mock(apply = Mock())
        self.MockAttribute = Mock(attr1='value1', spec_set=['attr1'])
        self.MockDraft = self._make_mock_draft_class(
            self.MockAttribute, self.mock_set)
        self.draft = self.MockDraft(
            self.MockAttribute, *self.args, **self.kwargs)
    
    def test(self):
        self.draft._builder_class.assert_called_with(
            self.MockAttribute, *self.args, **self.kwargs)
    
    def test___getattr__(self):
        self.assertEqual(self.draft.attr1, 'value1') 
        
    def test___getattr___no_attribute(self):
        self.assertRaises(AttributeError, getattr, self.draft, 'attr3')         
           
    def test___setattr__(self):
        self.draft.attr2 = 'value2'
        self.draft._set_class.assert_called_with('attr2', 'value2')
        (self.draft._builder_class.return_value.updates.append.
             assert_called_with(self.mock_set))
        
    def test_meta_builder(self):
        self.assertEqual(
            self.draft.meta_builder, 
            self.draft._builder_class.return_value)
        
    #Protected
    
    def _make_mock_draft_class(self, MockAttribute, mock_set):
        class MockBuilder: 
            #Public
            cls = MockAttribute
            updates = Mock()
        class MockDraft(AttributeDraft): 
            #Protected
            _builder_class = Mock(return_value=MockBuilder)
            _set_class = Mock(return_value=mock_set)
        return MockDraft