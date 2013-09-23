import unittest
from run import Command

class CommandTest(unittest.TestCase):
    
    #Public
    
    def test(self):
        command = Command(['run', 'method'])             
        print(command)