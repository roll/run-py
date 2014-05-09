import unittest
from unittest.mock import Mock
from run.module.find import FindModule

class FindModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.kwargs = {
            'names': 'names', 
            'tags': 'tags', 
            'file': 'file',             
            'basedir': 'basedir', 
            'recursively': 'recursively'}

    def test___new__(self):
        mock_module = Mock()
        MockModule = self._make_mock_module_class([mock_module])
        module = MockModule(**self.kwargs)
        self.assertIsInstance(module, Mock)
        MockModule._get_find.return_value.assert_called_with(
            names='names', 
            tags='tags',
            file='file', 
            basedir='basedir', 
            recursively='recursively')
        
    def test___new___no_modules(self):
        MockModule = self._make_mock_module_class([])
        self.assertRaises(ImportError, MockModule, **self.kwargs)
    
    #Protected

    def _make_mock_module_class(self, modules):
        class MockFindModule(FindModule):
            #Protected
            _get_find = Mock(return_value=Mock(return_value=modules))
        return MockFindModule