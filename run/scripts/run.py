import sys
from ..program import Program

def run():
    program = Program(sys.argv)
    return program.process()