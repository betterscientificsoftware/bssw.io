#!/usr/bin/env python
"""
"""
import os
import os.path
import re
import sys

from optparse import OptionParser

from checked_dictionary import checked_dictionary
from colors    import colorize
from utilities import *


class article_metadata(checked_dictionary):
    """
    checked dictionary implementation for article metadata.
    """
    def __init__(self):
        """
        Default c'tor.

        """
        self.__init_default__()

        self.add_restriction("Publish", restrictions=["yes","no"])
        self.add_restriction("Categories", restrictions=["Planning",
                                                         "Development",
                                                         "Performance",
                                                         "Reliability",
                                                         "Collaboration",
                                                         "Skills"])
        self.add_restriction("Topics", restrictions=None)
        self.add_restriction_dependency("Topics", "Categories", "Planning", restrictions=["Improving productivity and sustainability",
                                                                                          "Requirements",
                                                                                          "Design",
                                                                                          "Software interoperability"])
        self.add_restriction_dependency("Topics", "Categories", "Development", restrictions=["Documentation",
                                                                                             "Version control",
                                                                                             "Configuration and builds",
                                                                                             "Deployment",
                                                                                             "Issue tracking",
                                                                                             "Refactoring",
                                                                                             "Software engineering",
                                                                                             "Development tools"])
        self.add_restriction_dependency("Topics", "Categories", "Performance", restrictions=["High-performance computing (HPC)",
                                                                                             "Performance at leadership computing facilities (LCFs)",
                                                                                             "Performance portability"])
        self.add_restriction_dependency("Topics", "Categories", "Reliability", restrictions=["Testing",
                                                                                             "Continuous integration testing",
                                                                                             "Reproducibility",
                                                                                             "Debugging"])
        self.add_restriction_dependency("Topics", "Categories", "Collaboration", restrictions=["Licensing",
                                                                                               "Strategies for more effective teams",
                                                                                               "Funding sources and programs",
                                                                                               "Projects and organizations",
                                                                                               "Software publishing and citation",
                                                                                               "Discussion forums, Q&A sites"])
        self.add_restriction_dependency("Topics", "Categories", "Skills", restrictions=["Personal productivity and sustainability",
                                                                                        "Online learning"])


        self.add_restriction("Tags", restrictions=None)
        self.add_restriction("Level", restrictions=[0,1,2,3])
        self.add_restriction("Prerequisites", restrictions=None)
        self.add_restriction("Aggregate", restrictions=["none","base","subresource","stand-alone and subresource"])



def process_program_options():
    parser = OptionParser()
    parser.add_option("-f", "--filename", dest="param_ifilename",    default=None,              help="[REQUIRED] Input filename")
    parser.add_option("-d", "--dry-run",  action="store_true",       dest="param_dry_run",      default=False, help="[OPTIONAL] Dry Run. If enabled then don't modify any files. Default: %default")
    parser.add_option("-D", "--debug",    action="store_true",       dest="param_log_debug",    default=False, help="[OPTIONAL] Debug mode.  Default: %default")
    parser.add_option("-V", "--verbose",  action="store_true",       dest="param_log_verbose",  default=False, help="[OPTIONAL] Verbose mode.  Default: %default")
    parser.add_option(      "--color",    dest="param_color_stdout", default=None,              choices=["tty"],
                            help="Use --color=tty for ansi color.  Default: %default")
    (options, arguments) = parser.parse_args()

    # print out help if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    if options.param_ifilename is None:
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


def load_textfile_to_stringlist(filename, program_options=None):
    """
    Load a text file and return it as a list of strings and strip
    traling whitespce.

    @param filename: [required] The input filename
    @param program_optons: [optional] program options (from OptionParser).
    """
    output = []

    print_verbose("Load input file: %s"%(filename), program_options)

    with open(filename, "r") as ifp:
        for line in ifp:
            output.append( line.rstrip() )

    print_verbose("Load input file: Complete", program_options)

    if program_options.param_log_debug is True:
        print_debug("file contents:", program_options)
        for line in output:
            print_debug(line, program_options)

    return output


def extract_metadata_entries(file_lines, program_options):
    """
    Extract the metadata key/value properties from the file
    """
    metadata = article_metadata()

    metadata_start = "<!---"
    metadata_stop  = "--->"

    in_metadata = False

    for line in file_lines:
        if not in_metadata and line == metadata_start:
            in_metadata = True
            continue

        if in_metadata and line == metadata_stop:
            in_metadata = False
            continue

        if in_metadata:
            tag,value = re.split(":", line, maxsplit=1)
            tag = tag.strip()
            value = value.strip()
            print_verbose("Metadata: {tag: %s, value: %s}"%(tag,value), program_options)
            metadata[tag] = value

    return metadata


def main():
    """
    """
    program_options = process_program_options()

    file_lines = load_textfile_to_stringlist(program_options.param_ifilename, program_options)

    print "Validate metadata for '%s': "%(program_options.param_ifilename),
    try:
        metadata = extract_metadata_entries(file_lines, program_options)
    except ValueError, msg:
        print "FAIL"
        print msg
        exit(1)

    print "PASS"


if __name__ == "__main__":
    main()
