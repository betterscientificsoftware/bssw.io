#!/usr/bin/env python

# run ./wikize_refs.py --help for documentation

from optparse import OptionParser
from shutil import copyfile
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
  3. Auto-gen'd Intermediate link definitions ([J]: #refJ "Title {}")
  4. Auto-gen'd Ref. table (<a name="refJ"></a>J | [Title](https://... "{...}"))

Blocks 2, 3 and 4 are optional. Blocks 3 and 4 are generated from
block 2 if it exists. Repeated applications of this tool should
result in no changes to the file.

If the main content contains no footnotes, the file will be left
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

...moves original foo.md to foo.md~ and outputs a new foo.md. Use
-i option to disable this behavior.

    ./wikize_refs.py --help

...prints command-line arguments and options.
"""

def parse_args():
    """
    Parses arguments to wikize_refs.py.
    """
    parser = OptionParser(usage())

    parser.add_option("-w", "--warn",
                      default=False,
                      action="store_true",
                      help="Warn instead of error during sanity checks.")

    parser.add_option("-i", "--in-place",
                      default=False,
                      action="store_true",
                      help="Do the operation in place, overwriting the input file.\
                          Disables creation of backup file appended with ~")

    parser.add_option("-o", "--outfile",
                      default="",
                      help="Specify output file name.")

    opts, mdfiles = parser.parse_args()

    if not mdfiles:
        print("Must include the name of a markdown file to process.")
        exit(1)

    return opts, mdfiles[0]

def ld_block_begin_line():
    """Constant XML comment text for beginning of link def block"""
    return "<!-- BEGIN ORIGINAL LINK DEFS"

def ld_block_end_line():
    """Constant XML comment text for end of link def block"""
    return "END ORIGINAL LINK DEFS -->"

def gather_file_lines(filename):
    """Read all file lines into a list in memory"""
    with open(filename, 'r') as mdf:
        return mdf.readlines()

def is_ld_block_begin_line(mdfl):
    """Check if line is link def block begin comment"""
    return re.match("^%s$"%ld_block_begin_line(), mdfl) is not None

def is_ld_block_end_line(mdfl):
    """Check if line is link def block end comment"""
    return re.match("^%s$"%ld_block_end_line(), mdfl) is not None

def is_ld_block_defn_line(mdfl):
    """
    Parse GFM link definition lines of the form...
        [1]: https://www.google.com
        [1]: https://www.google.com "Title Info"
        [1]: https://www.google.com "Title Info {}"
        [1]: https://www.google.com "Title Info {biblio info}"
    """
    retval = re.findall("^\[([a-zA-Z0-9_-]*)\]:\s*(https?://\S*)\s*\"?([^{]*)([^\"]*)\"?$", mdfl)
    if not retval:
        return None

    ref_hdl = retval[0][0]
    ref_url = retval[0][1].strip()
    ref_tit = retval[0][2].strip().strip('"')
    ref_bib = retval[0][3].strip().strip('"{}')

    return [ref_hdl, ref_url, ref_tit, ref_bib]

def gather_main_content_lines(file_lines):
    """Returns all lines occuring before link def block"""
    mc_lines = []
    for mdfl in file_lines:
        if is_ld_block_defn_line(mdfl):
            break
        if is_ld_block_begin_line(mdfl):
            break
        mc_lines += [mdfl]
    return mc_lines

def gather_link_defn_lines(file_lines):
    """Returns all link def lines occuring after main content"""
    ld_lines = []
    for mdfl in file_lines:
         if is_ld_block_end_line(mdfl):
            break
         if is_ld_block_defn_line(mdfl):
            ld_lines += [mdfl]
    return ld_lines
    
def gather_fn_handles(mc_lines, warn):
    """Gets all footnote handles occuring in main content excluding any in XML comments."""
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
    """builds a map keyed by footnote handle with value [url, title, biblio]"""
    ref_map = {}
    for ldl in ld_lines:
        mdfparts = is_ld_block_defn_line(ldl)
        if mdfparts:
            if len(mdfparts) != 4:
                print("Error: unknown problem at or near this line...")
                print(ldl)
                if not warn:
                    print("Correct above issues and re-try...")
                    exit(1)
            ref_hdl, ref_url, ref_tit, ref_bib = mdfparts
            if ref_hdl in ref_map:
                print("Error: repeated reference handle", ref_hdl, "at or near this line...")
                print(ldl)
                if not warn:
                    print("Correct above issues and re-try...")
                    exit(1)
            ref_map[ref_hdl] = [ref_url, ref_tit, ref_bib]
            ref_map[ref_hdl].append(len(ref_map))
    return ref_map

def error_checks(fn_handles, ref_map, warn):
    """
    Error checks for footnote references and the reference list...
        - ensure every footnote references an existing item in the ref list
        - ensure every ref list item is referenced by at least one footnote
    """
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

    return missing_fns

def build_main_content(mc_lines, ref_map):
    """
    Builds main content lines but renumbering the footnotes. Filters any
    footnotes in the main content with their new re-numbered instances.
    """
    outlines = []

    # Since we're re-filtering the same line multiple times, we replace
    # <sup></sup> with <pus></pus> to avoid collisions and then undue that
    # filter in the last step.
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

def build_link_defn_lines(ld_lines, ref_map, missing_fns):
    """Rebuild the (original) link def lines but renumbered and reformatted slightly"""
    outlines = []
    if not ld_lines:
        return outlines

    outlines.append(ld_block_begin_line())
    outlines.append("\n\n")
    for l in ld_lines:
        ref_hdl, ref_url, ref_tit, ref_bib = is_ld_block_defn_line(l)
        if ref_hdl in missing_fns:
            continue
        if ref_tit and ref_bib:
            outlines.append("[%d]: %s \"%s {%s}\"\n"%(ref_map[ref_hdl][3], ref_url, ref_tit, ref_bib))
        elif ref_tit:
            outlines.append("[%d]: %s \"%s\"\n"%(ref_map[ref_hdl][3], ref_url, ref_tit))
        elif ref_bib:
            outlines.append("[%d]: %s \"{%s}\"\n"%(ref_map[ref_hdl][3], ref_url, ref_bib))
        else:
            outlines.append("[%d]: %s\n"%(ref_map[ref_hdl][3], ref_url))
    # handle any unused refs
    for x in missing_fns:
        ref_hdl, ref_url, ref_tit, ref_bib = x, ref_map[x][0], ref_map[x][1], ref_map[x][2]
        if ref_tit and ref_bib:
            outlines.append("[%d]: %s \"%s {%s}\"\n"%(ref_map[ref_hdl][3], ref_url, ref_tit, ref_bib))
        elif ref_tit:
            outlines.append("[%d]: %s \"%s\"\n"%(ref_map[ref_hdl][3], ref_url, ref_tit))
        elif ref_bib:
            outlines.append("[%d]: %s \"{%s}\"\n"%(ref_map[ref_hdl][3], ref_url, ref_bib))
        else:
            outlines.append("[%d]: %s\n"%(ref_map[ref_hdl][3], ref_url))
        del ref_map[ref_hdl] # finally, remove this unnused ref from our map
    outlines.append("\n")
    outlines.append(ld_block_end_line())

    return outlines

def build_intermediate_link_defn_lines(remapped_ref_map):
    """Build (auto-gen'd) intermediate link definitions"""
    outlines = []

    for k,v in sorted(remapped_ref_map.items()):
        outlines.append("[%d]: #ref%d%s\n"%(k, k, " \"%s\""%v[1] if v[1] else ""))

    return outlines

def build_reference_table_lines(remapped_ref_map):
    """Build the refrence table"""
    outlines = []

    outlines.append("\nReferences | &nbsp;\n")
    outlines.append(":--- | :---\n")
    for k,v in sorted(remapped_ref_map.items()):
        if v[1] and v[2]: # both title and bibinfo exist
            outlines.append("<a name=\"ref%d\"></a>%d | [%s<br>%s](%s)\n"%(k, k, v[1], v[2], v[0]))
        elif v[1]: # only title exists
            outlines.append("<a name=\"ref%d\"></a>%d | [%s](%s)\n"%(k, k, v[1], v[0]))
        elif v[2]: # only bibinfo exists
            outlines.append("<a name=\"ref%d\"></a>%d | [%s](%s)\n"%(k, k, v[2], v[0]))
        else: # only url exists
            outlines.append("<a name=\"ref%d\"></a>%d | [%s](%s)\n"%(k, k, v[0], v[0]))
    return outlines

def write_output_file(outlines, in_filename, out_filename, in_place):
    if not in_place and out_filename != "" and out_filename != in_filename:
        copyfile(in_filename, "%s~"%in_filename)
    outfname = out_filename if out_filename else  "%s-wikized.md"%os.path.splitext(in_filename)[0]
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

    # Do some sanity checks
    missing_fns = error_checks(fn_handles, ref_map, vopts['warn'])

    #
    # Ok, we're done processing the input file. Now, start building
    # the lines for the output file.
    #

    # First, build the main content lines with renumbered footnotes
    outlines = build_main_content(main_content, ref_map)

    # Build the (original but renumbered) link definitions
    outlines += build_link_defn_lines(ld_lines, ref_map, missing_fns)

    # Build a disclaimer line if we'll have generated content
    if ld_lines:
        outlines.append("\n\n<!-- ALL CONTENT BELOW HERE IS AUTO-GENERATED FROM wikize_refs.py -->\n\n")
    
    # Build intermediate link definitions lines
    remapped_ref_map = {v[3]:[v[0],v[1],v[2],k] for k,v in ref_map.items()}
    outlines += build_intermediate_link_defn_lines(remapped_ref_map)

    # Build reference table lines
    outlines += build_reference_table_lines(remapped_ref_map)

    # Ok, now actually write the updated file
    write_output_file(outlines, mdfile, vopts['outfile'], vopts['in_place'])

#
# So this python script can be used both as a shell command
# and as an imported python module.
#
if __name__ == '__main__':
    main()
