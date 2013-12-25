import os
from run import Program

def test():
    path = os.path.join(os.path.dirname(__file__), '..', '..')
    program = Program(['run', 'render', '-p', path])
    program()