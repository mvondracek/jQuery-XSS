#!/usr/bin/env python3
import logging
import sys
import warnings
from contextlib import closing
from enum import unique, Enum
from typing import Optional, Sequence

from jqueryxss import __author__ as package_author, __date__ as package_date, __version__ as package_version
from jqueryxss.config import Config
from jqueryxss.core import analyse_file, InvalidInput

__version__ = package_version
__date__ = package_date
__author__ = package_author

LOGGER = logging.getLogger(__name__)


@unique
class ExitCode(Enum):
    """
    Return codes.
    Some are inspired by sysexits.h.
    """
    EX_OK = 0
    """Program terminated successfully."""

    UNKNOWN_FAILURE = 1
    """Program terminated due to unknown error."""

    ARGUMENTS = 2
    """Incorrect or missing arguments provided."""

    EX_DATAERR = 65
    """The input data was incorrect in some way."""

    KEYBOARD_INTERRUPT = 130
    """Program received SIGINT."""


def main(argv: Optional[Sequence[str]]) -> ExitCode:
    """
    :raises InvalidInput: on syntax error in provided JavaScript source code
    """
    logging.captureWarnings(True)
    warnings.simplefilter('always', ResourceWarning)

    with closing(Config.from_args(argv[1:])) as config:  # argv[0] is program name
        # On error with parsing argument, program was terminated by `Config.from_args` with exit code 2 corresponding to
        # `ExitCode.ARGUMENTS`. If arguments contained -h/--help or --version, program was terminated with exit code 0,
        # which corresponds to `ExitCode.E_OK`
        if config.logging_level:
            logging.basicConfig(format='%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s',
                                level=config.logging_level)
        else:
            logging.disable(logging.CRITICAL)
        LOGGER.debug('Config parsed from args.')

        # raises InvalidInput: on syntax error in provided JavaScript source code
        analyse_file(config.input)
    return ExitCode.EX_OK


if __name__ == '__main__':
    exitcode: ExitCode = ExitCode.EX_OK
    try:
        exitcode = main(sys.argv)
    except InvalidInput as e:
        LOGGER.critical(e)
        exitcode = ExitCode.EX_DATAERR
    except KeyboardInterrupt:
        LOGGER.info('received KeyboardInterrupt, stopping')
        exitcode = ExitCode.KEYBOARD_INTERRUPT
    except Exception as e:
        print(str(e), file=sys.stderr)
        exitcode = ExitCode.UNKNOWN_FAILURE
    sys.exit(exitcode.value)
