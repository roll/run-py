#!/usr/bin/env python3.3
import sys
from run import SubprocessServer, Run

class Run(Run):
    
    #Public
    
    def hello(self, person, times=1):
        """Prints 'Hello {person} {times} times!'"""
        print('Hello {person} {times} times!'.format(person=person,
                                                     times=str(times)))


if __name__ == '__main__':
    server = SubprocessServer(Run(), sys.argv)
    server.serve()