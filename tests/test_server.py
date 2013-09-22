import unittest
from run import Server, SubprocessServer, Run, Request, Encoder

#Tests

class SubprocessServerTest(unittest.TestCase):
    
    def setUp(self):
        self.encoder = Encoder() 
        self.request = Request('echo', ['content'])
        self.argv = ['run', self.encoder.encode(self.request)]
        self.server = EchoSubprocessServer(self.argv)    
      
    def test_serve(self):
        self.server.serve() 
         
    def test_respond(self):
        response = self.server.respond(Request('echo', ['content']))
        self.assertEqual(response.result, 'content')
        self.assertEqual(response.error, '')
    
    def test_respond_unknown_method(self):
        response = self.server.respond(Request('unknown_method'))
        self.assertEqual(response.result, None)
        self.assertTrue(response.error)
        
        
#Fixtures

class Run(Run):
    
    #Public
    
    def echo(self, content):
        return content
    
    
class EchoSubprocessServer(SubprocessServer):
    
    #Public
    
    @property
    def run(self):
        return Run()    