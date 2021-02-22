#!/usr/bin/env python

# run ./wikize_refs.py --help for documentation

from optparse import OptionParser
import re, os

def usage():
    return \
"""
%prog <infile.md>

Re-formats a series of reference style links in a GitHub Markdown file
so that the article's footnote links behave more Wikipedia-like.

Treats a markdown file as being composed of four succesive logical
blocks...

  1. The main content with possible footnote refs (<sup>[J],...</sup>)
  2. The author's link definitions ([J]: https://... "Title {}")
  3. Intermediate link definitions ([J]: #refJ "Title {}")
  4. Ref. table (<a name="refJ"></a>J | [Title](https://... "{...}"))

Blocks 2, 3 and 4 are optional. Blocks 3 and 4 are generated from
block 2 if it exists.

If the main content contains no footnotes, the file should be left
unchanged. If a footnote references a non-existent author's link
definition, an error message is issued and processing is stopped.
If a link definition is not referenced by any footnote, a warning
message is produced but processing continues.

The author's link definitions are renumbered 1...N and all footnote
references are updated accordingly. These link definitions are output
but bracketed by XML comment blocks to hide these link definitions
from any markdown processing.

The renumbered and re-formatted links are bi-level. Footnotes in the
content link to entries in a table of references at the bottom of the
document. Items in the table of references link off-page to their
intended destinations. The resulting file is still GitHub flavored
Markdown with a minimal amount of embedded HTML.

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

    parser.add_option("-i", "--in-place",
                      default=False,
                      action="store_true",
                      help="Do the operation in place, overwriting the input file.")

    parser.add_option("-o", "--outfile",
                      help="Specify output file name.")

    opts, mdfiles = parser.parse_args()

    if not mdfiles:
        print("Must include the name of a markdown file to process.")
        exit(1)

    return opts, mdfiles[0]

def ld_block_begin_line():
    return "<!-- BEGIN ORIGINAL LINK DEFS"

def ld_block_end_line():
    return "END ORIGINAL LINK DEFS -->"

def gather_file_lines(filename):
    with open(filename, 'r') as mdf:
        return mdf.readlines()

def is_ld_block_begin_line(mdfl):
    return re.match("^%s$"%ld_block_begin_line(), mdfl) is not None

def is_ld_block_end_line(mdfl):
    return re.match("^%s$"%ld_block_end_line(), mdfl) is not None

def is_ld_block_defn_line(mdfl):
    return re.search("^\[([a-zA-Z0-9_-]*)\]: (https?://.*) \"(.*)( {.*})?\"$", mdfl)

def gather_main_content_lines(file_lines):
    mc_lines = []
    for mdfl in file_lines:
        if is_ld_block_defn_line(mdfl):
            break
        if is_ld_block_begin_line(mdfl):
            break
        mc_lines += [mdfl]
    return mc_lines

def gather_link_defn_lines(file_lines):
    ld_lines = []
    for mdfl in file_lines:
         if is_ld_block_end_line(mdfl):
            break
         if is_ld_block_defn_line(mdfl):
            ld_lines += [mdfl]
    return ld_lines
    
def gather_fn_handles(mc_lines, warn):
    fn_handles = set()
    in_comment = False
    for mcl in mc_lines:
        if re.match("^\s*<!---?\s*$", mcl):
            in_comment = True
        elif in_comment and re.match("^\s*---?>\s*$", mcl):
            in_comment = False
        elif not in_comment: # handle up to 3 footnotes in a single <sup></sup>
             fns1 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\]</sup>", mcl)
             fn_handles = fn_handles.union(set(fns1))
             fns2 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mcl)
             for fn in fns2: fn_handles = fn_handles.union(set(fn))
             fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mcl)
             for fn in fns3: fn_handles = fn_handles.union(set(fn))
             fns4p = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],(.*)</sup>", mcl)
             if len(fns4p) >= 4:
                 print("Error: Max number of grouped footnotes between <sup>...</sup> is 3")
                 print("This occurred at or near this line...")
                 print(mcl)
                 if not warn:
                    print("Correct above issues and re-try...")
                    exit(1)
    return fn_handles

def build_ref_map(ld_lines, warn):
    ref_map = {}
    for ldl in ld_lines:
        mdfparts = is_ld_block_defn_line(ldl)
        if mdfparts is not None:
            if len(mdfparts.groups()) != 4:
                print("Error: unknown problem at or near this line...")
                print(ldl)
                if not warn:
                    print("Correct above issues and re-try...")
                    exit(1)
            ref_hdl = mdfparts.groups()[0]
            ref_url = mdfparts.groups()[1]
            ref_tit = mdfparts.groups()[2]
            ref_bib = ""
            if (mdfparts.groups()[3]):
                ref_bib = mdfparts.groups()[3][2:-1]
            if ref_hdl in ref_map:
                print("Error: repeated reference handle", ref_hdl, "at or near this line...")
                print(ldl)
                if not warn:
                    print("Correct above issues and re-try...")
                    exit(1)
            ref_map[ref_hdl] = [ref_tit, ref_url, ref_bib]
            ref_map[ref_hdl].append(len(ref_map))
    return ref_map

#
# Sanity checks for footnote references and the reference list
#    - ensure every footnote references an existing item in the ref list
#    - ensure every ref list item is referenced by at least one footnote
#
def sanity_checks(fn_handles, ref_map, warn):
    ref_handles = set(ref_map.keys())
    missing_refs = fn_handles - ref_handles
    if missing_refs:
        print("Some footnotes never appear in the references...")
        print([x for x in missing_refs])
        if not warn:
            print("Correct above issues and re-try...")
            exit(1)

    missing_fns = ref_handles - fn_handles
    if missing_fns:
        print("Some references never appear in a footnote...")
        print([x for x in missing_fns])
        if not warn:
            print("Correct above issues and re-try...")
            exit(1)

def build_main_content(mc_lines, ref_map):
    outlines = []

    #
    # Filter any footnotes in the main content with their new re-numbered
    # instances. Since we're re-filtering the same line multiple times, we
    # replace <sup></sup> with <pus></pus> to avoid collisions and then
    # undue that filter in the last step.
    #
    for mcl in mc_lines:
        fns1 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\]</sup>", mcl)
        for fn in fns1:
            mcl = re.sub("<sup>\[%s\]</sup>"%fn, "<pus>[%d]</pus>"%ref_map[fn][3], mcl)
        fns2 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mcl)
        for fn in fns2:
            mcl = re.sub("<sup>\[%s\],\[%s\]</sup>"%(fn[0],fn[1]), "<pus>[%d],[%d]</pus>"%(ref_map[fn[0]][3],ref_map[fn[1]][3]), mcl)
        fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mcl)
        for fn in fns3:
            mcl = re.sub("<sup>\[%s\],\[%s\],\[%s\]</sup>"%(fn[0],fn[1],fn[2]), "<pus>[%d],[%d],[%d]</pus>"%(ref_map[fn[0]][3],ref_map[fn[1]][3],ref_map[fn[2]][3]), mcl)
        mcl = re.sub("<pus>","<sup>", mcl)
        mcl = re.sub("</pus>","</sup>", mcl)
        outlines.append(mcl)

    return outlines

def build_link_defn_lines(ld_lines, ref_map):
    outlines = []
    if not ld_lines:
        return outlines

    outlines.append(ld_block_begin_line())
    outlines.append("\n\n")
    for l in ld_lines:
        lparts = re.search("^\[([a-zA-Z0-9_-]*)\]: (.*) \"(.*)( {.*})?\"$", l)
        ref_hdl = lparts.groups()[0]
        ref_url = lparts.groups()[1]
        ref_tit = lparts.groups()[2]
        if lparts.groups()[3]:
            ref_bib = lparts.groups()[3][2:-1]
            outlines.append("[%d]: %s \"%s {%s}\"\n"%(ref_map[ref_hdl][3], ref_url, ref_tit, ref_bib))
        else:
            outlines.append("[%d]: %s \"%s\"\n"%(ref_map[ref_hdl][3], ref_url, ref_tit))
    outlines.append("\n")
    outlines.append(ld_block_end_line())

    return outlines

def build_intermediate_link_defn_lines(remapped_ref_map):
    outlines = []

    for k,v in sorted(remapped_ref_map.items()):
        outlines.append("[%d]: #ref%d \"%s\"\n"%(k, k, v[0]))

    return outlines

def build_reference_table_lines(remapped_ref_map):
    outlines = []

    outlines.append("\nReferences | &nbsp;\n")
    outlines.append(":--- | :---\n")
    for k,v in sorted(remapped_ref_map.items()):
        if (not v[0] or v[0].isspace()) and (not v[2] or v[2].isspace()):
            outlines.append("<a name=\"ref%d\"></a>%d | %s\n"%(k, k, v[1]))
        elif v[0] in v[2]:
            outlines.append("<a name=\"ref%d\"></a>%d | [%s](%s)\n"%(k, k, v[2], v[1]))
        else:
            outlines.append("<a name=\"ref%d\"></a>%d | [%s %s](%s)\n"%(k, k, v[0], v[2], v[1]))

    return outlines

def write_output_file(outlines, in_filename, out_filename, in_place):
    if in_place:
        outfname = in_filename
    else:
        outfname =  outfname = "%s-wikized.md"%os.path.splitext(in_filename)[0]
    with open(outfname, 'w') as outf:
        outf.writelines(["%s" % line for line in outlines])

#
# For basic design/operation, see usage notes (above)
#
def main():

    # Process command line options
    opts, mdfile = parse_args()
    vopts = vars(opts)

    # Get all txt lines from file into a list
    file_lines = gather_file_lines(mdfile)

    # Get the lines of "main content"
    # (everything before first link def line)
    main_content = gather_main_content_lines(file_lines)

    # Examine main content lines for footnotes
    fn_handles = gather_fn_handles(main_content, vopts['warn'])

    # Get any link definition lines
    ld_lines = gather_link_defn_lines(file_lines[len(main_content):])
    
    # Build a map of the references including their re-numbering
    ref_map = build_ref_map(ld_lines, vopts['warn'])
    remapped_ref_map = {v[3]:[v[0],v[1],v[2],k] for k,v in ref_map.items()}

    # Do some sanity checks
    sanity_checks(fn_handles, ref_map, vopts['warn'])

    #
    # Ok, we're done processing the input file. Now, start building
    # the lines for the output file.
    #

    # First, output the main content lines with renumbered footnotes
    outlines = build_main_content(main_content, ref_map)

    # Output the (original but renumbered) link definitions
    outlines += build_link_defn_lines(ld_lines, ref_map)

    # Output a disclaimer line if we'll have generated content
    if ld_lines:
        outlines.append("\n\n<!-- ALL CONTENT BELOW THIS LINE IS AUTO-GENERATED -->\n\n")
    
    # Output intermediate link definitions lines
    outlines += build_intermediate_link_defn_lines(remapped_ref_map)

    # Output reference table lines
    outlines += build_reference_table_lines(remapped_ref_map)

    # Ok, now actually write the updated file
    write_output_file(outlines, mdfile, vopts['outfile'], vopts['in_place'])

#
# So this python script can be used both as a shell command
# and as an imported python module.
#
if __name__ == '__main__':
    main()
