import unittest
from run import Module, NullTask, require, trigger

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
    task2.trigger('task1')
    
    @require('task1')
    @trigger('task2')
    def task3(self):
        pass
        