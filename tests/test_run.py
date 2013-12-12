import unittest
from run import Run, Task

#Tests

class RunTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.sub = MockRun()
        
    def test__tasks(self):
        self.assertEqual(list(self.sub._tasks), ['x', 'a', 'b', 'c'])
        
        
#Fixtures
        
class MockTask(Task):
    
    def complete(self, values):
        pass   
    
    
class BaseMockRun(Run):
  
    x = MockTask()
    c = MockTask()
    
    
class MockRun(BaseMockRun):
  
    a = MockTask()
    b = MockTask()  
    c = BaseMockRun.c