import unittest
from functools import partial
from unittest.mock import Mock
from run.cluster import Cluster

class ClusterTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockCluster = self._make_mock_cluster_class()
        self.cluster_constructor = partial(MockCluster,
            names='names', 
            tags='tags', 
            filename='filename',             
            basedir='basedir', 
            recursively='recursively',
            existent='existent', 
            dispatcher='dispatcher')

    def test___getattr__(self):
        cluster = self.cluster_constructor()
        self.assertEqual(cluster.attr1, [1, 2, 3])
            
    def test___getattr__with_existent_is_false(self):
        cluster = self.cluster_constructor(existent=False)
        self.assertRaises(AttributeError, getattr, cluster, 'attr2')
        
    def test___getattr___with_existent_is_true(self):
        cluster = self.cluster_constructor(existent=True)
        self.assertEqual(cluster.attr2, [1])
    
    def test__modules(self):
        cluster = self.cluster_constructor()
        cluster._modules
        for module in cluster._finder_class.return_value.find.return_value:
            module.assert_called_with(
                basedir='basedir', dispatcher='dispatcher', module=None)
        
    def test__module_classes(self):
        cluster = self.cluster_constructor()
        cluster._module_classes
        cluster._finder_class.return_value.find.assert_called_with(
            'filename', 'basedir', 'recursively')
            
    def test__module_loader(self):
        cluster = self.cluster_constructor()
        cluster._module_loader
        cluster._finder_class.assert_called_with(
            names='names', tags='tags')
        
    def test__basedir_default(self):
        cluster = self.cluster_constructor(basedir=None)
        self.assertEqual(cluster._basedir, 'default_basedir')
        
    def test__filename_default(self):
        cluster = self.cluster_constructor(filename=None)
        self.assertEqual(cluster._filename, 'default_filename')
        
    #Protected
    
    def _make_mock_cluster_class(self):
        class MockCluster(Cluster):
            #Protected
            _finder_class = Mock(return_value=Mock(find=
                Mock(return_value=[module_class for module_class in 
                    [Mock(return_value=Mock(attr1=1, attr2=1)), 
                     Mock(return_value=Mock(attr1=2, spec=['attr1'])), 
                     Mock(return_value=Mock(attr1=3, spec=['attr1']))]])))
            _default_basedir = 'default_basedir'
            _default_filename = 'default_filename'            
        return MockCluster