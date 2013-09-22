import unittest
from run import Server, Run, Request

#Tests

class ServerTest(unittest.TestCase):
    
    #Public
    
    def setUp(self):
        self.server = EchoServer()
        
    def test_respond(self):
        request = Request('echo', ['content'])
        response = self.server.respond(request)
        self.assertEqual(response.result, 'content')
        self.assertEqual(response.error, '')
        
        
#Fixtures

class Run(Run):
    
    #Public
    
    def echo(self, content):
        return content
    
    
class EchoServer(Server):
    
    #Public
    
    def serve(self):
        pass
    
    @property
    def run(self):
        return Run()