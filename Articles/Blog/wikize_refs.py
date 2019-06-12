#!/usr/bin/env python

# run ./wikize_refs.py --help for documentation

from optparse import OptionParser
import re, os, stat

def warning_msg(mdfile):
    return "<!--- WARNING: DO NOT EDIT! Auto-generated with wikize_refs.py from %s --->\n"%mdfile

def usage():
    return \
"""
%prog <infile.md>

Renumbers 1...N and re-formats, slightly, footnotes and a series of
reference style links in a GitHub Markdown file so that the article's
footnote links behave more Wikipedia-like. In the new file, the original
reference style link definitions are copied over but commented out by
bracketing in <!--- and --->. The renumbered and re-formatted links are
bi-level. Footnotes in the content link to entries in a table of 
references at the bottom of the document. Items in the table of references
link off-page to their intended destinations. The resulting file is still
GitHub flavored Markdown with a minimal amount of embedded HTML.
For more information, see https://github.com/betterscientificsoftware/\
betterscientificsoftware.github.io/blob/master/Articles/Blog/\
ReferencesInMarkdownHybridApproach.md

By default, infile.md is moved to infile.src.md and the new file is
given the name infile.md and is made read-only. However, you can set
the name of the output file instead and disable the read-only setting.
By default, failed sanity checks cause an abort. However, this can
be disabled by setting them to warn.

To process a file...

    ./wikize_refs.py foo.md

...moves foo.md to foo.src.md and the new file is foo.md
"""

def parse_args():
    """
    Parses arguments to wikize_refs.py.
    """
    parser = OptionParser(usage())

    parser.add_option("--warn",
                      default=False,
                      action="store_true",
                      help="Warn instead of error during sanity checks.")

    parser.add_option("--no-readonly",
                      default=False,
                      action="store_true",
                      help="Disable making output file read-only.")

    parser.add_option("-o", "--outfile",
                      help="Specify output file name.")

    opts, mdfiles = parser.parse_args()

    if not mdfiles:
        print "Must include the name of a markdown file to process."
        exit(1)

    return opts, mdfiles[0]

#
# Process the original md file grepping for
# footnotes and reference definitions
#
def process_input_file(filename):
    fn_handles = set()
    other_lines = []
    original_refs = []
    ref_map = {}
    in_comment = False
    with open(filename, 'r') as mdf:
        for mdfl in mdf.readlines():
            # grep for ^[xxx]: URL "Short Description {Formal Bibliographic data}"$
            mdfparts = re.search("^\[([a-zA-Z0-9_-]*)\]: (.*) \"(.*) {(.*)}\"$", mdfl)
            if in_comment and re.match("--->", mdfl):
                in_comment = False
            elif re.match("<!---", mdfl):
                in_comment = True
            if not in_comment and mdfparts != None and len(mdfparts.groups()) == 4:
                ref_hdl = mdfparts.groups()[0]
                ref_url = mdfparts.groups()[1]
                ref_desc = mdfparts.groups()[2]
                ref_bib = mdfparts.groups()[3]
                if ref_hdl in ref_map:
                    print "Error: repeated reference definition handle", ref_hdl
                    exit(1)
                ref_map[ref_hdl] = [ref_desc, ref_url, ref_bib]
                ref_map[ref_hdl].append(len(ref_map))
                original_refs += [mdfl]
            elif not in_comment: # handle up to 3 footnotes in a single <sup></sup>
                fns1 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\]</sup>", mdfl)
                fn_handles = fn_handles.union(set(fns1))
                fns2 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mdfl)
                for fn in fns2: fn_handles = fn_handles.union(set(fn))
                fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mdfl)
                for fn in fns3: fn_handles = fn_handles.union(set(fn))
                other_lines += [mdfl]
            else:
                other_lines += [mdfl]

    return fn_handles, other_lines, original_refs, ref_map

#
# Sanity checks for footnote references and the reference list
#    - ensure every footnote references an existing item in the ref list
#    - ensure every ref list item is referenced at least once
#
def sanity_checks(fn_handles, ref_map, warn):
    ref_handles = set(ref_map.keys())
    missing_refs = fn_handles - ref_handles
    if missing_refs:
        print "Some footnotes never appear in the references..."
        print "   ", [x for x in missing_refs]
        if not warn:
            print "Correct above issues and re-try..."
            exit(1)

    missing_fns = ref_handles - fn_handles
    if missing_fns:
        print "Some references never appear in a footnote..."
        print "   ", [x for x in missing_fns]
        if not warn:
            print "Correct above issues and re-try..."
            exit(1)

