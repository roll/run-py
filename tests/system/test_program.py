import os
from run import Program

def test():
    os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
    program = Program(['run', 'render', '-d'])
    program()