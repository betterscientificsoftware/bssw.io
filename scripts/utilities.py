#!/usr/bin/env python
"""
Core validation functions
"""
from colors import colorize



def print_debug(text, program_options):
    """
    Optionally prints DEBUG messages.

    @param text: The message text to print out.
    @param program_options: A program options object (from optparse.OptionParser),
                            or an object that has the following members:
                            - 'param_color_stdout' : what kind of colorization is allowed (currently 'tty' or None are allowed).
                            - 'param_log_debug' : True/False to control whether or not the message is printed.

    """
    if program_options is not None and program_options.param_log_debug is True:
        prefix_str = colorize("red", "[D] ", program_options.param_color_stdout)
        print "%s%s"%(prefix_str, text)
    return None



def print_verbose(text, program_options):
    """
    Optionally prints VERBOSE messages.

    @param text: The message text to print out.
    @param program_options: A program options object (from optparse.OptionParser),
                            or an object that has the following members:
                            - 'param_color_stdout' : what kind of colorization is allowed (currently 'tty' or None are allowed).
                            - 'param_log_debug' : True/False to control whether or not the message is printed.

    """
    if program_options is not None and program_options.param_log_verbose is True:
        prefix_str = colorize("cyan", "[V] ", program_options.param_color_stdout)
        print "%s%s"%(prefix_str, text)
    return None



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

    if program_options.param_log_debug is True:
        print_debug("file contents:", program_options)
        for line in output:
            print_debug(line, program_options)

    print_verbose("Load input file: Loaded %d lines"%(len(output)), program_options)
    print_verbose("Load input file: Complete", program_options)


    return output


