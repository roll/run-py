from run import FindModule
from packgram import ManageModule
    
class MainModule(ManageModule):
    
    #Modules
        
    #TODO: use names instead basedir after run fix
    docs = FindModule(basedir='docs')
    tests = FindModule(basedir='tests') 

    #Vars
    
    author = 'roll'
    author_email = 'roll@respect31.com'
    caution = 'DO NOT CHANGE THIS FILE. SOURCE IS IN "_sources" DIRECTORY.'
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers', 
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.3', 
        'Topic :: Software Development :: Libraries :: Python Modules', 
        'Topic :: System :: Systems Administration', 
    ]
    data_files = [('/etc/bash_completion.d', ['data/run.sh'])]
    description = 'Run is a program to run tasks from files.'
    development_requires = [
        'sphinx',
        'sphinx_rtd_theme',
    ]
    entry_points = {'console_scripts': ['run = run:program']}
    github_user = 'respect31'
    install_requires = [
        'box>=0.20',
        'jinja2',
    ]
    license = 'MIT License'  
    maintainer = 'roll'
    maintainer_email = 'roll@respect31.com'
    name = 'run'
    platforms = ['Unix'] 
    pypi_name = 'runpack'
    pypi_user = 'roll'
    pypi_password_secure = 'JaTeiyjnimmtwhbdfPMZZdtp+5S920vb0HobJWL1QQjHVAo5Hwt0kTWYG+zjDrpWUL+NanVNqhQA8xnvWKbI5cZ+n3PvS7KFbgn6XcTYfeEGyEdYUFi0sXaUsgcfke+9nyMBDLoRH2M7TGqpLY2dmXk5C0h0RMkkAPjxgZCan94='
    tests_require = [
        'packgram>=0.9',        
        'nose',
    ]
    test_suite = 'nose.collector'    