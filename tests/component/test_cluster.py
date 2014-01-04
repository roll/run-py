import unittest
from functools import partial
from unittest.mock import Mock
from run.cluster import Cluster

#Tests

class ClusterTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.cluster_constructor = partial(MockCluster,
            names='names', tags='tags', basedir='basedir', 
            file_pattern='file_pattern', recursively='recursively',
            existent='existent', dispatcher='dispatcher')

    def test___getattr__(self):
        cluster = self.cluster_constructor()
        self.assertEqual(cluster.attr1, [1, 2, 3])
        #Check loader calls
        loader = cluster._module_loader
        loader.__init__.assert_called_with(names='names', tags='tags')
        loader.load.assert_called_with('basedir', 'file_pattern', 'recursively')
        #Check modules calls
        for module in cluster._modules:
            module.__init__.assert_called_with(
                basedir='basedir', dispatcher='dispatcher', module=None)
            
    def test___getattr__with_existent_is_false(self):
        cluster = self.cluster_constructor(existent=False)
        self.assertRaises(AttributeError, getattr, cluster, 'attr2')
        
    def test___getattr___with_existent_is_true(self):
        cluster = self.cluster_constructor(existent=True)
        self.assertEqual(cluster.attr2, [1])           
        

#Fixtures

    
class MockModule1:

    #Public

    __init__ = Mock(return_value=None)
    attr1 = 1
    attr2 = 1
        
    
class MockModule2:

    #Public

    __init__ = Mock(return_value=None)
    attr1 = 2
    
    
class MockModule3:

    #Public

    __init__ = Mock(return_value=None)
    attr1 = 3
    
    
class MockLoader:
    
    #Public
    
    __init__ = Mock(return_value=None)
    load = Mock(return_value=[module for module in 
        [MockModule1, MockModule2, MockModule3]])
    
    
class MockCluster(Cluster):

    #Protected

    _loader_class = MockLoader