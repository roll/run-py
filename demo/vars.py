import os
from run import (Module, CommandTask, CommandVar, DescriptorVar, FindVar,
                 FunctionVar)


class VarsModule(Module):

    # Tasks

    command_task = CommandTask(
        'echo "Hello World!"',
    )

    # Vars

    command = CommandVar(
        'echo "Hello World!"',
    )

    descriptor = DescriptorVar(
        descriptor=property(lambda self: True),
        meta_docstring='Return True.',
    )

    find = FindVar(
        mode='strings',
        string='find',
        getfirst=True,
    )

    function = FunctionVar(
        function=os.path.abspath,
        path='path',
    )
