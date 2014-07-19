import unittest
from unittest.mock import Mock
from run.cluster.find import find

class find_Test(unittest.TestCase):

    # Public

    def setUp(self):
        self.find = self._make_mock_find()

    def test(self):
        list(self.find(
            names='names',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively'))
        self.find._find_files.assert_called_with(
            filepath=None,
            notfilepath=None,
            filename='file',
            notfilename='exclude',
            basedir='basedir',
            maxdepth=None)

    # Protected

    def _make_mock_find(self):
        class mock_find(find):
            # Public
            default_basedir = 'default_basedir'
            default_exclude = 'default_exclude'
            default_file = 'default_file'
            default_names = 'default_names'
            default_recursively = 'default_recursively'
            default_tags = 'default_tags'
            # Protected
            _find_files = Mock(return_value=['file1', 'file2'])
            _loader_class = Mock(return_value=Mock(
                load_module=Mock(return_value=unittest.mock)))
        return mock_find
