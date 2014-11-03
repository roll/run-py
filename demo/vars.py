from run import Module, CommandTask, CommandVar, FindVar


class VarsModule(Module):

    # Tasks

    command_task = CommandTask(
        'echo "Hello World!"',
    )

    # Vars

    command = CommandVar(
        'echo "Hello World!"',
    )

    find = FindVar(
        mode='strings',
        string='find',
        getfirst=True,
    )
