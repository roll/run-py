import os
import re
import json
from copy import deepcopy
from argparse import ArgumentParser
from lib31.decorators.cachedproperty import cachedproperty
from lib31.functions.load import load
from .settings import settings
from .exceptions.exit import (HelpExit, 
                              ErrorExit, 
                              DriverIsNotFoundExit, 
                              LanguageIsNotSupportedExit,
                              RunfileIsNotFoundExit,
                              RunfileIsNotReadableExit)

class Command(object):
    
    EXCLUDE = [
        'driver',
        'language',
    ]

    def __init__(self, argv):
        self._argv = argv
        self._boot()
        
    def __getattr__(self, name):
        return getattr(self._parsed, name)

    @property
    def driver(self):
        driver = self._parsed.driver
        language = self.language
        attempts = []
        if driver:
            attempts.append(driver)
        else:
            if language:
                for pattern in settings.drivers.values():
                    name = pattern.format(
                        language=language,
                        language_capitalized=
                        language.capitalize()
                    )
                    attempts.append(name)
        for name in attempts:
            try:
                try:
                    Driver = load(name)
                except ImportError:
                    Driver = load(name, path=[os.getcwd()])
                driver = Driver(self)
                break
            except ImportError:
                continue
        else:
            driver = None
        if not driver:
            raise DriverIsNotFoundExit(
                attempts=attempts,
                language=language
            )
        return driver

    @property
    def language(self):
        language = self._parsed.language
        runfile = self.runfile
        attempts = []
        if not language:            
            for name, pattern in settings.languages.items():
                if re.search(pattern, runfile):
                    language = name
                    break
                else:
                    attempts.append(name)                    
        if not language:            
            raise LanguageIsNotSupportedExit(
                attempts=attempts,                    
                runfile=runfile
            )                
        return language

    @property
    def ishelp(self):
        return self._parsed.ishelp
    
    @property
    def runfile(self):
        runfile = self._parsed.runfile
        language = self._parsed.language
        runfile = os.path.abspath(runfile)
        dirname = os.path.dirname(runfile)
        basename = os.path.basename(runfile)
        patterns = []           
        patterns.append('^{runfile}'.
                        format(runfile=re.escape(basename)))
        if language in settings.languages:
            patterns.append(settings.languages[language])
        matched = []            
        attempts = []
        for name in os.listdir(dirname):
            if reduce(lambda ismatched, pattern: 
                      ismatched and re.search(pattern, name),
                      patterns,
                      True):
                matched.append(name)
            else:
                attempts.append(name)
        if matched:
            #Select shortest matched name to join with dirname
            result = os.path.join(dirname, sorted(matched)[0])
        else:
            result = ''
        if not self.ishelp:
            if not result:
                raise RunfileIsNotFoundExit(
                    attempts=attempts,
                    patterns=patterns,
                    dirname=dirname,
                    basename=basename,                    
                    language=language
                )
            if not self._check_file_is_readable(result):
                raise RunfileIsNotReadableExit(
                    runfile=runfile
                )
        return result       
    
    @property
    def runclass(self):
        return self._parsed.runclass
    
    @property
    def function(self):
        function = self._parsed.function
        if self.ishelp:
            if not function:
                raise HelpExit()
        return function
    
    @property
    def arguments(self):
        return self._parsed.arguments

    @property
    def json(self):
        data = {}
        for name in self._parsed.__dict__:
            if name not in self.EXCLUDE:
                data[name] = getattr(self, name)
        return json.dumps(data)

    @property
    def usage(self):
        return self._parser.format_usage().strip()
    
    @property
    def help(self):
        return self._parser.format_help().strip()
    
    def add_option(self, *args, **kwargs):
        self._parser.add_argument(*args, **kwargs)
        self._parsed = False        
        
    def add_argument(self, *args, **kwargs):
        self._parser.add_argument(*args, **kwargs)
        self._parsed = False

    def _boot(self):
        for name, data in deepcopy(settings.arguments).items():
            self.add_argument(name, **data)
        for name, data in deepcopy(settings.options).items():
            self.add_option(*data.pop('flags'), dest=name, **data)

    @cachedproperty
    def _parsed(self):
        return self._parser.parse_args(self._argv[1:])
    
    @_parsed.setter
    def _parsed(self, value):
        if value == False:
            cachedproperty.reset(self, '_parsed')        
        
    @cachedproperty
    def _parser(self):
        return CommandArgumentParser(**settings.parser)
    
    @staticmethod
    def _check_file_is_readable(runfile):
        try:
            with open(runfile):
                pass
        except IOError:
            return False
        else:
            return True
    
    
class CommandArgumentParser(ArgumentParser):
    
    def error(self, message):
        raise ErrorExit(message)