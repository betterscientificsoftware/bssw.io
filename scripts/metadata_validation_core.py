#!/usr/bin/env python
"""
"""
import re

from utilities import *
from checked_multivalue_dictionary import checked_multivalue_dictionary



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



def get_metadata_section(file_lines, program_options):
    """
    Extract the metadata section from the file.
    """
    metadata_start_token = "<!---"
    metadata_stop_token  = "--->"
    metadata_file_lines  = []

    in_metadata  = False
    has_metadata = False

    for line in file_lines:

        line = line.strip()

        if not in_metadata and line == metadata_start_token:
            in_metadata = True
            has_metadata = True
            continue

        if in_metadata and line == metadata_stop_token:
            in_metadata = False
            break

        if in_metadata:
            metadata_file_lines.append(line)

    if in_metadata:
        msg = "Missing metadata section terminator '--->'."
        raise EOFError, msg
    if has_metadata is not True:
        msg = "Metadata section not found.  Requires starting token: '<!---'."
        raise EOFError, msg

    return metadata_file_lines


def tokenize_metadata(metadata_file_lines, program_options):
    """
    Tokenize the metadata in the file into key/value pairs.
    """
    metadata_token_list = []
    for line in metadata_file_lines:
        key,value_list = re.split(":", line, maxsplit=1)
        key = key.strip()
        for v in value_list.split(","):
            v = v.strip()
            if v is not None and v != "":
                metadata_token_list.append( (key,v) )

    return metadata_token_list



def check_metadata_tokens(metadata_tokens, mv_dict, program_options):
    """
    mv_dict is a checked_multivalue_dictionary with appropriate rules set up.
    """
    for key,value in metadata_tokens:
        mv_dict.append_property_value(key,value)
    return None



def check_metadata_stringlist(metadata_stringlist, program_options):
    """
    """
    output_passed = True
    metadata_tokens = tokenize_metadata(metadata_stringlist, program_options)

    mv_dict = setup_mv_dict()

    try:
        check_metadata_tokens(metadata_tokens, mv_dict, program_options)
    except ValueError, msg:
        print "ERROR:"
        print msg
        output_passed = False

    return output_passed


def check_metadata_in_file_lines(file_lines, program_options):
    """
    """
    output_passed = True
    try:
        metadata_lines = get_metadata_section(file_lines, program_options)
        output_passed = check_metadata_stringlist(metadata_lines, program_options)

    except EOFError, msg:
        print "ERROR:"
        print msg
        output_passed = False

    return output_passed


def check_metadata_in_file(filename, program_options):
    """
    """
    print "Check metadata for '%s': "%(filename)

    output_passed = True
    file_lines = load_textfile_to_stringlist(filename, program_options)
    output_passed = check_metadata_in_file_lines(file_lines, program_options)
    return output_passed




def setup_mv_dict():
    """
    Sets up the rules for the checked dictionary.
    """
    mv_dict = checked_multivalue_dictionary()
    mv_dict.add_restriction("Publish", restrictions=["yes", "no"])
    mv_dict.add_restriction("Categories", restrictions=["Planning",
                                                                        "Development",
                                                                        "Performance",
                                                                        "Reliability",
                                                                        "Collaboration",
                                                                        "Skills"])
    mv_dict.add_restriction("Topics", restrictions=None)
    mv_dict.add_restriction_dependency("Topics", "Categories", "Planning",
                                                       restrictions=["Requirements",
                                                                     "Design",
                                                                     "Software interoperability"])
    mv_dict.add_restriction_dependency("Topics", "Categories", "Development",
                                                       restrictions=["Documentation",
                                                                     "Version control",
                                                                     "Configuration and builds",
                                                                     "Deployment",
                                                                     "Issue tracking",
                                                                     "Refactoring",
                                                                     "Software engineering",
                                                                     "Development tools"])

    mv_dict.add_restriction_dependency("Topics", "Categories", "Performance",
                                                       restrictions=["High-performance computing",
                                                                     "Performance at LCFs",
                                                                     "Performance portability"])
    mv_dict.add_restriction_dependency("Topics", "Categories", "Reliability",
                                                       restrictions=["Testing",
                                                                     "Continuous integration testing",
                                                                     "Reproducibility",
                                                                     "Debugging"])
    mv_dict.add_restriction_dependency("Topics", "Categories", "Collaboration",
                                                       restrictions=["Licensing",
                                                                     "Strategies for more effective teams",
                                                                     "Funding sources and programs",
                                                                     "Projects and organizations",
                                                                     "Software publishing and citation",
                                                                     "Discussion forums, Q&A sites"])
    mv_dict.add_restriction_dependency("Topics", "Categories", "Skills",
                                                       restrictions=["Personal productivity and sustainability",
                                                                     "Online learning"])

    mv_dict.add_restriction("Tags", restrictions=None)

    mv_dict.add_restriction("Level", restrictions=[0,1,2,3])

    mv_dict.add_restriction("Prerequisites", restrictions=None)

    mv_dict.add_restriction("Aggregate", restrictions=["none","base","subresource","stand-alone and subresource"])

    return mv_dict


