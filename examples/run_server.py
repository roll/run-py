#!/usr/bin/env python3.3
import sys
from run import SubprocessServer, Response

class RunServer(SubprocessServer):
    
    #Public
    
    def respond(self, request):
        return Response(request.protocol, request.content)


if __name__ == '__main__':
    server = RunServer(sys.argv)
    server.serve()