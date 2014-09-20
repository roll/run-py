import os
import fractions
from run import Module, FindModule, FunctionModule, CommandModule


class ModulesModule(Module):

    # Modules

    command = CommandModule(
        mapping={
            'hello': 'echo "Hello World!"',
            'goodbye': 'echo "Goodbye World!"',
        },
    )

    find = FindModule(
        filename='tasks.py',
        basedir=os.path.dirname(__file__),
    )

    function = FunctionModule(
        mapping=fractions,
    )