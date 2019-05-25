#!/usr/bin/env python

# run ./wikize-refs.py --help for documentation

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
references. Items in the table of references link off-page to their
intended destinations. The resulting file is still GitHub flavored
Markdown but with a minimal amount of embedded HTML.

For our purposes, GitHub Markdown reference style links should be
formated as follows...

[<LINK-ID>]: <URL> "<DESC> {<BIB-DATA>}"

where...

all characters outside <> delimeters are required
<LINK-ID> is any alpha-numeric text (must start at col 0)
<URL> is the actual url of the  an on-line reference
<DESC> is a short description/summary of the referenced item
<BIB-DATA> is a full bibliographic entry (Optional. If none use {})

Some sanity checking is performed.

Examples...

To process a file...

    ./wikize-refs.py foo.md

...produces foo-wikized.md, with the references adjusted.
"""

from optparse import OptionParser
import re, os, stat, tempfile

def parse_args():
    """
    Parses arguments to wikize-refs.py.
    """
    parser = OptionParser(usage())

    parser.add_option("--warn",
                      default=False,
                      action="store_true",
                      help="[Optional] Warn instead of error during sanity checks.")

    parser.add_option("--no-rdonly",
                      default=False,
                      action="store_true",
                      help="Disable making output file read-only.")

    parser.add_option("-o", "--outfile",
                      help="Specify output file name instead of ")

    opts, mdfiles = parser.parse_args()
    return opts, mdfiles

#
# Process the original md file grepping for
# footnotes and reference definitions
#
def process_input_file(filename):
    fn_handles = set()
    other_lines = []
    comment_lines = []
    original_refs = []
    ref_map = {}
    in_comment = False
    with open(filename, 'r') as mdf:
        for mdfl in mdf.readlines():
            # grep for ^[xxx]: URL "Short Description {Formal Bibliographic data}"$
            mdfparts = re.search("^\[([a-zA-Z0-9_-]*)\]: (.*) \"(.*) {(.*)}\"$", mdfl)
            if in_comment:
                comment_lines += [mdfl]
            elif re.match("<!---", mdfl):
                in_comment = True
                comment_lines += [mdfl]
            elif re.match("--->", mdfl):
                in_comment = False
                comment_lines += [mdfl]
            elif mdfparts != None and len(mdfparts.groups()) == 4:
                ref_hdl = mdfparts.groups()[0]
                ref_url = mdfparts.groups()[1]
                ref_desc = mdfparts.groups()[2]
                ref_bib = mdfparts.groups()[3]
                if ref_hdl in ref_map:
                    print "Error: repeated reference definition handle", ref_hdl
                    exit()
                ref_map[ref_hdl] = [ref_desc, ref_url, ref_bib]
                ref_map[ref_hdl].append(len(ref_map))
                original_refs += [mdfl]
            else: # handle up to 3 footnotes in a single <sup></sup>
                fns1 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\]</sup>", mdfl)
                fn_handles = fn_handles.union(set(fns1))
                fns2 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mdfl)
                for fn in fns2: fn_handles = fn_handles.union(set(fn))
                fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mdfl)
                for fn in fns3: fn_handles = fn_handles.union(set(fn))
                other_lines += [mdfl]

    return fn_handles, other_lines, comment_lines, original_refs, ref_map

#
# Sanity checks for footnote references and the reference list
#    - ensure every footnote references an existing item in the ref list
#    - ensure every ref list item is referenced at least once
#
def sanity_checks(fn_handls, ref_map, warn):
    ref_handles = set(ref_map.keys())
    missing_refs = fn_handles - ref_handles
    if missing_refs:
        print "Some footnotes never appear in the references..."
        print "   ", [x for x in missing_refs]
        if not warn:
            print "Correct above issues and re-try..."
            exit()

    missing_fns = ref_handles - fn_handles
    if missing_fns:
        print "Some references never appear in a footnote..."
        print "   ", [x for x in missing_fns]
        if not warn:
            print "Correct above issues and re-try..."
            exit()

def generate_output_file_lines(other_lines, original_refs, ref_map, comment_lines):
    outlines = []

    #
    # write warning comment about this being auto-generated
    #
    outlines.append("<!--- WARNING: Auto-generated with wikize-refs.py from %s --->\n"%mdfile)

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
    # Write all comment lines
    #
    outlines.append("\n<br>\n\n")
    for l in comment_lines:
        outlines.append(l)
    outlines.append("\n")

    #
    # write warning comment about this being auto-generated
    #
    outlines.append("<!--- WARNING: Auto-generated with wikize-refs.py from %s --->\n"%mdfile)

    return outlines

def write_output_temp_file(outlines):
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as outf:
        out.writelines(["%s\n" % item  for item in outlines])
        return tempfile.name

def rename_files(in_filename, tmp_filename, out_filename, rd_only):
    if not out_filename:
        new_in_filename = "%s.src.md"%os.path.splitext(in_filename)[0]
        if os.path.exists(new_in_filename):
            print "Cannot rename \"%s\" to \"%s\" because it already exists"%(in_filename, new_in_filename)
            exit()
        os.rename(in_filename, new_in_filename)
        os.rename(tmp_filename, in_filename)
        if not vopts['no_rdonly']:
            os.chmod(in_filename, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)
    else:
        if os.path.exists(out_filename):
            print "Cannot write to \"%s\" because it already exists"%out_filename
            exit()
        os.rename(tmp_filename, out_filename)
        if not vopts['no_rdonly']:
            os.chmod(out_filename, stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)

def main():

    #
    # Process command line
    #
    opts, mdfile = parse_args()
    vopts = vars(opts)

    #
    # Process the input file, collecting up refs and various
    # kinds of lines into different lists and maps
    #
    fn_handles, \
    other_lines, \
    comment_lines, \
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
    generate_ouput_file_lines(other_lines, original_refs, ref_map, comment_lines)

    #
    # Write the output file to a temporary file
    #
    tmp_filename = write_output_temp_file(outlines)

    #
    # Rename files as cl args indicate
    #
    rename_files(mdfile, tmp_filename, vopts['outfile'], vopts['no_rdonly'])

if __name__ == '__main__':
    main()
