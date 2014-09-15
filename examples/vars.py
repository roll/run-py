import os
from run import (Module, CommandTask, DerivedVar, DescriptorVar, FindVar,
                 FunctionVar, CommandVar)


class VarsModule(Module):

    # Tasks

    command_task = CommandTask(
        'echo "Hello World!"',
    )

    # Vars

    command = CommandVar(
        'echo "Hello World!"',
    )

    derived = DerivedVar(
        task='command_task',
    )

    descriptor = DescriptorVar(
        descriptor=property(lambda self: True),
        meta_docstring='Return True.',
    )

    find = FindVar(
        string='find',
        getfirst=True,
    )

    function = FunctionVar(
        function=os.path.abspath,
        path='path',
    )
