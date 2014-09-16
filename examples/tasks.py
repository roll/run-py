import os
from run import (Module, DerivedTask, DescriptorTask, FindTask, FunctionTask,
                 NullTask, CommandTask)


class TasksModule(Module):

    # Tasks

    command = CommandTask(
        'echo "Hello World!"',
    )

    derived = DerivedTask(
        task='command',
    )

    descriptor = DescriptorTask(
        descriptor=property(lambda self: True),
        meta_docstring='Return True.',
    )

    find = FindTask(
        mode='strings',
        string='find',
        getfirst=True,
    )

    function = FunctionTask(
        function=os.path.abspath,
    )

    null = NullTask(
        meta_require=['command'],
    )
