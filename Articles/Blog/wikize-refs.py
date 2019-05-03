#!/usr/bin/env python

# run ./add_refs.py --help for documentation
def usage():
    return \
"""
%prog <infile.md>

Takes an input GitHub Markdown file with a series of footnotes
and reference-style links and re-formats them slightly to make
them behave more like Wikipedia style links.

This step should be performed as a post-processing step after
the author has finished all work on the original Markdown
document. It is possible to manually add more footnotes and
references after re-processing, just more tedius.

Examples...

To re-format a file using GitHub Markdown reference style links
to make the behave more like Wikipedia links...

    ./wikize-refs.py foo.md

...will produce a new file, foo-wikized.md, with the references
adjusted.
"""
from optparse import OptionParser
import re

def parse_args():
    """
    Parses arguments to wikize-refs.py.
    """
    parser = OptionParser(usage())
    opts, mdfiles = parser.parse_args()
    return opts, mdfiles

#
# Read the command line
#
opts, mdfiles = parse_args()
vopts = vars(opts)


other_lines = []
original_refs = []
reformed_refs = []
anchored_refs = []
for mdfile in mdfiles:
    with open(mdfile, 'r') as mdf:
        for mdfl in mdf.readlines():
            mdfparts = re.search("^\[([0-9]*)\]: (.*) \"(.*)\"$", mdfl)
            if mdfparts != None and len(mdfparts.groups()) == 3:
                ref_hdl = mdfparts.groups()[0]
                ref_url = mdfparts.groups()[1]
                ref_desc = mdfparts.groups()[2]
                original_refs += [mdfl]
                reformed_ref = "[%s]: #ref%s \"%s\""%(ref_hdl, ref_hdl, ref_desc)
                reformed_refs += [reformed_ref]
                anchored_ref = "<a name=\"ref%s\"></a><sup>%s</sup>[%s](%s)"%(ref_hdl, ref_hdl, ref_desc, ref_url)
                anchored_refs += [anchored_ref]
            else:
                other_lines += [mdfl]

with open("%s.wikized"%mdfile, 'w') as wmdf:
    for l in other_lines:
        wmdf.write(l)
    wmdf.write("\n<!---\n")
    for l in original_refs:
        wmdf.write(l)
    wmdf.write("\n--->\n")
    for l in reformed_refs:
        wmdf.write("%s\n"%l)
    wmdf.write("\n|References|\n")
    wmdf.write("|:---|\n")
    for l in anchored_refs:
        wmdf.write("|%s|\n"%l)
