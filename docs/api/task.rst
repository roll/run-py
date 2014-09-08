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

Concrete tasks
--------------

.. autoclass:: run.task.DescriptorTask
.. autoclass:: run.task.FunctionTask

Metaclass
---------

.. autoclass:: run.task.TaskMetaclass

Prototype
---------

.. autoclass:: run.task.TaskPrototype

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
