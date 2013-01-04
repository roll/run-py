import sys
from ..program.program import Program

def run():
    program = Program(sys.argv)
    return program.process()