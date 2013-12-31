import unittest
from unittest.mock import Mock
from run.dependent.builder import DependentAttributeBuilder

#Tests

class DependentAttributeBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.builder = MockDependentAttributeBuilder(None)
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}

    def test_require(self):
        self.builder.require(*self.args, **self.kwargs)
        self.builder._call_class.assert_called_with(
            'require', *self.args, **self.kwargs)
        
    def test_trigger(self):
        self.builder.trigger(*self.args, **self.kwargs)
        self.builder._call_class.assert_called_with(
            'trigger', *self.args, **self.kwargs)        
    
    
#Fixtures

class MockDependentAttributeBuilder(DependentAttributeBuilder):
    
    #Protected
    
    _call_class = Mock()   