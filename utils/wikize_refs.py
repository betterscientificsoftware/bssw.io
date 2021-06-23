#!/usr/bin/env python

# run ./wikize_refs.py --help for documentation

from shutil import copyfile
import re, os

try:
    # python2
    from urlparse import urlparse
    from urllib import urlopen
except:
    # python3
    from urllib.parse import urlparse
    from urllib.request import urlopen

def usage():
    return \
"""
Adjusts, slightly, a markdown file so that any footnotes using
reference-style link and link-definitions to behave more
Wikipedia-like.

If the file contains no footnotes, the file will be left unchanged.
Does some minimal error checking that there is an existing link
definition for every footnote and that every link definition appears
in at least one footnote. It will also check that links are valid.
If errors are fatal, processing will stop upon encountering an error.
Otherwise only warning messages are produced.

The author's *original link definitions get adjusted slightly by
appending '-wikize-refs' to each link's id. This has the effect of
breaking their connection to the footnotes referencing them. This
is later repaired when a new set of link definitions are appended
to the end of the file.

The new links links are bi-level. Footnotes in the content link to
entries in a visible list of references (rendered as either a table
or a list) appended to the end of the document. Items in the list of
references link off-page to their intended destinations. The resulting
file is still GitHub flavored Markdown with a minimal amount of embedded
HTML.

To process a file...

    ./wikize_refs.py foo.md

...creates/updates the output file foo-wikized.md.

To modify the input file in-place...

    ./wikize_refs.py -i foo.md

...which also backs up the original file as foo.md~.  Use option
-s to skip the backup on the input file in this case.

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

    parser.add_argument("-c", "--check-links",
                      default=False,
                      action="store_true",
                      help="Check validity (parse and server response) of links.")

    parser.add_argument("-i", "--in-place",
                      default=False,
                      action="store_true",
                      help="Modify input file in-place.")

    parser.add_argument("-g", "--gather-linkdefs",
                      default=False,
                      action="store_true",
                      help="Gather all link definitions to the end of the file.")

    parser.add_argument("-r", "--renumber",
                      default=0, type=int,
                      help="Renumber references starting from specified value.")

    parser.add_argument("-l", "--list-refs",
                      default=False,
                      action="store_true",
                      help="Output references as list instead of table.")

    parser.add_argument("-s", "--skip-backup",
                      default=False,
                      action="store_true",
                      help="Disable creation of backup file appended with ~")

    parser.add_argument("-o", "--outfile",
                      default=None,
                      help="Specify an output file name. If none specified, will \
                            use <infile>-wikized.md or <infile>.md if -i option \
                            is specified")

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

def magic():
    return 'sfer-ezikiw'

def autogen_disclaimer():
    return '<!--- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (%s) --->'%magic()

def message(msg, warn):
    if warn:
        print("%s -- IGNORING due to -w (--warn)"%msg)
    else:
        print(msg)
        print("Either correct above errors or run with -w (--warn)")
        exit(1)

def valid_url(x):
    """Test that a given string is a valid URL"""
    try:
        ckparse = urlparse(x)
        return all([ckparse.scheme, ckparse.netloc, ckparse.path])
    except:
        return False

def broken_link(x):
    """Test if a link appears to be working or broken"""
    if x.startswith('ftp://') or x.startswith('file:///') or \
       x.startswith('#'):
       return False
    try:
        resp = urlopen(x)
        try:
            status = resp.getcode()
        except:
            status = resp.status 
        if status in [404,408,409,501,502,503]:
            return True
        else:
            return False
    except:
        return True

def is_link_def_line(mdfl):
    """
    Parse GFM link definition lines of the form...
        [10]: https://www.google.com
        [11]: https://www.google.com "Title Info"
        [1a]: https://www.google.com "Title Info {}"
        [2b]: https://www.google.com "Title Info {biblio info}"
        [foo]: ftp://some/file/online/foo.pdf
        [bar]: file:///some/file/online/foo.pdf
        [1234]: #some-internal-anchor

        Returns footnote handle, url, title, biblio-info as a list
    """
    retval = re.findall("^\[([a-zA-Z0-9_-]*)\]:\s*((https?://|ftp://|file:///|#)\S*)\s*\"?([^{]*)([^\"]*)\"?$", mdfl)
    if not retval:
        return None

    # Strip possible mangling applied from a previous run
    ref_hdl = retval[0][0]
    if ref_hdl.endswith('-%s'%magic()):
        ref_hdl = ref_hdl[:-len(magic())-1]
    ref_url = retval[0][1].strip()
    ref_tit = retval[0][3].strip().strip('"')
    ref_bib = retval[0][4].strip().strip('"{}')

    # Ignore cases that appear to be auto-generated intermediate links
    if ref_url.startswith('#%s'%magic()):
        return None

    return [ref_hdl, ref_url, ref_tit, ref_bib]

def gather_and_classify_file_lines(filename):
    """Read all file lines into a list in memory, classifying each line
       as we go."""
    lines = {}
    with open(filename, 'r') as mdf:
        lineno = 1
        in_xmlcomment = False
        in_frontmatter = False
        for line in mdf.readlines():
            line_type = ""
            if not in_frontmatter and re.match("^---$", line):
                line_type = "frontmatter"
                in_frontmatter = True
            elif in_frontmatter and re.match("^---$", line):
                line_type = "frontmatter"
                in_frontmatter = False
            elif not in_xmlcomment and re.match("^\s*<!---?.*---?>\s*$", line):
                line_type = "comment"
            elif not in_xmlcomment and re.match("^\S+<!---?.*---?>\s*$", line):
                line_type = "mixed"
            elif not in_xmlcomment and re.match("^\s*<!---?.*---?>\S+$", line):
                line_type = "mixed"
            elif not in_xmlcomment and re.match("^\S+<!---?.*---?>\S+$", line):
                line_type = "mixed"
            elif not in_xmlcomment and re.match("^\S+<!---?.*$", line):
                line_type = "mixed"
                in_xmlcomment = True
            elif in_xmlcomment and re.match("^.*---?>\S+$", line):
                line_type = "mixed"
                in_xmlcomment = False
            elif not in_xmlcomment and re.match("^\s*<!---?.*$", line):
                line_type = "comment"
                in_xmlcomment = True
            elif in_xmlcomment and re.match("^.*---?>\s*$", line):
                line_type = "comment"
                in_xmlcomment = False

            if not line_type:
                if in_frontmatter:
                    line_type = "frontmater"
                elif in_xmlcomment:
                    line_type = "comment"
                elif is_link_def_line(line):
                    line_type = "linkdef"
                else:
                    line_type = "content"

            # Ignore general content lines that appear to be auto-generated
            if line_type == "content" and magic() in line:
                continue

            if line.startswith(autogen_disclaimer()):
                continue

            lines[lineno] = {'line':line, 'type':line_type} 
            if line_type == "linkdef":
                lines[lineno]['linkdef'] = is_link_def_line(line)
            lineno += 1

    return lines

def gather_fn_handles(file_lines, warn):
    """Gets all footnote references occuring in content file lines."""
    fn_handles = set()
    for k in sorted(file_lines):

        if file_lines[k]['type'] != 'content':
            continue

        fl = file_lines[k]['line']

        # detect cases of <sup>[x]</sup> 
        fns1 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\]</sup>", fl)
        if fns1: fn_handles = fn_handles.union(set(fns1))

        # detect cases of <sup>[x],[y]</sup> 
        fns2 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", fl)
        if fns2:
            if len(set(fns2[0])) != 2:
                message("Duplicate footnote used between <sup>...</sup> at line %d."%k, warn)
            fn_handles = fn_handles.union(set(fns2[0]))

        # detect cases of <sup>[x],[y],[z]</sup> 
        fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", fl)
        if fns3:
            if len(set(fns3[0])) != 3:
                message("Duplicate footnote used between <sup>...</sup> at line %d."%k, warn)
            fn_handles = fn_handles.union(set(fns3[0]))

        # detect cases of <sup>[x],[y],[z],...</sup> 
        fns4p = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],(.*)</sup>", fl)
        if fns4p and len(fns4p[0]) >= 4:
            if len(set(fns4p[0][:3])) != 3:
                message("Duplicate footnote used between <sup>...</sup> at line %d."%k, warn)
            fn_handles = fn_handles.union(set(fns4p[0][:3]))
            message("Extra footnotes beyond 3 between <sup>...</sup> at line %d."%k, warn)

    return fn_handles

def build_ref_map(file_lines, warn):
    """builds a map keyed by footnote handle with value
       [url, title, biblio, re-numbered-id]"""
    ref_map = {}
    for k in sorted(file_lines):

        if file_lines[k]['type'] != 'linkdef':
            continue

        mdfparts = file_lines[k]['linkdef']
        if len(mdfparts) != 4:
            message("Improperly parsed link definition at line %d"%k, warn)
            continue

        ref_hdl, ref_url, ref_tit, ref_bib = mdfparts
        if ref_hdl in ref_map:
            message("Repeated reference handle %s at line %d"%(ref_hdl,k), warn)
            continue

        ref_map[ref_hdl] = [ref_url, ref_tit, ref_bib]
        ref_map[ref_hdl].append(len(ref_map))

    return ref_map

def error_checks(fn_handles, ref_map, check_links, warn):
    """
    Error checks footnote references and the link def reference list...
        - ensure every footnote references an existing item in the ref list
        - ensure every ref list item is referenced by at least one footnote
        - ensure URLs pass parsing rules
        - ensure URL targets exist
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

    if check_links:
        for k in ref_map:
            url = ref_map[k][0]
            if not valid_url(url):
                message("Invalid URL: \"%s\""%url, warn)
            if broken_link(url):
                message("Broken URL: \"%s\""%url, warn)

    return missing_fns

