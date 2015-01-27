# Block: caution
# TO MAKE CHANGES USE [meta] DIRECTORY.

# Block: data_files
import os
data_files = [('/etc/bash_completion.d', ['data/run.sh'])]
if data_files:
    try:
        if os.geteuid() != 0:
            data_files.clear()
    except Exception:
        pass

# Block: long_description
from glob import iglob
long_description = 'Run is a program to run tasks from files.'
for filepath in iglob('README.*'):
    with open(filepath) as file:
        long_description = file.read()
    break     

# Block: packages
from setuptools import find_packages
packages = find_packages(os.path.dirname(__file__) or '.', exclude=['tests*'])

# Block: setup
from setuptools import setup
setup(
    author='roll',
    author_email='roll@respect31.com',
    classifiers=[],       
    description='Run is a program to run tasks from files.',
    data_files=data_files,
    download_url='https://github.com/run-hub/run/tarball/0.46.1',
    entry_points={'console_scripts': ['run = run:program']},
    license='MIT License',
    long_description=long_description,
    maintainer='roll',
    maintainer_email='roll@respect31.com',
    name='runfile',
    include_package_data=True,
    install_requires=['clyde'], 
    packages=packages,
    platforms=['Unix'],
    url='https://github.com/run-hub/run',
    tests_require=['nose', 'coverage'],
    test_suite='nose.collector',
    version='0.46.1')
