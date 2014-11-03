import os
from run import (Module, Task, CommandTask, DescriptorTask, FindTask,
                 FunctionTask, ProxyTask)


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

    proxy = ProxyTask(
        task='command',
    )

    task = Task(
        meta_require=['command'],
    )
