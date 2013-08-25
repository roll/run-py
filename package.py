from setuptools import find_packages

package = {

	#Main

    'name': 'run-client',
	'version': '',
	'packages': find_packages('run-client'),
	'include_package_data': True,
    'data_files': [
        ('/etc/bash_completion.d', ['run/console/completion/run.sh'])       
    ],
    'entry_points': {
        'console_scripts': [
            'run = run.console.script:script',
        ]
    },
    'install_requires': ['lib31>=0.4'],     
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': 'Respect31',
    'author_email': 'post@respect31.com',
    'maintainer': 'Respect31',
    'maintainer_email': 'post@respect31.com',
    'license': 'MIT License',    
    'url': 'https://github.com/respect31/run-client',
    'download_url': 'https://github.com/respect31/run-client/tarball/',    
    'classifiers': ['Development Status :: 4 - Beta', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Programming Language :: Python :: 3.3', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: System :: Systems Administration'],    
    'description': 'Extendable program to run, get help and list functions/methods from file with autocompletion.   ',    
    'long_description': '''Run-client
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
- added driver seeking in current working directory''',
        
}