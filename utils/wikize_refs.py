#!/usr/bin/env python

# run ./wikize_refs.py --help for documentation

from shutil import copyfile
import os, re, sys

try:
    # python2
    from urlparse import urlparse
    from urllib2 import urlopen
    from urllib2 import Request
except:
    # python3
    from urllib.parse import urlparse
    from urllib.request import urlopen
    from urllib.request import Request

def usage():
    return \
"""
Adjusts, slightly, a markdown file so that any footnotes using
reference-style markdown links and link-definitions behave more
Wikipedia-like. Ordinarily, this can be accomplished by simply
name-mangling the author's original link labels (to move them
out of the way) and *adding* some lines to the file.

The author's *original* link labels get mangled. This has the effect
of breaking their connection to the footnotes referencing them. This
is later repaired when a new set of link definitions are appended
to the end of the file.

The new links are bi-level. Footnotes in the content link to
entries in a visible list of references appended to the end of the
visible content. Items in the list of references link off-page to their
intended destinations. The resulting file is still GitHub flavored
Markdown with a minimal amount of embedded HTML.

To create just simple, ordinary footnotes (e.g. not reference style
links) using the same machinery, simply ensure the URL portion of the
reference link is just the hashtag/pound character ('#') and then
be sure to enclose the footnote text in double quotes.

If the file contains no footnotes, it will be left unchanged.

Some minimal error checks include: a) there is an existing link
definition for every footnote and b) every link definition appears
in at least one footnote. It will also check that links are valid,
that the URLs are valid URL strings and that following the links
yields an actual URL resource and not an error of some kind.
If errors are fatal, processing will stop upon encountering a first
error. Otherwise only warning messages are produced.

Ordinarily, the input file is never changed. However, with the -i
option, the changes are applied *in place* meaning the input file
is indeed modified. In that case, some of the options here are
*irreversible* in that the file is changed in ways not easy to
reverse. Those options are noted.

Repeated application of this tool to the same file should result
in no changes. This behavior is useful in CI, together with the -u
option, to confirm a proposed file with wikized references is up to date.

To process a file...

    ./wikize_refs.py foo.md

...creates/updates the output file foo-wikized.md.

To modify the input file in-place...

    ./wikize_refs.py -i foo.md

...which also backs up the original file as foo.md~.  Use option
-s to skip the backup on the input file in this case.

    ./wikize_refs.py --help

...prints command-line arguments and options.

If no *irreversible* options are used, the following sed pipe command
should be able to take the wikized file and produce the original...

cat <filename> | sed -e 's/^\[\(.*\)-sfer-ezikiw\]:/[\1]:/' | grep -v sfer-ezikiw

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
                      help="Warn instead of exit during (most) error checks.")

    parser.add_argument("-o", "--outfile",
                      default=None,
                      help="Specify an output file name. If none specified, will \
                            use <infile>-wikized.md or <infile>.md if -i option \
                            is specified")

    parser.add_argument("-s", "--skip-backup",
                      default=False,
                      action="store_true",
                      help="Disable creation of backup file appended with ~")

    parser.add_argument("-l", "--linkdef-db",
                      type=str, default=None,
                      action="append",
                      help="Specify name of file to use as a linkdef database from which \
                            to resolve footnote references in the file being processed. Any \
                            used linkdefs will be copied from that file to the file being \
                            processed here. Multiple -l options are allowed.")

    parser.add_argument("-c", "--check-links",
                      type=int, default=0,
                      help="Specify a timeout>0 in seconds for checking for broken links. \
                      Note: using this option does require network access to confirm URLs \
                      actually work.")

    parser.add_argument("-u", "--up-to-date",
                      default=False,
                      action="store_true",
                      help="Check if a file's refs are up to date. Return non-zero if so.")

    parser.add_argument("-i", "--in-place",
                      default=False,
                      action="store_true",
                      help="Modify input file in-place (irreversible).")

    parser.add_argument("-r", "--renumber",
                      type=int, default=0,
                      help="Renumber references starting from specified value > 0 (irreversible).")

    parser.add_argument("-g", "--gather-linkdefs",
                      default=False,
                      action="store_true",
                      help="Gather all link definitions to the end of the file (irreversible).")

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
    """A magic string to help identify lines produced by this tool"""
    return 'sfer-ezikiw'

def autogen_disclaimer():
    """Disclaimer message about autogenerated content"""
    return '<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (%s) -->'%magic()

def errors_are_fatal(x=None):
    """Encapsulate warn mode in a function for safer use as a global"""
    if not hasattr(errors_are_fatal, 'warn'):
         assert x is not None
         errors_are_fatal.warn = x
    return errors_are_fatal.warn

def message(msg):
    """Issue error message and possibly exit if errors are fatal"""
    if errors_are_fatal():
        print(msg)
        print("Either correct above errors or run with -w (--warn)")
        exit(1)
    else:
        print("%s -- IGNORING due to -w (--warn)"%msg)

# urlparse appears to allow all sorts of chars in path. So, it
# isn't clear how much utility this check really provides.
def valid_url(x):
    """Test that a given string is a valid URL"""
    try:
        ckparse = urlparse(x)
        return all([ckparse.scheme, ckparse.netloc, ckparse.path])
    except:
        return False

# It would be best to test the link without actually downlading
# the webpage. In theory, that requires a HEAD request and for
# typical webpages, requesting *just* the HEAD instead of the
# whole webpage isn't necessarily a big win.
def broken_link(x, timeout=20):
    """Test if a link appears to be working or broken"""

    broken_link.agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'

    if x.startswith('ftp://') or x.startswith('file:///') or \
       x.startswith('#'):
       return False

    req = Request(x, None, {'User-Agent': broken_link.agent})

    try:
        resp = urlopen(req, None, timeout)
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

def has_smart_curly_quotes(line):

    left_double = '\xe2\x80\x9c'
    right_double = '\xe2\x80\x9d'
    left_single = '\xe2\x80\x98'
    right_single = '\xe2\x80\x99'

    if left_double in line:
        return True
    if right_double in line:
        return True
    if left_single in line:
        return True
    if right_single in line:
        return True

    return False

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
        in_wrblock = False # a wikize refs block
        for line in mdf.readlines():
            line_type = ""
            if not in_frontmatter and re.match("^---$", line) and lineno == 1:
                line_type = "frontmatter"
                in_frontmatter = True
            elif in_frontmatter and re.match("^---$", line):
                line_type = "frontmatter"
                in_frontmatter = False
            elif not in_wrblock and re.match("^<!-- \(%s begin\) -->$"%magic(), line):
                line_type = "wrblock"
                in_wrblock = True
            elif in_wrblock and re.match("^<!-- \(%s end\) -->$"%magic(), line):
                line_type = "wrblock"
                in_wrblock = False
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
                elif in_wrblock:
                    line_type = "wrblock"
                elif is_link_def_line(line):
                    line_type = "linkdef"
                else:
                    line_type = "content"

            # Ignore general content lines that appear to be auto-generated
            if line_type == "content" and magic() in line:
                continue

            # Ignore wikize-ref blocks
            if line_type == "wrblock":
                continue

            # Ignore some special cases
            if line.startswith(autogen_disclaimer()):
                continue

            lines[lineno] = {'line':line, 'type':line_type} 
            if line_type == "linkdef":
                lines[lineno]['linkdef'] = is_link_def_line(line)
            lineno += 1

    return lines

def gather_fn_handles(file_lines):
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
                message("Duplicate footnote used between <sup>...</sup> at line %d."%k)
            fn_handles = fn_handles.union(set(fns2[0]))

        # detect cases of <sup>[x],[y],[z]</sup> 
        fns3 = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\]</sup>", fl)
        if fns3:
            if len(set(fns3[0])) != 3:
                message("Duplicate footnote used between <sup>...</sup> at line %d."%k)
            fn_handles = fn_handles.union(set(fns3[0]))

        # detect cases of <sup>[x],[y],[z],...</sup> 
        fns4p = re.findall("<sup>\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],\[([a-zA-Z0-9_-]*)\],(.*)</sup>", fl)
        if fns4p and len(fns4p[0]) >= 4:
            fn_handles = fn_handles.union(set(fns4p[0][:3]))
            message("Extra footnotes beyond 3 between <sup>...</sup> at line %d."%k)
            if len(set(fns4p[0][:3])) != 3:
                message("Duplicate footnote used between <sup>...</sup> at line %d."%k)

    return fn_handles

def build_ref_map(file_lines):
    """builds a map keyed by footnote handle with value
       [url, title, biblio, index-in-map]"""
    ref_map = {}
    has_basic_footnotes = False
    for phase in 1,2: 
        for k in sorted(file_lines):

            if file_lines[k]['type'] != 'linkdef':
                continue

            mdfparts = file_lines[k]['linkdef']
            if phase == 1 and len(mdfparts) != 4:
                message("Improperly parsed link definition at line %d"%k)
                continue

            ref_hdl, ref_url, ref_tit, ref_bib = mdfparts
            if phase == 1 and ref_hdl in ref_map:
                message("Repeated reference handle %s at line %d"%(ref_hdl,k))
                continue

            #
            # Handle only basic footnotes in phase 1 and only full
            # references in phase 2. This ensures that basic footnotes
            # have numerically smaller map-index entries than full
            # references.
            #
            if phase == 1 and ref_url != '#':
                continue
            if phase == 2 and ref_url == '#':
                continue

            if phase == 1:
                has_basic_footnotes = True

            #
            # Each ref_map entry is a 4 item list of the form
            #     [url, title, bibinfo, map-index]
            #
            ref_map[ref_hdl] = [ref_url, ref_tit, ref_bib]
            ref_map[ref_hdl].append(len(ref_map))

    return ref_map, has_basic_footnotes

def error_checks(file_lines, fn_handles, ref_map, check_links, has_lddbs):
    """
    Error checks footnote references and the link def reference list...
        - Ensure every footnote references an existing item in the ref list
        - Ensure every ref list item is referenced by at least one footnote
        - Ensure there are no smart quotes / curly quotes
        - Ensure URLs pass parsing rules
        - Ensure URL targets exist
    """
    ref_handles = set(ref_map.keys())
    missing_refs = fn_handles - ref_handles
    if missing_refs:
        message("Some footnotes never appear in the references%s...\n%s"%
            ("\nmaybe they will resolve in a linkdef database" if has_lddbs else "", str(list(missing_refs))))

    missing_fns = ref_handles - fn_handles
    if missing_fns:
        message("Some references never appear in a footnote...\n%s"%str(list(missing_fns)))

    # Check linkdef lines for smart quotes
    for k in sorted(file_lines):

        if file_lines[k]['type'] != 'linkdef':
            continue

        fl = file_lines[k]['line']

        if has_smart_curly_quotes(fl):
           message("Replace smart/curly quotes in link definition at line %d with straight quotes"%k)

    # Check references for titles
    for k in ref_map:
        tit = ref_map[k][1]
        if not tit:
            message("Reference labeled %s is missing title"%k)

    # Only ever produce warnings for missing bibliographic info
    if not errors_are_fatal():
        for k in ref_map:
            bib = ref_map[k][2]
            if not bib:
                message("Some references are missing bibliographic info.\nPlease consider adding it.")
                break

    if check_links:
        for k in ref_map:
            url = ref_map[k][0]
            if not valid_url(url):
                message("Invalid URL: \"%s\""%url)
            elif broken_link(url, check_links):
                message("Broken URL: \"%s\""%url)

    return missing_refs

def resolve_missing_refs(missing_refs, ref_map, lddbs):
    """
    Resolve references in the missing_refs list with linkdefs defined
    in additionally supplied files with --linkdef-dbs.
    """

    for lddb in lddbs:
        file_lines = gather_and_classify_file_lines(lddb)
        lddb_ref_map, hbfn = build_ref_map(file_lines)

        found_refs = []
        for x in missing_refs:
            if x in lddb_ref_map:
                ref_map[x] = [lddb_ref_map[x][0], lddb_ref_map[x][1], lddb_ref_map[x][2]]
                ref_map[x].append(len(ref_map))
                found_refs += [x]
        missing_refs = missing_refs - set(found_refs)
        if not missing_refs:
            break 

    if missing_refs:
        message("Some footnotes never resolved by any linkdef databases...\n%s"%str(list(missing_refs)))

#
# What renumber means here when we are building the main content is whether to
# use the footnote's original identifiers or to use their index in the ref_map
# (which is entry 3 in each ref_map list) plus the 'renumber' (option) offset.
# Later on, in build_reference_list_lines, if renumbering is active, we will
# sort the lines before emitting them so they appear in their sorted order in
# the visible reference list at the end of the article.
#
def build_main_content(file_lines, ref_map, renumber, gather_linkdefs):
    """
    Rebuilds the file lines possibly renumbering the footnotes
    """
    outlines = []

    for k in sorted(file_lines):

        lineinfo = file_lines[k]
        ltype = lineinfo['type']
        line = lineinfo['line']

        if ltype == 'linkdef':

            # Just skip linkdef lines if we're gathering 'em
            if gather_linkdefs:
                continue

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

    if gather_linkdefs:

        for k in sorted(file_lines):

            lineinfo = file_lines[k]
            ltype = lineinfo['type']
            line = lineinfo['line']

            if ltype != 'linkdef':
                continue

            ref_hdl, ref_url, ref_tit, ref_bib = lineinfo['linkdef']
            if magic() in line:
                # Its already mangled from a previous run
                outlines.append(line)
            else:
                # Mangle the linkdef to move it out of the way but nonetheless retain it
                outlines.append(line.replace(ref_hdl, "%s-%s"%(ref_hdl, magic()), 1))

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

def build_reference_list_lines(remapped_ref_map, renumber, has_basic_footnotes):
    """Build (auto-gen'd) rendered list of references."""
    outlines = []

    # First, assume just a single phase to output full references
    phases = ['refs']

    # If we have basic footnotes, then we have two phases
    if has_basic_footnotes:
        phases = ['bfns','refs'] # basic footnotes in first phase, full refs in 2nd

    for phase in phases:

        if remapped_ref_map:
            outlines.append("<!-- (%s begin) -->\n"%magic())
            if phase == 'bfns':
                outlines.append("### Footnotes\n")
            else:
                outlines.append("### References\n")
            outlines.append("<!-- (%s end) -->\n"%magic())
            try: # First, try to sort treating footnote identifiers as integers.
                if renumber:
                    sorted_map = sorted(remapped_ref_map.items(), key=lambda item: int(item[0]))
                else:
                    sorted_map = sorted(remapped_ref_map.items(), key=lambda item: int(item[1][3]))
            except: # If sorting as ints fails, sort lexicographically.
                sorted_map = sorted(remapped_ref_map.items(), key=lambda item: item[1][3])
            i = 0
            for k,v in sorted_map:
                if phase == 'bfns' and v[0] != '#':
                    continue
                if phase == 'refs' and v[0] == '#':
                    continue
                v3 = k+renumber if renumber else v[3]
                if v[1] and v[2]: # both title and bibinfo exist
                    outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>[%s<br>%s](%s)\n"%(magic(), v3, v3, v[1], v[2], v[0]))
                elif v[1]: # only title exists
                    if v[0] == '#':
                        outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>%s\n"%(magic(), v3, v3, v[1]))
                    else:
                        outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>[%s](%s)\n"%(magic(), v3, v3, v[1], v[0]))
                elif v[2]: # only bibinfo exists
                    outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>[%s](%s)\n"%(magic(), v3, v3, v[2], v[0]))
                else: # only url exists
                    outlines.append("* <a name=\"%s-%s\"></a><sup>%s</sup>[%s](%s)\n"%(magic(), v3, v3, v[0], v[0]))
                i += 1

    return outlines

def write_output_file(file_lines, out_lines, in_filename, out_filename, in_place, skip_backup):
    """Write the output file. But, only if it would be different than the input."""

    with open(in_filename, 'r') as inf:
        in_lines = inf.readlines()
        if str().join(out_lines) == str().join(in_lines):
            print("\"%s\" is up to date. No changes will be made."%in_filename)
            return 2

    # don't make the backup if asked not to
    if in_place and not skip_backup:
        copyfile(in_filename, "%s~"%in_filename)

    # ok, write the file
    outfname = out_filename if out_filename else in_filename
    with open(outfname, 'w') as outf:
        outf.writelines(["%s" % line for line in out_lines])

    return 1

#
# For basic design/operation, see usage notes (above)
#
def main(opts, mdfile):

    # Get and classify all lines in file
    file_lines = gather_and_classify_file_lines(mdfile)

    # Examine file lines for footnotes
    fn_handles = gather_fn_handles(file_lines)

    # Build a map of the references including their re-numbering
    ref_map, has_basic_footnotes = build_ref_map(file_lines)

    # Do some error checking
    missing_refs = error_checks(file_lines, fn_handles, ref_map,
        opts['check_links'], opts['linkdef_db'] is not None)

    # If we have missing references and linkdef-dbs are specified,
    # lets try to resolve them
    if missing_refs and opts['linkdef_db']:
        resolve_missing_refs(missing_refs, ref_map, opts['linkdef_db'])

    #
    # Ok, we're done processing the input file. Now, start building
    # the lines for the output file.
    #

    # First, build the main content lines with renumbered footnotes
    out_lines = build_main_content(file_lines, ref_map,
        opts['renumber'], opts['gather_linkdefs'])

    # Build a disclaimer line if we'll have generated content
    if ref_map:
        out_lines.append("%s\n"%autogen_disclaimer())
    
    # Build intermediate link definition lines
    remapped_ref_map = {v[3]:[v[0],v[1],v[2],k] for k,v in ref_map.items()}
    out_lines += build_intermediate_link_defn_lines(remapped_ref_map, opts['renumber'])

    # Build reference list lines
    out_lines += build_reference_list_lines(remapped_ref_map, opts['renumber'],
                     has_basic_footnotes)

    # Ok, now actually write the updated file
    flines = [file_lines[k]['line'] for k in sorted(file_lines)]
    return write_output_file(flines, out_lines, mdfile, opts['outfile'], opts['in_place'],
        opts['skip_backup'])

#
# So this python script can be used both as a shell command
# and as an imported python module.
#
if __name__ == '__main__':

    # Process command line options
    opts, mdfile = parse_args()

    # Initialize error mode
    errors_are_fatal(not opts['warn'])

    retval = main(opts, mdfile)

    # Set right error state if we're checking if file is up to date
    if opts['up_to_date'] and retval != 2:
        sys.exit(1)

    sys.exit(0)
