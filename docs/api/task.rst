========
run.task
========

Module provides task related functionality.

Public
======

Module’s public interface.

Base class
----------

.. autoclass:: run.task.Task

Metaclass
---------

.. autoclass:: run.task.TaskMetaclass

Prototype
---------

.. autoclass:: run.task.TaskPrototype

Concrete tasks
--------------

.. autoclass:: run.task.DerivedTask
.. autoclass:: run.task.DescriptorTask
.. autoclass:: run.task.FindTask
.. autoclass:: run.task.FunctionTask
.. autoclass:: run.task.InputTask
.. autoclass:: run.task.MethodTask
.. autoclass:: run.task.NullTask
.. autoclass:: run.task.RenderTask
.. autoclass:: run.task.SubprocessTask

Signal class
------------

.. autoclass:: run.task.TaskSignal

Helper functions
----------------

.. autofunction:: run.task.build
.. autofunction:: run.task.fork
.. autofunction:: run.task.task
   
Internal
========

Module’s internal implementation.

.. autoclass:: run.task.update.TaskUpdate