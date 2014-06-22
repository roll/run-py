import unittest
from functools import partial
from unittest.mock import Mock
from run.cluster.cluster import Cluster

class ClusterTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockCluster = self._make_mock_cluster_class()
        self.pcluster = partial(MockCluster,
            names='names', 
            tags='tags', 
            file='file',             
            basedir='basedir', 
            recursively='recursively',
            existent='existent', 
            dispatcher='dispatcher')

    def test___getattr__(self):
        cluster = self.pcluster()
        self.assertEqual(cluster.attr1, [1, 2, 3])
        cluster._find_files.assert_called_with(
            file='file', 
            basedir='basedir', 
            recursively='recursively')        
        cluster._find_modules.assert_called_with(
            names='names', 
            tags='tags',
            files=['file1', 'file2'],                                                       
            basedir='basedir')
        for module in cluster._find_modules.return_value:
            module.assert_called_with(
                meta_dispatcher='dispatcher', 
                meta_module=None)
            
    def test___getattr___with_existent_is_false(self):
        cluster = self.pcluster(existent=False)
        self.assertRaises(AttributeError, getattr, cluster, 'attr2')
        
    def test___getattr___with_existent_is_true(self):
        cluster = self.pcluster(existent=True)
        self.assertEqual(cluster.attr2, [1])
        
    #Protected
    
    def _make_mock_cluster_class(self):
        class MockCluster(Cluster):
            #Protected
            _find_files = Mock(return_value=[
                'file1', 
                'file2'])
            _find_modules = Mock(return_value=[
                Mock(return_value=Mock(attr1=1, attr2=1)), 
                Mock(return_value=Mock(attr1=2, spec=['attr1'])), 
                Mock(return_value=Mock(attr1=3, spec=['attr1']))])
        return MockCluster