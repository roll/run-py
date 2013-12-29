import unittest
from run import DependentAttributeTask

#Tests

class DependentAttributeTaskTest(unittest.TestCase):

    #Public

    def test(self):
        task = DependentAttributeTask()
    
    
#Fixtures

class ModuleMock:
    
    #Public
    
    def task(self, *args, **kwargs):
        return (args, kwargs) 
    
    
class AttributeMock:
    
    #Public
    
    def __init__(self):
        self._module = ModuleMock()
    
    def meta_module(self):
        return self._module    