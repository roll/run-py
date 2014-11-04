.. Block: caution

.. TO MAKE CHANGES USE "meta" DIRECTORY (see packgram docs).

.. Block: description

Run
=====================
Run is a program to run tasks from files.

.. Block: badges

.. image:: http://img.shields.io/badge/code-GitHub-brightgreen.svg
     :target: https://github.com/run-hub/run
     :alt: code
.. image:: http://img.shields.io/travis/run-hub/run/master.svg
     :target: https://travis-ci.org/run-hub/run 
     :alt: build
.. image:: http://img.shields.io/coveralls/run-hub/run/master.svg 
     :target: https://coveralls.io/r/run-hub/run  
     :alt: coverage
.. image:: http://img.shields.io/badge/docs-latest-brightgreen.svg
     :target: http://run.readthedocs.org
     :alt: docs     
.. image:: http://img.shields.io/pypi/v/runfile.svg
     :target: https://pypi.python.org/pypi?:action=display&name=runfile
     :alt: pypi


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
    [+] list
    [+]

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
    [+] info

- run task from command line:

  .. code-block:: bash

    $ run hello Rachel, times=5
    We are ready.
    [+] hello/ready
    Hello Rachel 5 times!
    We are done.
    [+] hello/done
    [+] hello

.. Block: application

Application
-----------
Package is under active development and is not ready for production use.
Backward-compatibility between minor releases (0.x.0), documentation and 
changelog are not guaranteed to be present before stable versions (>=1.0.0).

.. Block: requirements

Requirements
------------
- Platforms

  - Unix
- Interpreters

  - Python 3.3
  - Python 3.4

.. Block: installation

Installation
------------
- pip install runfile

.. Block: contribution

Contribution
------------
- Authors

  - roll <roll@respect31.com>
- Maintainers

  - roll <roll@respect31.com>

.. Block: changelog

Changelog
---------
- no entries yet

.. Block: license

License
-------
**MIT License**

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
