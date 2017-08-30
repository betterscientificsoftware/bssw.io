#!/usr/bin/env python
"""
Test validation on metadata sections
"""
from pprint import pprint
from metadata_validation_core import *


test_strings = [
    """
    <!---
    Publish: yes
    Categories: Planning, Reliability,
    Topics: Testing, Debugging, Design,
    Tags: training, webinar,
    Level: 2
    Prerequisites: defaults
    Aggregate: subresource
    --->
    """,

    """
    <!---
    Publish: yes
    Categories: Planning,
    Topics: Testing, Debugging, Design,
    Tags: training, webinar,
    Level: 2
    Prerequisites: defaults
    Aggregate: subresource
    --->
    """,

    """
    <!---
    --->
    """,

    """
    <!--
    --->
    """,

    """
    <!---
    -->
    """,

    """
    """,
]


def to_stringlist(text):
    stringlist = []
    for line in text.split( "\n" ):
        line = line.rstrip()
        stringlist.append(line)
    return stringlist


def main():
    """
    Starts here...
    """

    entry_idx = 0
    for entry in test_strings:

        print "Check entry %d: "%(entry_idx),
        stringlist = to_stringlist(entry)

        passed,failmsg = check_metadata_in_file_lines(stringlist, program_options=None)

        if passed is True:
            print "PASSED"
        else:
            print "FAILED"
        print ""

        entry_idx += 1


    print "Done."



if __name__ == "__main__":
    main()
