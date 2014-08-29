import os
import fractions
from run import Module, AutoModule, FindModule, SubprocessModule


class ModulesModule(Module):

    # Modules

    auto = AutoModule(
        sources=[fractions],
    )

    find = FindModule(
        file='tasks.py',
        basedir=os.path.dirname(__file__),
    )

    subprocess = SubprocessModule(
        mapping={
            'hello': 'echo "Hello World!"',
            'goodbye': 'echo "Goodbye World!"',
        },
    )
