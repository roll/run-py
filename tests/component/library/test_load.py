import unittest
from unittest.mock import Mock
from run.library.load import LoadModule

class LoadModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.kwargs = {
            'names': 'names', 
            'tags': 'tags', 
            'basedir': 'basedir', 
            'file_pattern': 'file_pattern', 
            'recursively': 'recursively'}

    def test___new__(self):
        mock_module = Mock()
        MockLoadModule = self._make_mock_load_module_class([mock_module])
        module = MockLoadModule(**self.kwargs)
        self.assertIsInstance(module, Mock)
        MockLoadModule._loader_class.assert_called_with(
            names='names', tags='tags')
        MockLoadModule._loader_class.return_value.load.assert_called_with(
            'basedir', 'file_pattern', 'recursively')
        
    def test___new___no_modules(self):
        MockLoadModule = self._make_mock_load_module_class([])
        self.assertRaises(ImportError, MockLoadModule, **self.kwargs)
    
    #Protected

    def _make_mock_load_module_class(self, modules):
        class MockLoadModule(LoadModule):
            #Protected
            _loader_class = Mock(return_value=Mock(
                load=Mock(return_value=modules)))
        return MockLoadModule