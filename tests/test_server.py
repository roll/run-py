import io
import sys
import unittest
from run import SubprocessServer, Run, Request, Encoder, Decoder

#Tests

class SubprocessServerTest(unittest.TestCase):
    
    def setUp(self):
        self.encoder = Encoder()
        self.decoder = Decoder()         
        self.server = SubprocessServer(
            Run(), ['run', self.encoder.encode(Request('echo', ['content']))])    
      
    def test_serve(self):
        #TODO: add context manager?
        old_stdout = sys.stdout
        sys.stdout = new_stdout = io.StringIO()
        self.server.serve()
        sys.stdout = old_stdout
        text_message = new_stdout.getvalue()
        response = self.decoder.decode(text_message)
        self.assertEqual(response.result, 'content')
        self.assertEqual(response.error, '')
         
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