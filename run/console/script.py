import sys
from .program import Program

def script():
    program = Program(sys.argv)
    return program.process()