import os
from run import Module, Task, CommandTask, FindTask, FunctionTask


class TasksModule(Module):

    # Tasks

    command = CommandTask(
        'echo "Hello World!"',
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
