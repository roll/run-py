import sys
import ast
import csv
import logging.config
from sugarbowl import cachedproperty
from clyde import Command, Option, ManpageFormatter, mixin
from .machine import Machine
from .metadata import version
from .settings import settings


class Program(Command):
    """Run main program.
    """

    # Public

    meta_formatter = ManpageFormatter

    def meta_execute(self, attribute=None, *arguments):
        for name in ['list', 'info', 'meta']:
            if getattr(self, name, False):
                if attribute is not None:
                    arguments = (attribute,) + arguments
                attribute = name
                break
        self.__run(attribute, *arguments)

    # Mixins

    @mixin
    def initiate_logging(self):
        logging.config.dictConfig(settings.logging_config)
        logger = logging.getLogger()
        if self.debug:
            logger.setLevel(logging.DEBUG)
        # TODO: rethink!
        if self.verbose:
            logger.setLevel(logging.INFO)
        if self.quiet:
            logger.setLevel(logging.ERROR)

    @mixin(require='help')
    def print_help(self):
        print(self.meta_format('help'))
        exit()

    @mixin(require='version')
    def print_version(self):
        print('Run ' + version)
        exit()

    # Options

    debug = Option(
        action='store_true',
        flags=['-d', '--debug'],
        help='Enable debug mode.',
    )

    stackless = Option(
        action='store_true',
        flags=['-c', '--stackless'],
        help='Enable stackless mode.',
    )

    filepath = Option(
        flags=['-f', '--filepath'],
        default=settings.filename,
        help='Runfile path.',
    )

    help = Option(
        action='store_true',
        flags=['-h', '--help'],
        help='Display this help message.',
    )

    info = Option(
        action='store_true',
        flags=['-i', '--info'],
        help='Display task information.',
    )

    list = Option(
        action='store_true',
        flags=['-l', '--list'],
        help='Display module tasks.',
    )

    meta = Option(
        action='store_true',
        flags=['-m', '--meta'],
        help='Display task meta.',
    )

    plain = Option(
        action='store_true',
        flags=['-p', '--plain'],
        help='Activate plain mode.',
    )

    quiet = Option(
        action='store_true',
        flags=['-q', '--quiet'],
        help='Enable quiet mode.',
    )

    verbose = Option(
        action='store_true',
        flags=['-v', '--verbose'],
        help='Enable verbose mode.',
    )

    version = Option(
        action='store_true',
        flags=['-V', '--version'],
        help='Display the program version.',
    )

    # Private

    def __run(self, attribute, *arguments):
        args, kwargs = self.__parse_arguments(arguments)
        try:
            self.__machine.run(attribute, *args, **kwargs)
        except Exception as exception:
            logging.getLogger(__name__).error(
                str(exception), exc_info=self.debug)
            sys.exit(1)

    def __parse_arguments(self, arguments):
        args = []
        kwargs = {}
        for element in next(csv.reader([''.join(arguments)])):
            parts = [self.__parse_literal(item.strip()) for item in
                     next(csv.reader([element], delimiter='='))]
            if len(parts) == 1:
                args.append(parts[0])
            elif len(parts) == 2:
                kwargs[parts[0]] = parts[1]
        return (args, kwargs)

    def __parse_literal(self, literal):
        try:
            value = ast.literal_eval(literal)
        except Exception:
            value = literal
        return value

    @cachedproperty
    def __machine(self):
        machine = Machine(
            filepath=self.filepath,
            stackless=self.stackless,
            plain=self.plain)
        return machine


program = Program(name='run')