def build_main_content(file_lines, ref_map, renumber):
    """
    Rebuilds the file lines possibly renumbering the footnotes
    """
    outlines = []

    for k in sorted(file_lines):

        lineinfo = file_lines[k]
        ltype = lineinfo['type']
        line = lineinfo['line']

        if ltype == 'linkdef':

            ref_hdl, ref_url, ref_tit, ref_bib = lineinfo['linkdef']
            if magic() in line:
                # Its already mangled from a previous run
                outlines.append(line)
            else:
                # Mangle the linkdef to move it out of the way but nonetheless retain it
                outlines.append(line.replace(ref_hdl, "%s-%s"%(ref_hdl, magic()), 1))

        elif ltype == 'content':

            if not renumber:
                outlines += [line]
                continue

            # renumber any footnotes
            # Since we're re-filtering the same line multiple times, we replace
            # <sup></sup> with <pus></pus> to avoid collisions and then undue that
            # filter in the last step.
            fns1 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\]</sup>", line)
            for fn in fns1:
                line = re.sub("<sup>\[%s\]</sup>"%fn, "<pus>[%d]</pus>"%(ref_map[fn][3]+renumber), line)
            fns2 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", line)
            for fn in fns2:
                line = re.sub("<sup>\[%s\],\[%s\]</sup>"%(fn[0],fn[1]),
                             "<pus>[%d],[%d]</pus>"%\
                             (ref_map[fn[0]][3]+renumber, ref_map[fn[1]][3]+renumber), line)
            fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", line)
            for fn in fns3:
                line = re.sub("<sup>\[%s\],\[%s\],\[%s\]</sup>"%(fn[0],fn[1],fn[2]),
                             "<pus>[%d],[%d],[%d]</pus>"%\
                             (ref_map[fn[0]][3]+renumber,ref_map[fn[1]][3]+renumber,ref_map[fn[2]][3]+renumber), line)
            line = re.sub("<pus>","<sup>", line)
            line = re.sub("</pus>","</sup>", line)
            outlines += [line]

        else: # just output the same line as input
            outlines += [line]

    return outlines

