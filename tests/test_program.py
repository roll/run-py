import os
from sub import Program

def test():
    path = os.path.join(os.path.dirname(__file__), '..', 'subfile.py')
    program = Program(['sub', '-f', path])
    program()