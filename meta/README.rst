{% extends 'packgram/README.rst' %}

{% block badges %}
{{ super() }}

Example
-------

The real simple example introduces some functionality. 

- create runfile.py in current working directory:

  .. code-block:: python

    from run import Module, require, trigger
    
    class Module(Module):
        
        #Tasks
        
        def ready(self):
            print('We are ready.')
    
        @require('ready')
        @trigger('done')
        def hello(self, person='World', times=3):
            """Say hello to the given person."""
            print('Hello', person, str(times), 'times!')
    
        def done(self):
            print('We are done.')
	    
- get run attributes list from command line:

  .. code-block:: bash

    $ run
    default
    done
    hello
    info
    list
    meta
    ready

- autocomplete attribute from command line:

  .. code-block:: bash

    $ run h<TAB>
    $ run hello
    
- get attribute infomation from command line:

  .. code-block:: bash

    $ run hello -i
    hello(person='World', times=3)
    ---
    Type: MethodTask
    Dependencies: [trigger <MethodTask "done">, require <MethodTask "ready">]
    Default arguments: ()
    Default keyword arguments: {}
    ---
    Say hello to the given person.

- run task from command line:

  .. code-block:: bash

    $ run hello Rachel, times=5
    We are ready.
    Hello Rachel 5 times!
    We are done.
{% endblock %}