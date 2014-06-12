==============
run.dependency
==============

Module provides dependency related functionality.

Public
======

Module’s public interface.

Base class
----------

.. autoclass:: run.dependency.Dependency

Base decorator class
--------------------

.. autoclass:: run.dependency.DependencyDecorator

Helper decorators
-----------------

.. autoclass:: run.dependency.depend
.. autoclass:: run.dependency.require
.. autoclass:: run.dependency.trigger
     
Internal
========

Module’s internal implementation.

.. autoclass:: run.dependency.resolver.Resolver
.. autoclass:: run.dependency.resolver.CommonResolver
.. autoclass:: run.dependency.resolver.NestedResolver