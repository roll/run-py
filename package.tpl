from setuptools import find_packages

package = {

	#Main

    'name': '{{ name }}',
	'version': '{{ version }}',
	'packages': find_packages('{{ name }}'),
	'include_package_data': True,
    'data_files': [
        ('/etc/bash_completion.d', ['run/console/completion/run.sh'])       
    ],
    'entry_points': {
        'console_scripts': [
            'run = run.console.script:script',
        ]
    },
    'install_requires': ['lib31>=0.5', 'ipclight>=0.5'],     
    'tests_require': ['nose'],
    'test_suite': 'nose.collector',
    
    #Description
    
    'author': '{{ author }}',
    'author_email': '{{ author_email }}',
    'maintainer': '{{ maintainer }}',
    'maintainer_email': '{{ maintainer_email }}',
    'license': '{{ license }}',    
    'url': 'https://github.com/{{ author|lower }}/{{ name|lower }}',
    'download_url': 'https://github.com/{{ author|lower }}/{{ name|lower }}/tarball/{{ version|lower }}',    
    'classifiers': {{ classifiers }},    
    'description': '{{ description }}',    
    'long_description': '''{{ long_description }}''',
        
}