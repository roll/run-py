# Block: caution
# TO MAKE CHANGES USE "meta" DIRECTORY (see packgram docs).

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
    download_url='https://github.com/respect31/run/tarball/0.41.0',
    entry_points={'console_scripts': ['run = run:program']},
    license='MIT License',
    long_description=long_description,
    maintainer='roll',
    maintainer_email='roll@respect31.com',
    name='runfile',
    include_package_data=True,
    install_requires=['sugarbowl', 'box>=0.44', 'color>=0.3', 'clyde>=0.5', 'dialog>=0.4', 'find>=0.3', 'render>=0.3', 'claire>=0.7'], 
    packages=packages,
    platforms=['Unix'],
    url='https://github.com/respect31/run',
    tests_require=['nose', 'coverage'],
    test_suite='nose.collector',
    version='0.41.0')
