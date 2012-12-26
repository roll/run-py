import os
import sys
import json
import unittest
from lib31.utils.patcher import Patcher
from run import Command, Driver
from run.exceptions.exit import (HelpExit, 
                                 DriverIsNotFoundExit, 
                                 LanguageIsNotSupportedExit,
                                 RunfileIsNotFoundExit)
from .fixtures import process, clicommand

#Environment
sys, process


#Fixtures
class Driver(Driver):
    
    def process(self):
        pass


def load(pointer, *args, **kwargs):
    if pointer == 'run_python.PythonDriver':
        return Driver
    else:
        raise ImportError()


#Tests
class CommandTest(unittest.TestCase):
    
    PATCH = {
        'sys.modules[Command.__module__].load': load,
        'process.cwd': os.path.dirname(__file__),
        'clicommand.runfile': 'test_command.py',
    }
    
    def setUp(self):
        self.patcher = Patcher(globals())
        self.patcher.patch(self.PATCH)
        self.command = Command(clicommand.argv)
        
    def tearDown(self):
        self.patcher.restore()


class CommandTest_normal(CommandTest):
        
    def test_driver(self):
        self.assertIsInstance(self.command.driver, 
                              Driver)
        
    def test_language(self):
        self.assertEqual(self.command.language, 
                         clicommand.language)
                           
    def test_ishelp(self):
        self.assertEqual(self.command.ishelp, 
                         clicommand.ishelp)
   
    def test_runfile(self):
        self.assertTrue(os.path.isfile(self.command.runfile))        
        self.assertTrue(self.command.runfile.
                        endswith(clicommand.runfile))  
   
    def test_runclass(self):
        self.assertEqual(self.command.runclass, 
                         clicommand.runclass)
                 
    def test_function(self):
        self.assertEqual(self.command.function, 
                         clicommand.function)

    def test_arguments(self):
        self.assertEqual(self.command.arguments, 
                         clicommand.arguments)
        
    def test_unknown_option(self):
        self.assertRaises(AttributeError, getattr, 
                          self.command, 'unknown')      
   
    def test_json(self):
        command = json.loads(self.command.json)
        self.assertEqual(len(command), 5)
        self.assertEqual(command['ishelp'], 
                         clicommand.ishelp)
   
    def test_usage(self):
        self.assertIn('usage', self.command.usage)
        
    def test_help(self):
        self.assertIn('usage', self.command.help)
        
    def test_add_option(self):
        self.command.add_option('--test', default='test')
        self.assertEqual(self.command.test, 'test')
        
    def test_add_argument(self):
        self.command.add_argument('test')
        self.assertEqual(self.command.test, 'argument2')


class CommandTest_driver_by_language(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'clicommand.language': 'python',          
        'clicommand.driver': None,             
    })
    
    def test_driver(self):
        self.assertIsInstance(self.command.driver, 
                              Driver)
        
        
class CommandTest_driver_is_not_found(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'clicommand.language': 'language_is_not_supported',
        'clicommand.driver': None,             
    })
    
    def test_driver(self):      
        self.assertRaises(DriverIsNotFoundExit, getattr,
                          self.command, 'driver') 
                       

class CommandTest_language_by_runfile(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'clicommand.language': None,            
    })
    
    def test_language(self):
        self.assertEqual(self.command.language, 'python')
        

class CommandTest_language_is_not_supported(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'Command.runfile': 'basename.uknown_extension',
        'clicommand.language': None,            
    })
    
    def test_language(self):        
        self.assertRaises(LanguageIsNotSupportedExit, getattr, 
                          self.command, 'language')      
        
       
class CommandTest_file_is_not_found(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'clicommand.runfile': 'file_is_not_found',             
    })
    
    def test_runfile(self):  
        self.assertRaises(RunfileIsNotFoundExit, getattr, 
                          self.command, 'runfile')
                
        
class CommandTest_file_is_not_found_in_help_mode(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'clicommand.ishelp': True,
        'clicommand.runfile': 'file_is_not_found',             
    })
    
    def test_runfile(self):
        self.assertEqual(self.command.runfile, '')
        
                        
class CommandTest_no_function(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'clicommand.function': None,
        'clicommand.arguments': None,             
    })
    
    def test_function(self):
        self.assertEqual(self.command.function, '')
        
                        
class CommandTest_no_function_with_help(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'clicommand.ishelp': True,
        'clicommand.function': None,
        'clicommand.arguments': None,             
    })
    
    def test_function(self):
        self.assertRaises(HelpExit, getattr, 
                          self.command, 'function')
        
        
class CommandTest_no_arguments(CommandTest):
    
    PATCH = CommandTest.PATCH.copy()
    PATCH.update({
        'clicommand.arguments': None,             
    })
    
    def test_arguments(self):
        self.assertEqual(self.command.arguments, [])        