def build_intermediate_link_defn_lines(remapped_ref_map, renumber):
    """Build (auto-gen'd) intermediate link definitions"""
    outlines = []

    if remapped_ref_map:
        for k,v in sorted(remapped_ref_map.items()):
            if renumber:
                outlines.append("[%d]: #%s-%d %s\n"%(k+renumber, magic(), k+renumber, "\"%s\""%v[1] if v[1] else ""))
            else:
                outlines.append("[%s]: #%s-%s %s\n"%(v[3], magic(), v[3], "\"%s\""%v[1] if v[1] else ""))

    return outlines

def build_reference_table_lines(remapped_ref_map, renumber):
    """Build (auto-gen'd) rendered table of references"""
    outlines = []

    if remapped_ref_map:
        outlines.append("References | &nbsp;\n")
        outlines.append(":--- | :---\n")
        for k,v in sorted(remapped_ref_map.items()):
            if v[1] and v[2]: # both title and bibinfo exist
                outlines.append("<a name=\"%s-%s\"></a>%s | [%s<br>%s](%s)\n"
                    %(magic(), k+renumber if renumber else v[3], k+renumber if renumber else v[3], v[1], v[2], v[0]))
            elif v[1]: # only title exists
                outlines.append("<a name=\"%s-%s\"></a>%s | [%s](%s)\n"
                    %(magic(), k+renumber if renumber else v[3], k+renumber if renumber else v[3], v[1], v[0]))
            elif v[2]: # only bibinfo exists
                outlines.append("<a name=\"%s-%s\"></a>%s | [%s](%s)\n"
                    %(magic(), k+renumber if renumber else v[3], k+renumber if renumber else v[3], v[2], v[0]))
            else: # only url exists
                outlines.append("<a name=\"%s-%s\"></a>%s | [%s](%s)\n"
                    %(magic(), k+renumber if renumber else v[3], k+renumber if renumber else v[3], v[0], v[0]))

    return outlines

