import unittest
from unittest.mock import Mock
from run.attribute.builder import AttributeBuilder

#Tests

class AttributeBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.args = ('arg1', 'arg2')
        self.kwargs = {'kwarg1': 'kwarg1', 'kwarg2': 'kwarg2'}
        self.builder = AttributeBuilder(
            MockAttribute, *self.args, **self.kwargs)

    def test___call__(self):
        for _ in [1, 2]:
            obj = self.builder()
            self.assertIsInstance(obj, MockAttribute)
            obj.__init__.assert_called_with('arg1', kwarg1='kwarg1')
    

#Fixtures

class MockAttribute:

    #Public

    __init__ = Mock(return_value=None)
    
    @staticmethod
    def __meta_init__(args, kwargs):
        args.pop(1)
        kwargs.pop('kwarg2')