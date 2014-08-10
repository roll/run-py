from packgram import ManageModule


class Module(ManageModule):

    # Attributes

    author = 'roll'
    author_email = 'roll@respect31.com'
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
    ]
    data_files = [('/etc/bash_completion.d', ['data/run.sh'])]
    description = 'Run is a program to run tasks from files.'
    development_requires = ['packgram>=0.10.4', 'sphinx', 'sphinx_rtd_theme']
    entry_points = {'console_scripts': ['run = run.program:program']}
    github_user = 'respect31'
    install_requires = ['box>=0.32', 'jinja2']
    license = 'MIT License'
    name = 'run'
    platforms = ['Unix']
    pypi_name = 'runpack'
    pypi_password_secure = 'JaTeiyjnimmtwhbdfPMZZdtp+5S920vb0HobJWL1QQjHVAo5Hwt0kTWYG+zjDrpWUL+NanVNqhQA8xnvWKbI5cZ+n3PvS7KFbgn6XcTYfeEGyEdYUFi0sXaUsgcfke+9nyMBDLoRH2M7TGqpLY2dmXk5C0h0RMkkAPjxgZCan94='
    tests_require = ['nose']
    test_suite = 'nose.collector'
