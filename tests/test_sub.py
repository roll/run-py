import unittest
from sub import Sub, Task

#Tests

class SubTest(unittest.TestCase):

    #Public

    def setUp(self):
        self.sub = MockSub()
        
    def test__tasks(self):
        self.assertEqual(list(self.sub._tasks), ['x', 'a', 'b', 'c'])
        
        
#Fixtures
        
class MockTask(Task):
    
    def complete(self, values):
        pass   
    
    
class BaseMockSub(Sub):
  
    x = MockTask()
    c = MockTask()
    
    
class MockSub(BaseMockSub):
  
    a = MockTask()
    b = MockTask()  
    c = BaseMockSub.c