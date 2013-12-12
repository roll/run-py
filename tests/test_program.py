import os
from run import Program

def test():
    path = os.path.join(os.path.dirname(__file__), '..', 'runfile.py')
    program = Program(['run', '-f', path])
    program()