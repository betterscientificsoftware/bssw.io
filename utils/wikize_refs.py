#!/usr/bin/env python

# run ./wikize_refs.py --help for documentation

from shutil import copyfile
import re, os

def usage():
    return \
"""
Re-formats a series of reference style links in a GitHub Markdown file
so that the article's footnote links behave more Wikipedia-like.

Treats a markdown file as being composed of four successive logical
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
but bracketed within XML comment blocks to hide these link definitions
from any markdown processing.

The renumbered and re-formatted links are bi-level. Footnotes in the
content link to entries in a list of references at the bottom of the
document. Items in the table of references link off-page to their
intended destinations. The resulting file is still GitHub flavored
Markdown with a minimal amount of embedded HTML.

For more information, see https://github.com/betterscientificsoftware/\
betterscientificsoftware.github.io/blob/master/Articles/Blog/\
ReferencesInMarkdownHybridApproach.md

To process a file...

    ./wikize_refs.py foo.md

...creates/updates the output file foo-wikized.md.

To modify the input file in-place...

    ./wikize_refs.py -i foo.md

...which also backs up the original file as foo.md~.  Use option -s to skip
the backup on the input file in this case.

    ./wikize_refs.py --help

...prints command-line arguments and options.
"""

def parse_args():
    """
    Parses arguments to wikize_refs.py.
    """
    from argparse import ArgumentParser, RawDescriptionHelpFormatter

    parser = ArgumentParser(description=usage(),
        formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument("-w", "--warn",
                      default=False,
                      action="store_true",
                      help="Warn instead of error during (most) error checks.")

    parser.add_argument("-i", "--in-place",
                      default=False,
                      action="store_true",
                      help="Modify input file in-place.")

    parser.add_argument("-s", "--skip-backup",
                      default=False,
                      action="store_true",
                      help="Disable creation of backup file appended with ~")

    parser.add_argument("-o", "--outfile",
                      default=None,
                      help="Specify an output file name. If none specified, will \
                            use <infile>-wikized.md")

    parser.add_argument("mdfile")

    opts = parser.parse_args()

    vopts = vars(opts)

    if not vopts['mdfile']:
        print("Must include the name of a markdown file to process!")
        exit(1)
    else:
        mdfile = vopts['mdfile']

    if vopts['in_place'] and vopts['outfile']:
        print("Can't set both -i and -o options!")
        exit(1)

    if vopts['in_place']:
        vopts['outfile'] = mdfile
    elif not vopts['outfile']:
        vopts['outfile'] = "%s-wikized.md"%os.path.splitext(mdfile)[0]

    return vopts, mdfile

def ld_block_begin_line():
    """Constant XML comment text for beginning of link def block"""
    return "<!-- BEGIN ORIGINAL LINK DEFS"

def ld_block_end_line():
    """Constant XML comment text for end of link def block"""
    return "END ORIGINAL LINK DEFS -->"

def is_ld_block_begin_line(mdfl):
    """Check if line is link def block begin comment"""
    return re.match("^%s$"%ld_block_begin_line(), mdfl) is not None

def is_ld_block_end_line(mdfl):
    """Check if line is link def block end comment"""
    return re.match("^%s$"%ld_block_end_line(), mdfl) is not None

def is_ld_block_defn_line(mdfl):
    """
    Parse GFM link definition lines of the form...
        [10]: https://www.google.com
        [11]: https://www.google.com "Title Info"
        [1a]: https://www.google.com "Title Info {}"
        [2b]: https://www.google.com "Title Info {biblio info}"

        Returns footnote id, url, title, biblio-info as a list
    """
    retval = re.findall("^\[([a-zA-Z0-9_-]*)\]:\s*((https?|ftp)://\S*)\s*\"?([^{]*)([^\"]*)\"?$", mdfl)
    if not retval:
        return None

    ref_hdl = retval[0][0]
    ref_url = retval[0][1].strip()
    ref_tit = retval[0][3].strip().strip('"')
    ref_bib = retval[0][4].strip().strip('"{}')

    return [ref_hdl, ref_url, ref_tit, ref_bib]

def gather_file_lines(filename):
    """Read all file lines into a list in memory"""
    with open(filename, 'r') as mdf:
        return mdf.readlines()

def gather_main_content_lines(file_lines):
    """Returns all lines occuring before first link def line."""
    mc_lines = []
    for mdfl in file_lines:
        if is_ld_block_defn_line(mdfl):
            break
        if is_ld_block_begin_line(mdfl):
            break
        mc_lines += [mdfl]
    return mc_lines

def gather_link_defn_lines(file_lines):
    """Returns all link def lines occuring after main content.
       Should be called with set of lines starting with first
       non-main-content line."""
    ld_lines = []
    for mdfl in file_lines:
        if is_ld_block_begin_line(mdfl):
            continue # ignore the block begin line
        if is_ld_block_end_line(mdfl):
            break
        if is_ld_block_defn_line(mdfl):
            ld_lines += [mdfl]
    return ld_lines
    
def gather_fn_handles(mc_lines, warn):
    """Gets all footnote references (handles) occuring in main content
       excluding any occuring in XML comments."""
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
    """builds a map keyed by footnote handle with value
       [url, title, biblio, re-numbered-id]"""
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
    Error checks footnote references and the link def reference list...
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

def remove_unref_ld_lines(ld_lines, missing_fns):
    """
    Scans link def lines for any for which there is not footnote
    referencing them. Returns two lists; one for all referenced
    link def lines and the other for un-referenced link def lines.
    """
    new_ld_lines = []
    unref_ld_lines = []

    if not ld_lines:
        return new_ld_lines, unref_ld_lines

    if not missing_fns:
        return ld_lines, unref_ld_lines

    for ld in ld_lines:
        fn_hdl = is_ld_block_defn_line(ld)
        if fn_hdl[0] in missing_fns:
            unref_ld_lines += [ld]
        else:
            new_ld_lines += [ld]

    return new_ld_lines, unref_ld_lines

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
            mcl = re.sub("<sup>\[%s\],\[%s\]</sup>"%(fn[0],fn[1]),
                         "<pus>[%d],[%d]</pus>"%\
                         (ref_map[fn[0]][3], ref_map[fn[1]][3]), mcl)
        fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", mcl)
        for fn in fns3:
            mcl = re.sub("<sup>\[%s\],\[%s\],\[%s\]</sup>"%(fn[0],fn[1],fn[2]),
                         "<pus>[%d],[%d],[%d]</pus>"%\
                         (ref_map[fn[0]][3],ref_map[fn[1]][3],ref_map[fn[2]][3]), mcl)
        mcl = re.sub("<pus>","<sup>", mcl)
        mcl = re.sub("</pus>","</sup>", mcl)
        outlines.append(mcl)

    return outlines

def build_link_defn_lines(ld_lines, ref_map, unref_ld_lines):
    """Rebuild the (original) link def lines but renumbered and reformatted slightly"""
    outlines = []

    # handle any unused refs first, outside of any comments bracketing blocks
    if unref_ld_lines:
        for ld in unref_ld_lines:
            outlines += [ld]
        outlines.append("\n")

    if not ld_lines:
        return outlines

    # Now, handle author's original link def lines but renumbered and
    # embedded in XML comment blocks
    outlines.append(ld_block_begin_line())
    outlines.append("\n\n")
    for l in ld_lines:
        ref_hdl, ref_url, ref_tit, ref_bib = is_ld_block_defn_line(l)
        if ref_tit and ref_bib:
            outlines.append("[%d]: %s \"%s {%s}\"\n"%(ref_map[ref_hdl][3], ref_url, ref_tit, ref_bib))
        elif ref_tit:
            outlines.append("[%d]: %s \"%s\"\n"%(ref_map[ref_hdl][3], ref_url, ref_tit))
        elif ref_bib:
            outlines.append("[%d]: %s \"{%s}\"\n"%(ref_map[ref_hdl][3], ref_url, ref_bib))
        else:
            outlines.append("[%d]: %s\n"%(ref_map[ref_hdl][3], ref_url))
    outlines.append("\n")
    outlines.append(ld_block_end_line())
    outlines.append("\n")

    return outlines

def build_intermediate_link_defn_lines(remapped_ref_map):
    """Build (auto-gen'd) intermediate link definitions"""
    outlines = []

    if remapped_ref_map:
        outlines.append("\n<!--- INTERMEDIATE LINK DEFS POINT TO ANCHORS IN TABLE --->\n")
        for k,v in sorted(remapped_ref_map.items()):
            outlines.append("[%d]: #ref%d%s\n"%(k, k, " \"%s\""%v[1] if v[1] else ""))

    return outlines

def build_reference_table_lines(remapped_ref_map):
    """Build (auto-gen'd) rendered table of references"""
    outlines = []

    if remapped_ref_map:
        outlines.append("\n<!--- TABLE OF REFS RENDERED AS MARKDOWN --->\n")
        outlines.append("References | &nbsp;\n")
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

def write_output_file(file_lines, out_lines, in_filename, out_filename, in_place, skip_backup):
    """Write the output file. But, only if it would be different than the input."""

    # don't write if output would be identical to input
    if str().join(out_lines) == str().join(file_lines):
        print("\"%s\" is up to date. No changes will be made."%mdfile)
        return

    # don't make the backup if asked not to
    if in_place and not skip_backup:
        copyfile(in_filename, "%s~"%in_filename)

    # ok, write the file
    outfname = out_filename if out_filename else in_filename
    with open(outfname, 'w') as outf:
        outf.writelines(["%s" % line for line in out_lines])

#
# For basic design/operation, see usage notes (above)
#
def main(opts, mdfile):

    # Get all txt lines from file into a list
    file_lines = gather_file_lines(mdfile)

    # Get the lines of "main content"
    # (everything before first link def line)
    main_content = gather_main_content_lines(file_lines)

    # Examine main content lines for footnotes
    fn_handles = gather_fn_handles(main_content, opts['warn'])

    # Get any link definition lines
    ld_lines = gather_link_defn_lines(file_lines[len(main_content):])
    
    # Build a map of the references including their re-numbering
    ref_map = build_ref_map(ld_lines, opts['warn'])

    # Do some error checking
    missing_fns = error_checks(fn_handles, ref_map, opts['warn'])

    # Remove from ld_lines any not actually referenced
    ld_lines, unref_ld_lines = remove_unref_ld_lines(ld_lines, missing_fns)

    # Rebuild the refmap again with remaining ld_lines
    ref_map = build_ref_map(ld_lines, opts['warn'])

    #
    # Ok, we're done processing the input file. Now, start building
    # the lines for the output file.
    #

    # First, build the main content lines with renumbered footnotes
    out_lines = build_main_content(main_content, ref_map)

    # Build the (original but renumbered) link definitions
    out_lines += build_link_defn_lines(ld_lines, ref_map, unref_ld_lines)

    # Build a disclaimer line if we'll have generated content
    if ld_lines:
        out_lines.append("\n<!-- ALL CONTENT BELOW HERE IS AUTO-GENERATED FROM wikize_refs.py -->\n")
    
    # Build intermediate link definitions lines
    remapped_ref_map = {v[3]:[v[0],v[1],v[2],k] for k,v in ref_map.items()}
    out_lines += build_intermediate_link_defn_lines(remapped_ref_map)

    # Build reference table lines
    out_lines += build_reference_table_lines(remapped_ref_map)

    # Ok, now actually write the updated file
    write_output_file(file_lines, out_lines, mdfile, opts['outfile'], opts['in_place'],
        opts['skip_backup'])

#
# So this python script can be used both as a shell command
# and as an imported python module.
#
if __name__ == '__main__':

    # Process command line options
    opts, mdfile = parse_args()

    main(opts, mdfile)
