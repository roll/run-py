import unittest
from functools import partial
from unittest.mock import Mock
from run.run.cluster import Cluster

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
            strict='strict', 
            dispatcher='dispatcher')

    def test___getattr__(self):
        cluster = self.pcluster()
        self.assertEqual(cluster.attr1, [1, 2, 3])
            
    def test___getattr__with_strict_is_true(self):
        cluster = self.pcluster(strict=True)
        self.assertRaises(AttributeError, getattr, cluster, 'attr2')
        
    def test___getattr___with_strict_is_false(self):
        cluster = self.pcluster(strict=False)
        self.assertEqual(cluster.attr2, [1])
    
    def test__modules(self):
        cluster = self.pcluster()
        cluster._modules
        cluster._find.assert_called_with(
            names='names', 
            tags='tags',                                                       
            file='file', 
            basedir='basedir', 
            recursively='recursively')
        for module in cluster._find.return_value:
            module.assert_called_with(
                meta_dispatcher='dispatcher', 
                meta_module=None)
        
    #Protected
    
    def _make_mock_cluster_class(self):
        class MockCluster(Cluster):
            #Public
            default_file = 'default_file'               
            default_basedir = 'default_basedir'
            #Protected
            _find = Mock(return_value=[module_class for module_class in 
                [Mock(return_value=Mock(attr1=1, attr2=1)), 
                 Mock(return_value=Mock(attr1=2, spec=['attr1'])), 
                 Mock(return_value=Mock(attr1=3, spec=['attr1']))]])
        return MockCluster