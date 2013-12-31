import unittest
from unittest.mock import Mock
from run.modules.base.load import LoadModule

#Tests

class LoadModuleTest(unittest.TestCase):

    #Public

    def test___new__(self):
        module = MockLoadModule(
            names='names', tags='tags', path='path', 
            file_pattern='file_pattern', recursively='recursively')
        self.assertIsInstance(module, MockModule)
        (MockLoadModule._loader_class.assert_called_with(
            names='names', tags='tags'))
        MockLoader.load.assert_called_with(
            'path', 'file_pattern', 'recursively')
        
    def test___new___no_modules(self):
        self.assertRaises(ImportError, NoModulesMockLoadModule)
    

#Fixtures

class MockModule:
    
    #Public
    
    __init__ = Mock(return_value=None)
    

class MockLoader:

    #Public

    load = Mock(return_value=[MockModule])


class MockLoadModule(LoadModule):

    #Protected

    _loader_class = Mock(return_value=MockLoader())
    

class NoModulesMockLoadModule(LoadModule):

    #Protected

    _loader_class = Mock(return_value=Mock(load=Mock(return_value=[])))