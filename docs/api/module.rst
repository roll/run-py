==========
run.module
==========

Module provides module related functionality.

Public
======

Module’s public interface.

Module class
------------

.. autoclass:: run.module.Module

Metaclass
---------

.. autoclass:: run.module.ModuleMetaclass

Prototype
---------

.. autoclass:: run.module.ModulePrototype 

Cluster
-------

.. autoclass:: run.module.ModuleCluster

Concrete modules
----------------

.. autoclass:: run.module.AutoModule
.. autoclass:: run.module.FindModule
.. autoclass:: run.module.NullModule
.. autoclass:: run.module.SubprocessModule

Helper functions
----------------

.. autoclass:: run.module.find
.. autofunction:: run.module.module
.. autofunction:: run.module.spawn

Exceptions
----------

.. autoclass:: run.module.NotFound

Internal
========

Module’s internal implementation.

.. autoclass:: run.module.constraint.Constraint
.. autoclass:: run.module.error.ModuleAttributeError