import unittest
import subprocess
from lib31.utils.patcher import Patcher
from run_python import PythonDriver

#Environment
subprocess


#Fixtures   
class Command(object):
    
    json = {}     

     
#Tests     
class PythonDriverTest(unittest.TestCase):       
      
    PATCH = {
        'subprocess.call': lambda *args, **kwargs: kwargs['env']         
    }
      
    def setUp(self):
        self.patcher = Patcher(globals())
        self.patcher.patch(self.PATCH)
        self.command = Command() 
        self.driver = PythonDriver(self.command)
        
    def tearDown(self):
        self.patcher.restore()
        
    def test_process(self):
        self.assertEqual(self.driver.process(), self.driver._environ)
        
    def test_environ(self):
        self.assertIn('RUN_COMMAND', self.driver._environ)
        self.assertEqual(self.driver._environ['RUN_COMMAND'], {})
        
    def test_connector(self):
        self.assertTrue(self.driver._connector.endswith('.py'))             