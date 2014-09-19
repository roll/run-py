import os
from run import (Module, CommandTask, DescriptorTask, FindTask,
                 FunctionTask, NullTask, ProxyTask)


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

    null = NullTask(
        meta_require=['command'],
    )

    proxy = ProxyTask(
        task='command',
    )