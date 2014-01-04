import unittest
from functools import partial
from unittest.mock import Mock
from run.cluster import Cluster

#Tests

class ClusterTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        MockCluster = self._make_mock_cluster_class()
        self.cluster_constructor = partial(MockCluster,
            names='names', tags='tags', basedir='basedir', 
            file_pattern='file_pattern', recursively='recursively',
            existent='existent', dispatcher='dispatcher')

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
        for module in cluster._loader_class.load.return_value:
            module.__init__.assert_called_with(
                basedir='basedir', dispatcher='dispatcher', module=None)
        
    def test__module_classes(self):
        cluster = self.cluster_constructor()
        cluster._module_classes
        cluster._loader_class.load.assert_called_with(
           'basedir', 'file_pattern', 'recursively')
            
    def test__module_loader(self):
        cluster = self.cluster_constructor()
        cluster._module_loader
        cluster._loader_class.__init__.assert_called_with(
            names='names', tags='tags')
        
    #Protected
    
    def _make_mock_module1_class(self):
        class MockModule1:
            #Public
            __init__ = Mock(return_value=None)
            attr1 = 1
            attr2 = 1
        return MockModule1
    
    def _make_mock_module2_class(self):
        class MockModule2:
            #Public
            __init__ = Mock(return_value=None)
            attr1 = 2
        return MockModule2
   
    def _make_mock_module3_class(self):
        class MockModule3:
            #Public
            __init__ = Mock(return_value=None)
            attr1 = 3
        return MockModule3  
    
    def _make_mock_loader_class(self):
        MockModule1 = self._make_mock_module1_class()
        MockModule2 = self._make_mock_module2_class()
        MockModule3 = self._make_mock_module3_class()
        class MockLoader:
            #Public
            __init__ = Mock(return_value=None)
            load = Mock(return_value=[module for module in 
                [MockModule1, MockModule2, MockModule3]])
        return MockLoader
    
#     def _make_mock_loader_class(self):
#         class MockLoader:
#             #Public
#             __init__ = Mock(return_value=None)
#             load = Mock(return_value=[module for module in 
#                 [Mock(return_value=Mock(attr1=1, attr2=1)), 
#                  Mock(return_value=Mock(attr1=2, attr2=2)), 
#                  Mock(return_value=Mock(attr1=3))]])
#         return MockLoader    
    
    def _make_mock_cluster_class(self):
        MockLoader = self._make_mock_loader_class()
        class MockCluster(Cluster):
            #Protected
            _loader_class = MockLoader
        return MockCluster