def generate_output_file_lines(mdfile, other_lines, original_refs, ref_map):
    outlines = []

    #
    # write warning comment about this being auto-generated
    #
    outlines.append(warning_msg(mdfile))

    #
    # Write all non-reference definition lines (e.g. article content) first
    #
    for ol in other_lines:
        # Filter any footnotes in this line with their new re-numbered instances.
        # Since we're re-filtering the same line multiple times, we replace
        # <sup></sup> with <pus></pus> to avoid collisions and then undue that
        # filter in the last step
        fns1 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\]</sup>", ol)
        for fn in fns1:
            ol = re.sub("<sup>\[%s\]</sup>"%fn, "<pus>[%d]</pus>"%ref_map[fn][3], ol)
        fns2 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", ol)
        for fn in fns2:
            ol = re.sub("<sup>\[%s\],\[%s\]</sup>"%(fn[0],fn[1]), "<pus>[%d],[%d]</pus>"%(ref_map[fn[0]][3],ref_map[fn[1]][3]), ol)
        fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", ol)
        for fn in fns3:
            ol = re.sub("<sup>\[%s\],\[%s\],\[%s\]</sup>"%(fn[0],fn[1],fn[2]), "<pus>[%d],[%d],[%d]</pus>"%(ref_map[fn[0]][3],ref_map[fn[1]][3],ref_map[fn[2]][3]), ol)
        ol = re.sub("<pus>","<sup>", ol)
        ol = re.sub("</pus>","</sup>", ol)
        outlines.append(ol)

    #
    # Write original set of refs embedded in comments
    #
    outlines.append("\n<br>\n\n<!---\n")
    for l in original_refs:
        outlines.append(l)
    outlines.append("\n--->\n<br>\n\n")

    #
    # Write link definitions with links to anchors in reference table
    #
    remapped_ref_map = {v[3]:[v[0],v[1],v[2],k] for k,v in ref_map.items()}
    for k,v in sorted(remapped_ref_map.items()):
        outlines.append("[%d]: #ref%d \"%s\"\n"%(k, k, v[0]))

    #
    # Finally, write the references and off-page links as a table
    # where each row defines an anchor for one of the link definitions, above
    #
    outlines.append("\n<br>\n\n")
    outlines.append("References | &nbsp;\n")
    outlines.append(":--- | :---\n")
    for k,v in sorted(remapped_ref_map.items()):
        if (not v[0] or v[0].isspace()) and (not v[2] or v[2].isspace()):
            outlines.append("<a name=\"ref%d\"></a>%d | %s\n"%(k, k, v[1]))
        elif v[0] in v[2]:
            outlines.append("<a name=\"ref%d\"></a>%d | [%s](%s)\n"%(k, k, v[2], v[1]))
        else:
            outlines.append("<a name=\"ref%d\"></a>%d | [%s %s](%s)\n"%(k, k, v[0], v[2], v[1]))

    #
    # write warning comment about this being auto-generated
    #
    outlines.append(warning_msg(mdfile))

    return outlines

def write_output_file(outlines, in_filename, out_filename, no_readonly):
    outfname = out_filename
    if not out_filename:
        outfname = "%s-wikized.md"%os.path.splitext(in_filename)[0]
    with open(outfname, 'w') as outf:
        outf.writelines(["%s" % line for line in outlines])
    if not no_readonly:
        os.chmod(outfname, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)

def main():

    #
    # Process command line
    #
    opts, mdfile = parse_args()
    vopts = vars(opts)

    #
    # Process the input file, collecting up footnotes and refs
    # various types of lines into different lists and maps
    #
    fn_handles, \
    other_lines, \
    original_refs, \
    ref_map = \
    process_input_file(mdfile)

    #
    # Check basic sanity of refs
    #
    sanity_checks(fn_handles, ref_map, vopts['warn'])

    #
    # Build up the list of lines for output file
    #
    outlines = \
    generate_output_file_lines(mdfile, other_lines, original_refs, ref_map)

    #
    # Write the output file to a temporary file
    #
    write_output_file(outlines, mdfile, vopts['outfile'], vopts['no_readonly'])

#
# So this python script can be used both as a shell command
# and as an imported python module.
#
if __name__ == '__main__':
    main()
