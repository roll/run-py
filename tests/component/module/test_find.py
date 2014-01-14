import unittest
from unittest.mock import Mock
from run.module.find import FindModule

class FindModuleTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.kwargs = {
            'names': 'names', 
            'tags': 'tags', 
            'filename': 'filename',             
            'basedir': 'basedir', 
            'recursively': 'recursively'}

    def test___new__(self):
        mock_module = Mock()
        MockFindModule = self._make_mock_find_module_class([mock_module])
        module = MockFindModule(**self.kwargs)
        self.assertIsInstance(module, Mock)
        (MockFindModule._get_finder_class.return_value.
            assert_called_with(names='names', tags='tags'))
        (MockFindModule._get_finder_class.return_value.return_value.find.
            assert_called_with('filename', 'basedir', 'recursively'))
        
    def test___new___no_modules(self):
        MockFindModule = self._make_mock_find_module_class([])
        self.assertRaises(ImportError, MockFindModule, **self.kwargs)
    
    #Protected

    def _make_mock_find_module_class(self, modules):
        class MockFindModule(FindModule):
            #Protected
            _get_finder_class = Mock(return_value=Mock(return_value=Mock(
                find=Mock(return_value=modules))))
        return MockFindModule