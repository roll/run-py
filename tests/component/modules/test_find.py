import unittest
from unittest.mock import Mock
from run.modules.find import FindModule

class FindModuleTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        MockFindModule = self._make_mock_find_module_class()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.module = MockFindModule(module=None)
    
    def test_find_files(self):
        files = self.module.find_files(*self.args, **self.kwargs)
        self.assertEqual(files, 'files')
        (self.module._find_files_function.
            assert_called_with(*self.args, **self.kwargs))
    
    def test_find_strings(self):
        strings = self.module.find_strings(*self.args, **self.kwargs)
        self.assertEqual(strings, 'strings')
        (self.module._find_strings_function.
            assert_called_with(*self.args, **self.kwargs))
    
    def test_find_objects(self):
        objects = self.module.find_objects(*self.args, **self.kwargs)
        self.assertEqual(objects, 'objects')
        (self.module._find_objects_function.
            assert_called_with(*self.args, **self.kwargs))
     
    #Protected 
        
    def _make_mock_find_module_class(self):
        class MockFindModule(FindModule):
            #Protected
            _find_files_function = Mock(return_value='files')
            _find_strings_function = Mock(return_value='strings')
            _find_objects_function = Mock(return_value='objects')
        return MockFindModule