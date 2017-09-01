#!/usr/bin/env python
"""
Validation driver to test the metadata of a single article.


    Usage: validate_article.py [options]

    Options:
      -h, --help            show this help message and exit
      -f PARAM_IFILENAME, --filename=PARAM_IFILENAME
                            [REQUIRED] Input filename
      -s PARAM_SPECFILENAME, --specfile=PARAM_SPECFILENAME
                            [REQUIRED] Constraints Specification Filename
      -d, --dry-run         [OPTIONAL] Dry Run. If enabled then don't modify any
                            files. Default: False
      -D, --debug           [OPTIONAL] Debug mode.  Default: False
      -V, --verbose         [OPTIONAL] Verbose mode.  Default: False
      --color=PARAM_COLOR_STDOUT
                            [OPTIONAL] Colorize the output. Use --color=tty for
                            ansi color.  Default: none

Returns: 0 if passed, 1 if failed.

"""
import os
import sys
from optparse import OptionParser

from colors import colorize
from metadata_validation_core import *
from utilities import *


def process_program_options():
    parser = OptionParser()
    parser.add_option("-f", "--filename", dest="param_ifilename",    default=None,              help="[REQUIRED] Input filename")
    parser.add_option("-s", "--specfile", dest="param_specfilename", default=None,              help="[REQUIRED] Constraints Specification Filename")
    parser.add_option("-d", "--dry-run",  action="store_true",       dest="param_dry_run",      default=False, help="[OPTIONAL] Dry Run. If enabled then don't modify any files. Default: %default")
    parser.add_option("-D", "--debug",    action="store_true",       dest="param_log_debug",    default=False, help="[OPTIONAL] Debug mode.  Default: %default")
    parser.add_option("-V", "--verbose",  action="store_true",       dest="param_log_verbose",  default=False, help="[OPTIONAL] Verbose mode.  Default: %default")
    parser.add_option(      "--color",    dest="param_color_stdout", default=None,              choices=["tty"],
                            help="[OPTIONAL] Colorize the output. Use --color=tty for ansi color.  Default: %default")
    (options, arguments) = parser.parse_args()

    # print out help if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if options.param_ifilename is None:
        parser.print_help()
        sys.exit(1)

    if options.param_specfilename is None:
        parser.print_help()
        sys.exit(1)

    # debug implies verbose mode.
    if options.param_log_debug:
        options.param_log_verbose = True

    if options.param_log_debug:
        print "Program Options:"
        for k,v in options.__dict__.items():
            print "    %-20s: %s"%(k,v)
        print "    %-20s: %s"%("working directory", os.path.dirname(os.path.realpath(__file__)))
        print ""

    return options



def main():
    """
    main function
    """
    passed = True

    program_options = process_program_options()

    specfile_data = load_metadata_specfile(program_options.param_specfilename, program_options)

    passed,failmsg = check_metadata_in_file(program_options.param_ifilename, specfile_data, program_options)

    if failmsg != "":
        print "ERROR: "
        print failmsg

    s = "Unknown"
    if passed is True:
        s = colorize("Green", "PASSED", terminal_type=program_options.param_color_stdout)
    else:
        s = colorize("Red", "FAILED", terminal_type=program_options.param_color_stdout)
    print "Check of '%s' %s"%(program_options.param_ifilename, s)

    return passed



if __name__ == "__main__":
    passed = main()

    rvalue = 0
    if passed is not True:
        rvalue = 1

    exit(rvalue)