def build_reference_list_lines(remapped_ref_map, renumber):
    """Build (auto-gen'd) rendered list of references"""
    outlines = []

    if remapped_ref_map:
        outlines.append("### References <!--- (%s) --->\n"%magic())
        for k,v in sorted(remapped_ref_map.items()):
            if v[1] and v[2]: # both title and bibinfo exist
                outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>[%s<br>%s](%s)\n"
                    %(magic(), k+renumber if renumber else v[3], k+renumber if renumber else v[3], v[1], v[2], v[0]))
            elif v[1]: # only title exists
                outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>[%s](%s)\n"
                    %(magic(), k+renumber if renumber else v[3], k+renumber if renumber else v[3], v[1], v[0]))
            elif v[2]: # only bibinfo exists
                outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>[%s](%s)\n"
                    %(magic(), k+renumber if renumber else v[3], k+renumber if renumber else v[3], v[2], v[0]))
            else: # only url exists
                outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>[%s](%s)\n"
                    %(magic(), k+renumber if renumber else v[3], k+renumber if renumber else v[3], v[0], v[0]))

    return outlines

def write_output_file(file_lines, out_lines, in_filename, out_filename, in_place, skip_backup):
    """Write the output file. But, only if it would be different than the input."""

    with open(in_filename, 'r') as inf:
        in_lines = inf.readlines()
        if str().join(out_lines) == str().join(in_lines):
            print("\"%s\" is up to date. No changes will be made."%in_filename)
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

    # Get and classify all lines in file
    file_lines = gather_and_classify_file_lines(mdfile)

    # Examine file lines for footnotes
    fn_handles = gather_fn_handles(file_lines, opts['warn'])

    # Build a map of the references including their re-numbering
    ref_map = build_ref_map(file_lines, opts['warn'])

    # Do some error checking
    missing_fns = error_checks(fn_handles, ref_map,
        opts['check_links'], opts['warn'])

    #
    # Ok, we're done processing the input file. Now, start building
    # the lines for the output file.
    #

    # First, build the main content lines with renumbered footnotes
    out_lines = build_main_content(file_lines, ref_map, opts['renumber'])

    # Build a disclaimer line if we'll have generated content
    if ref_map:
        out_lines.append("%s\n"%autogen_disclaimer())
    
    # Build intermediate link definitions lines
    remapped_ref_map = {v[3]:[v[0],v[1],v[2],k] for k,v in ref_map.items()}
    out_lines += build_intermediate_link_defn_lines(remapped_ref_map, opts['renumber'])

    # Build reference table lines
    if opts['list_refs']:
        out_lines += build_reference_list_lines(remapped_ref_map, opts['renumber'])
    else:
        out_lines += build_reference_table_lines(remapped_ref_map, opts['renumber'])

    # Ok, now actually write the updated file
    flines = [file_lines[k]['line'] for k in sorted(file_lines)]
    write_output_file(flines, out_lines, mdfile, opts['outfile'], opts['in_place'],
        opts['skip_backup'])

#
# So this python script can be used both as a shell command
# and as an imported python module.
#
if __name__ == '__main__':

    # Process command line options
    opts, mdfile = parse_args()

    main(opts, mdfile)
