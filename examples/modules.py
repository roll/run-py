import os
import fractions
from run import Module, AutoModule, FindModule, CommandModule


class ModulesModule(Module):

    # Modules

    auto = AutoModule(
        sources=[fractions],
    )

    command = CommandModule(
        mapping={
            'hello': 'echo "Hello World!"',
            'goodbye': 'echo "Goodbye World!"',
        },
    )

    find = FindModule(
        file='tasks.py',
        basedir=os.path.dirname(__file__),
    )
