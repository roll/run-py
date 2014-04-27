.. {{ caution }}

{{ name|capitalize }}
=====================
{{ description }}

.. image:: https://secure.travis-ci.org/{{ github_user }}/{{ name }}.png?branch=master 
     :target: https://travis-ci.org/{{ github_user }}/{{ name }} 
     :alt: build
.. image:: https://coveralls.io/repos/{{ github_user }}/{{ name }}/badge.png?branch=master 
     :target: https://coveralls.io/r/{{ github_user }}/{{ name }}  
     :alt: coverage
.. image:: http://b.repl.ca/v1/docs-uploaded-brightgreen.png
     :target: http://{{ name }}.readthedocs.org
     :alt: documentation
     
Quick Links
-----------
- `Source code (GitHub) <https://github.com/{{ github_user }}/{{ name }}>`_
- `Package index (PyPi) <https://pypi.python.org/pypi?:action=display&name={{ pypi_name }}>`_

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install {{ pypi_name }}

Example
-------

The real simple example introduces some functionality. 

- create runfile.py in current working directory:

  .. code-block:: python

    from run import Module, InputVar, require, trigger
    
    class MainModule(Module):
        
        #Tasks
        
        def ready(self):
            print('Your choice is "{greeting}".\n'
                  'We\'re ready.'.format(
                greeting=self.greeting,))    
        
        @require('ready')
        @trigger('done')
        def greet(self, person='World'):
        	"""Greet the given person."""
            print('{greeting} {person}!'.format(
                greeting=self.greeting, 
                person=person))
            
        def done(self):
            print('OK. We\'re done.')
            
        #Vars
        
        greeting = InputVar(
            prompt='Type your greeting',
            default='Hello',
        )
	    
- get run attributes list from command line:

  .. code-block:: bash

    $ run
    default
    done
    greet
    greeting
    info
    list
    meta
    ready

- autocomplete attribute from command line:

  .. code-block:: bash

    $ run li<TAB>
    $ run list
    
- get attribute infomation from command line:

  .. code-block:: bash

    $ run greet -i
    greet(person='World')
    ---
    Type: MethodTask
    Dependencies: [trigger <MethodTask "done">, require <MethodTask "ready">]
    Default arguments: ()
    Default keyword arguments: {}
    ---
    Greet the given person


- run task from command line:

  .. code-block:: bash

    $ run greet Rachel
    Type your greeting [Hello]: <Hi>
    Your choice is "Hi".
    We're ready.
    Hi Rachel!
    OK. We're done.
	
More usefull example you can find here:

- `Base module <https://github.com/respect31/packgram/blob/master/packgram/manage/python.py>`_
- `Run's module <https://github.com/respect31/run/blob/master/runfile.py>`_
- `Run's templates <https://github.com/respect31/run/tree/master/_sources>`_

That's how run builds himself using module inheritance.
        
Authors
-------
- {{ author }} <{{ author_email }}>

Maintainers
-----------
- {{ maintainer }} <{{ maintainer_email }}>

License
-------
{{ license }}
`````````````
Copyright (c) 2014 Respect31 <post@respect31.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.