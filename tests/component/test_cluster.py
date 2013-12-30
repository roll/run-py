import unittest
from unittest.mock import Mock
from run.cluster import Cluster

#Tests

class ClusterTest(unittest.TestCase):

    #Public
    
    def setUp(self):
        self.cluster = MockCluster(
            names='names', tags='tags', path='path', 
            file_pattern='file_pattern', recursively='recursively',
            existent='existent')

    def test(self):
        self.assertEqual(self.cluster.attr, ['attr1', 'attr2'])
    

#Fixtures

    
class MockModule1:

    #Public

    __init__ = Mock(return_value=None)
    attr = 'attr1'
    
    
class MockModule2:

    #Public

    __init__ = Mock(return_value=None)
    attr = 'attr2'    
    
    
class MockLoader:
    
    #Public
    
    __init__ = Mock(return_value=None)
    load = Mock(return_value=[x for x in [MockModule1, MockModule2]])
    
    
class MockCluster(Cluster):

    #Public

    _loader_class = MockLoader