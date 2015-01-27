from .module import Module, module
from .program import program
from .settings import settings
from .task import (Task, Logger, Event, TaskEvent, CallTaskEvent,
                   task, depend, require, trigger, hide, skip, stylize)
from .var import Var, var
version = '0.47.0'  # REPLACE: version = '{{ version }}'
