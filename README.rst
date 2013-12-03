Run
===
Program to run methods from file.

Requirements
------------
- Python 3.3 and higher

Installation
------------
- pip install runpack

Example
-------
- create runfile.py in current working directory::

    from run import Run

    class Run(Run):
    
        #Public
    
        def hello(self, person, times=1):
            """Print 'Hello {person} {times} times!'"""
            print('Hello {person} {times} times!'.format(person=person,
                                                         times=str(times)))
            
- get methods list from command line::

    $ run
    hello
    help
    list

- autocomplete method from command line::

    $ run he<TAB>
    $ run hello
    
- get method help from command line::

    $ run hello -h
    hello(person, times=1)
    Print 'Hello, {person}, {times} times!'

- run method from command line::

    $ run hello world, times=3
    Hello world 3 times!

History
-------
0.7.0
`````
- rewritten using IPC.Light
- moved to Python 3.3

0.6.0
`````
- included python driver

0.5.0
`````
- added user settings

0.4.0
`````
- added autocompletion

0.3.0
`````
- added runclass methods running
- added runfile running by absolute path
- renamed option filename to runfile

0.2.0
`````
- added driver seeking in current working directory