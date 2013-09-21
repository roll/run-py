#!/usr/bin/env python3.3
import sys
from run import SubprocessServer, Run

class Run(Run):
    
    #Public
    
    pass
    

class RunServer(SubprocessServer):
    
    #Public
    
    def run(self):
        return Run()


if __name__ == '__main__':
    server = RunServer(sys.argv)
    server.serve()