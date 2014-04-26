import unittest
from run import Module, NullTask, require

#Tests

class DependencyTest(unittest.TestCase):
    
    #Public
    
    pass


#Fixtures

class MainModule(Module):
    
    #Tasks
    
    task1 = NullTask()
    task2 = NullTask()
    task2.require('task1')
    
    @require('task1')
    def task3(self):
        pass
        