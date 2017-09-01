#!/usr/bin/env python
"""
Core validation functions
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



def string_to_stringlist(text, program_options=None):
    """
    Convert a (possibly) multi-line string into a list of strings.
    """
    return text.splitlines()



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
    print_verbose("Extract metadata lines", program_options)

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
        msg = "Metadata section not found. Missing metadata section end token: '--->'."
        raise EOFError, msg
    if has_metadata is not True:
        msg = "Metadata section not found. Missing metadata section start token: '<!---'."
        raise EOFError, msg

    print_verbose("Extract metadata lines - Complete", program_options)

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



def check_metadata_stringlist(metadata_stringlist, specfile_data, program_options):
    """
    Check the content of the metadata (a list of strings, one for each line)
    and return True or False if the metadata content passed.

    Returns (tuple):
        bool: True if the metadata passed
              False otherwise.
        str : "" if test passed
              reasons for failure if the test failed.
    """
    output_passed = True
    output_info   = ""

    # Fail if there's nothing in metadata...
    if 0 == len(metadata_stringlist):
        return False

    mv_dict = setup_mv_dict_from_specification(specfile_data, program_options)

    metadata_tokens = tokenize_metadata(metadata_stringlist, program_options)

    try:
        check_metadata_tokens(metadata_tokens, mv_dict, program_options)
    except ValueError, msg:
        output_passed = False
        output_info   = msg

    return output_passed, output_info



def get_metadata_lines_from_file(filename, program_options):
    """
    Load a file and pull out the meta lines into a list of strings.
    """
    metadata_lines = []
    file_lines = load_textfile_to_stringlist(filename, program_options)
    try:
        metadata_lines = get_metadata_section(file_lines, program_options)
    except EOFError, msg:
        print "ERROR:"
        print msg,"\n"

    return metadata_lines



def check_metadata_in_file_lines(file_lines, specfile_data, program_options):
    """
    """
    output_passed  = True
    metadata_lines = []
    try:
        metadata_lines = get_metadata_section(file_lines, program_options)
        output_passed,output_failmsg = check_metadata_stringlist(metadata_lines, specfile_data, program_options)

    except EOFError, msg:
        output_passed  = False
        output_failmsg = msg
        print_debug("ERROR:", program_options)
        print_debug(msg, program_options)

    if program_options.param_log_verbose is True and len(metadata_lines)>0:
        print_debug("===== metadata begin =====", program_options)
        for line in metadata_lines:
            print_debug(line, program_options)
        print_debug("===== metadata end =====", program_options)

    return output_passed,output_failmsg



def check_metadata_in_file(filename, specfile_data, program_options):
    """
    """
    print_debug("Check metadata for '%s': "%(filename), program_options)

    output_passed = True
    file_lines = load_textfile_to_stringlist(filename, program_options)
    output_passed,output_failmsg = check_metadata_in_file_lines(file_lines, specfile_data, program_options)

    return output_passed,output_failmsg



def setup_mv_dict_from_specification(specfile_data, program_options=None):
    """
    Set up the rules for the checked dictionary from specfile data.
    See load_metadata_specfile() for information on the required data structure.
    """
    print_debug("Configuring Restrictions", program_options)

    mv_dict = checked_multivalue_dictionary()

    if not isinstance(specfile_data, list):
        raise TypeError, "expected a list"

    for entry in specfile_data:

        if 'R' == entry['type']:
            print_debug("ADD RESTRICTION     : '%s' CAN HAVE '%s'"%(entry['property_name'], entry['allowable_value']), program_options)
            mv_dict.add_restriction(entry['property_name'], restrictions=entry['allowable_value'])

        if 'D' == entry['type']:
            print_debug("ADD RESTRICTION DEP : '%s' CAN HAVE '%s' IF '%s' HAS '%s'"%(entry['property_name'],
                                                  entry['allowable_value'],
                                                  entry['dependency_name'],
                                                  entry['dependency_value']), program_options)

            mv_dict.add_restriction_dependency(property_name=entry['property_name'],
                                               dependency_name = entry['dependency_name'],
                                               dependency_value = entry['dependency_value'],
                                               restrictions=entry['allowable_value'])

        if 'N' == entry['type']:
            print_debug("ADD RESTRICTION NONE: '%s'"%(entry['property_name']), program_options)
            mv_dict.add_restriction(property_name=entry['property_name'], restrictions=None)

    print_debug("%s"%(mv_dict), program_options)

    return mv_dict



def load_metadata_specfile(filename, program_options=None):
    """
    Load the metadata spec file.

    Returns: A list of dicts:
    [
      {'type': 'R', 'property_name': <string>,   'allowable_value':  <string>
      }
      {'type': 'D', 'property_name': <string>,   'allowable_value':  <string>
                    'dependency_name': <string>, 'dependency_value': <string>
      }
      {'type': 'N', 'property_name': <string>
      }
    ]

    Type R entries are simple restrictions in which keys with property_name may only have values
    in the allowable_value list.
    Type D entries have restrictions based on a dependency to another property.  dependency_name
    contains the property_name this property has a dependency on.  Dependency_value is the value
    of the other property that we're applying a restriction to for allowable_value.

    For example:
        property_name: FOO
        dependency_name: BAR
        dependency_value: baz
        allowable_value: biff

        Says that the property FOO can contain the value 'biff' if the value of BAR is 'baz'

    """
    print_verbose("Load metadata spec file: %s"%(filename), program_options)

    specfile_data = []

    ifp = open(filename, "r")

    for line in ifp:
        line = line.strip()

        if len(line)==0:
            continue

        if line[0] == "#":
            continue

        line_type = line[0].upper()

        if line_type not in ['R', 'D', 'N']:
            raise ValueError, "Bad value in column 0.  Allowable values are 'R' or 'D' but I got a '%s'"%(line[0])

        line = line[1:].strip()

        line_contents = [x.strip() for x in line.split(',')]

        print_debug("%s: %s"%(line_type, line_contents), program_options)

        entry = { 'type': line_type }
        if line_type == 'R':
            entry['property_name']   = line_contents[0]
            entry['allowable_value'] = line_contents[1]
        elif line_type == 'D':
            entry['property_name']    = line_contents[0]
            entry['dependency_name']  = line_contents[1]
            entry['dependency_value'] = line_contents[2]
            entry['allowable_value']  = line_contents[3]
        elif line_type == 'N':
            entry['property_name'] = line_contents[0]
        else:
            raise ValueError

        specfile_data.append(entry)

    ifp.close()

    print_verbose("Load metadata spec file: Complete", program_options)

    return specfile_data




