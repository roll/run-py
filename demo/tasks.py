import os
from run import (Module, Task, CommandTask, DescriptorTask, FindTask,
                 FunctionTask)


class TasksModule(Module):

    # Tasks

    command = CommandTask(
        'echo "Hello World!"',
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

    task = Task(
        meta_require=['command'],
    )
