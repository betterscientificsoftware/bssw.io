#!/bin/bash
# Extract CSV file containing filenames and tags used
# Results can be imported into a spreadsheet
#
# Note that "template" files will cause multiple entries, and extras
# currently need to be deleted manually.

grep -i tags: *.md | \
    sed 's/\ *Tags: /,/' | \
    grep -v "^\[" | \
    grep -v -i "^specify"
