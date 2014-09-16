import unittest
from unittest.mock import Mock, ANY, patch
from run.library.cluster import module


class ClusterModuleTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.addCleanup(patch.stopall)
        self.task = Mock()
        self.args = ('arg1',)
        self.kwargs = {'kwarg1': 'kwarg1'}
        self.FoundModule = Mock(
            return_value=Mock(meta_tasks={'task': self.task}))
        self.find = Mock(return_value=[self.FoundModule])
        patch.object(module, 'find_modules', self.find).start()

    def test(self):
        self.module = module.ClusterModule(
            meta_module=None,
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively')
        self.assertEqual(self.module.task(), [self.task.return_value])
        # Check find call
        self.find.assert_called_with(
            target=module.Module,
            key='key',
            tags='tags',
            file='file',
            exclude='exclude',
            basedir='basedir',
            recursively='recursively',
            filters=ANY)
        # Check FoundModule call
        self.FoundModule.assert_called_with(meta_module=self.module)
