import argparse
import logging
import sys
from typing import Optional, TextIO, Sequence

from jqueryxss import __version__, __date__, __author__


class Config:
    PROGRAM_DESCRIPTION = 'jQuery XSS Static Analyser'
    LOGGING_LEVELS_DICT = {'debug': logging.DEBUG,
                           'warning': logging.WARNING,
                           'info': logging.INFO,
                           'error': logging.ERROR,
                           'critical': logging.ERROR,
                           'disabled': None,  # logging disabled
                           }
    LOGGING_LEVEL_DEFAULT = 'info'

    def __init__(self, logging_level: Optional[int], input_: TextIO, locations_only: bool):
        self.logging_level: Optional[int] = logging_level
        self.input: TextIO = input_
        self.locations_only: bool = locations_only

    def close(self):
        self.input.close()

    @classmethod
    def init_parser(cls) -> argparse.ArgumentParser:
        """
        Initialize argument parser.
        :return: initialized parser
        """
        parser = argparse.ArgumentParser(
            description=cls.PROGRAM_DESCRIPTION,
            epilog="{}, {}.".format(__author__, __date__)
        )
        parser.add_argument('-i', '--input',
                            type=argparse.FileType('r'),
                            # default='-',
                            required=True,
                            help='input file with JavaScript (\'-\' for stdin)',
                            metavar='FILE',
                            )
        parser.add_argument('-v', '--verbosity',
                            # NOTE: The type is called before check against choices. In order to display logging level
                            # names as choices, name to level int value conversion cannot be done here. Conversion is
                            # done after parser call in `self.from_args`.
                            default=cls.LOGGING_LEVEL_DEFAULT,
                            choices=cls.LOGGING_LEVELS_DICT,
                            help='logging verbosity level (default: %(default)s)'
                            )
        parser.add_argument('-l', '--locations-only',
                            action='store_true',
                            default=False,
                            help='output only locations of detected unsafe jQuery method calls',
                            )
        parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
        return parser

    @classmethod
    def from_args(cls, args: Optional[Sequence[str]] = sys.argv):
        """
        Return Config object parsed from command line arguments.
        `"By default, the argument strings are taken from sys.argv"
            <https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args>`_
        :param args: argument strings
        """
        # NOTE: Call to parse_args with namespace=self does not set logging_level with default value, if argument is not
        # in provided args, for some reason.
        parsed_args = cls.init_parser().parse_args(args=args)

        # name to value conversion as noted in `self.init_parser`
        logging_level = cls.LOGGING_LEVELS_DICT[parsed_args.verbosity]

        return cls(logging_level, parsed_args.input, parsed_args.locations_only)
