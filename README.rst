Run-client
===
Extendable program to run, get help and list functions/methods from file with autocompletion.   

Installation
------------
Step 1
``````
- pip install box

Step 2
``````
- pip install runfile

Example
-------
- create runfile.py in current working directory::

    def hello(person, times=1):    
        """prints 'Hello, {person}, {times} times!'"""
        print('Hello, {person}, {times} times!'.
              format(person=person,
                     times=str(times)))
            
    def nothing():
        """does nothing"""
        pass
            
    OR        
            
    class Runclass(object):
        
        def hello(self, person, times=1): 
            """prints 'Hello, {person}, {times} times!'"""
            print('Hello, {person}, {times} times!'.
                  format(person=person,
                         times=str(times)))
            
        def nothing(self):
            """does nothing"""
            pass
            
- get functions/methods list from command line::

    $ run
    hello
    nothing

- autocomplete function/method from command line::

    $ run he<TAB>
    $ run hello
    
- get function/method help from command line::

    $ run hello -h
    hello(person, times=1)
    prints 'Hello, {person}, {times} times!'

- run function/method from command line::

    $ run hello world times=3
    Hello, world, 3 times!
    
Usage
-----
Command line::

    run [-h] [-d DRIVER] [-l LANGUAGE] [-f RUNFILE] [-c RUNCLASS] 
        [function] [arguments [arguments ...]]

    positional arguments:
      function
      arguments

    optional arguments:
      -h, --help    
      -d DRIVER, --driver DRIVER
      -l LANGUAGE, --language LANGUAGE
      -f RUNFILE, --runfile RUNFILE      
      -c RUNCLASS, --runclass RUNCLASS

Extension
---------
You can write driver for your favorite language. 
It's all about run/inspect functions -- no script/command line routine need to be implemented.
Run core automaticly finds language drivers in run_{language}.{Language}Driver form.

History
-------
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