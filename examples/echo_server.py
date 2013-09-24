#!/usr/bin/env python3.3
import sys
from run import SubprocessServer, Run

class Run(Run):
    
    #Public
    
    def echo(self, content):
        return content


if __name__ == '__main__':
    server = SubprocessServer(Run(), sys.argv)
    server.serve()