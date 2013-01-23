from box import Package

class Package(Package):
    
    #Public
    
    name = 'runfile'
    data_files = [
        ('/etc/bash_completion.d', ['run/data/completion/run.sh'])       
    ]     
    entry_points = {
        'console_scripts': [
            'run = run.scripts.run:run',
        ]
    }   
    include_package_data = True    
    install_requires = ['box>=0.5', 'lib31>=0.3']   
    test_suite = 'nose.collector'
    tests_require = ['nose']
    
    url = 'https://github.com/respect31/run'
    platforms=['Unix', 'POSIX']
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',               
    ]
    
    
package = Package()