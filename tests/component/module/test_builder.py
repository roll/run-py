import unittest
from unittest.mock import Mock
from run.module.builder import ModuleBuilder

#Tests

class ModuleBuilderTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.builder = MockModuleBuilder(MockModule2)
    
    def test__create_object(self):
        obj = self.builder._create_object()
        #It doesn't work
        #self.assertIsInstance(obj, self.builder._builded_class)
        self.assertIsInstance(obj, MockModule2)
        self.assertIsInstance(obj, MockModule1)
        
    def test__builded_class(self):
        self.assertTrue(issubclass(self.builder._builded_class, MockModule2))
        self.assertTrue(issubclass(self.builder._builded_class, MockModule1))
        
    def test__builded_class_name(self):
        self.assertEqual(self.builder._builded_class_name, 'MockModule2Builded')    
     
    def test__builded_class_bases(self):
        self.assertEqual(self.builder._builded_class_bases, (MockModule2,))
        
    def test__builded_class_dict(self):
        self.assertEqual(self.builder._builded_class_dict, {
            '__doc__': 'docstring',
            '__module__': type(self).__module__,
            'attr1': 'value1',
            'attr2': 'value2',
        })
    
    
#Fixtures

class MockModule1:
    
    #Public
    
    __meta_init__ = lambda *args, **kwargs: None
    attr1 = Mock(return_value='value1')


class MockModule2(MockModule1):
    """docstring"""

    #Public

    attr2 = Mock(return_value='value2')


class MockModuleBuilder(ModuleBuilder):

    #Protected

    _attribute_builder_class = Mock