import os
import mario
mario.activate(basedir=os.path.dirname(__file__))
from mario.origin import ProjectModule  # @UnresolvedImport


class ProjectModule(ProjectModule):

    # Public

    author = 'roll'
    author_email = 'roll@respect31.com'
    copyright = 'Copyright (c) 2014 Respect31 <post@respect31.com>'
    data_files = [('/etc/bash_completion.d', ['data/run.sh'])]
    description = 'Run is a program to run tasks from files.'
    development_requires = [
        'mario', 'sphinx', 'sphinx-settings', 'sphinx-rtd-theme']
    entry_points = {'console_scripts': ['run = run:program']}
    github_user = 'run-hub'
    install_requires = ['clyde']
    interpreters = ['3.3', '3.4']
    license = 'MIT License'
    name = 'run'
    platforms = ['Unix']
    pypi_name = 'runfile'
    pypi_password_secure = 'UTAKiB5msNGZpd9PAqU0JjOvNsv+RUKrZ9UmUOGHin5flYBDnLHvW6cYDr1mQC4zKh3bJ2pqyGEvM1KtlX+IkhSnHn7sZM3npgoOGKcRpf+Vlz7b+ClK6AqtFH6bZPBnbw6HsAm8NWjt8N5GwQaqdSLJxxcpsnBBatOEzkuzggw='
    tests_require = ['nose', 'coverage']
    test_suite = 'nose.collector'
    version = '0.46.1'
