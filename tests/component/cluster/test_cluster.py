import unittest
from unittest.mock import Mock
from run.cluster.cluster import Cluster

class ClusterTest(unittest.TestCase):

    # Public

    def setUp(self):
        self.Cluster = self._make_mock_cluster_class()

    def test___getattr__(self):
        cluster = self.Cluster(
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively',
            skip='skip',
            dispatcher='dispatcher')
        self.assertEqual(cluster.attr1, [1, 2, 3])
        self.assertEqual(cluster.attr2, [1])
        # Find
        cluster._find.assert_called_with(
            names='names',
            tags='tags',
            file='file',
            basedir='basedir',
            recursively='recursively')
        # Find's return values
        for module in cluster._find.return_value:
            module.assert_called_with(
                meta_dispatcher='dispatcher',
                meta_module=None)

    def test___getattr___with_skip_is_false(self):
        cluster = self.Cluster(skip=False)
        self.assertRaises(AttributeError, getattr, cluster, 'attr2')

    # Protected

    def _make_mock_cluster_class(self):
        class MockCluster(Cluster):
            # Protected
            _find = Mock(return_value=[
                Mock(return_value=Mock(attr1=1, attr2=1)),
                Mock(return_value=Mock(attr1=2, spec=['attr1'])),
                Mock(return_value=Mock(attr1=3, spec=['attr1']))])
        return MockCluster
