---
title: Wikipedia-Like Citations and References In GitHub Markdown
sidebar: bssw_sidebar
permalink: bssw_wikize_refs.html
toc: false
---

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: May 1, 2019

Managing a list of references and footnotes to them as is demonstrated in
[this bssw.io article](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap)
using *just* [GitHub Flavored Markdown (GFM)][GFM] (or, frankly, any
[markdown implementation](https://en.wikipedia.org/wiki/Markdown#Implementations)) is
not convenient.

Here, we describe conventions in the use of [GitHub Flavored Markdown (GFM)][GFM]
together with a Python post-processing script
[`wikize_refs.py`](https://github.com/betterscientificsoftware/bssw.io/blob/main/utils/README.md#wikize_refspy)
to make it easier to manage such references in a
[Wikipedia-like way](https://en.wikipedia.org/wiki/Note_(typography)#References).

A key issue is that [GFM][GFM] does not support easy creation of *user-defined*
anchors (other than by embedding raw html). The trick here is to use
[*reference style links*](https://github.github.com/gfm/#reference-link) and then
post-process the markdown file to auto-generate some additional markdown
and some embedded html.

## List References as [GFM][GFM] Reference Style Links

Authors should use [GFM][GFM]
[reference style links](https://www.markdownguide.org/basic-syntax/#reference-style-links)
to define the list of references used in an article.

To do this, the author should list each reference used in the article using
[*reference style links*](https://github.github.com/gfm/#reference-link) by convention
at the end of the markdown file, of the form

    [LAB]: URL "TIT {BIB}"

- Must begin at column 0 in the markdown file
- `LAB`: (**REQUIRED**) Alphanumeric *label* for the reference
  - **Note**: The post-processing script renumbers them 1...N
- `URL`: (**REQUIRED**) The URL for the reference
- `TIT`: (*optional*) A (short) title for the reference (will also appear as tool-tip during hover)
- `{BIB}`: (*optional*) Remaining full bibliographic information for the reference including the full title
  - The `{BIB}` field, embedded in a [markdown reference style link](https://github.github.com/gfm/#reference-link) [title](https://www.markdownguide.org/basic-syntax#adding-titles) is a notational *extension* specific to and known by only the `wikize_refs.py` tool.
- **Note**: Be sure whatever editor you are using is not inadvertently sneaking in [*smart quotes* or *curly quotes*](https://practicaltypography.com/straight-and-curly-quotes.html) and that you are using only *straight* quotes.
  If you are drafting content in whatever editor you have available locally and then cutting from that local editor and pasting into a web browser editing directly on GitHub, be aware that it is possible smart quotes can get carried along.

### Examples

    [mcm]: https://www.osti.gov/servlets/purl/936460 "Smart Libraries {Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}"
    [1]: https:// "Hello World {Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241}"
    [ale3d-paper]: https://wci.llnl.gov/simulation/computer-codes/ale3d
    [ascidmf-saf]: https://github.com/markcmiller86/SAF/blob/master/src/safapi/docs/miller001.pdf "The SAF Data Model"

In the first example, the various entries are given as...
* `[LAB]:` is the label `[mcm]:`
* `URL` is the link `https://www.osti.gov/servlets/purl/936460`
* `TIT` is a short title `Smart Librares`
* `{BIB}` is the full bibliographic entry, `{Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}` which includes the full title.
* Note that the `TIT` followed by `{BIB}` entries are together bracketed by opening and closing double quotes, `"`.

Note that the second example with label `[1]:` is an example of a journal citation with no URL.
It contains just an incomplete URL, `https://`, for the `URL` field.
The third example with label `[ale3d-paper]:` has only the `URL` field.
The fourth example, with label `[ascidmf-saf]:` has the `URL` and a short title for the `"TIT"` field.

In (most) markdown processors, link definitions such as this will not appear in the rendered HTML for the document.
Thus, in order to make them appear, we post-process the file with a Python script, `wikize_refs.py` which adds various auto-generated content to the *bottom* of the file to support the better referencing style. More on that later.

## Footnotes in GitHub Flavored Markdown

Authors can cite items in the list of references in their main article
flow using footnotes of the form `<sup`&#8203;`>[LAB]<`&#8203;`/sup>` where `LAB` is the
identifier for a link and following proper grammatical style for footnote
usage following these rules.

Reference numbers should appear:
- After the fact, quotation, or idea being cited
- Outside periods and commas
- Inside colons and semi-colons
- If citing more than one reference (max of 3) in the same footnote,
  separate the numbers with commas and no spaces between like so (`<sup`&#8203;`>[1],[2],[3]<`&#8203;`/sup>`).

### Examples

    This drug is used to treat hepatitis.<sup>[1]</sup>

    Storing latex at high heat may cause degradation,<sup>[mcm],[1]</sup>
    but it is difficult to keep materials cool in a desert environment.

    Some physicians choose to store prescription pads in locked
    cabinets<sup>[ale3d-paper]</sup>; others keep them in their
    coats at all times.<sup>[1]</sup>

Which would appear as...

---

This drug is used to treat hepatitis.<sup>[1]</sup>

Storing latex at high heat may cause degradation,<sup>[mcm],[1]</sup>
but it is difficult to keep materials cool in a desert environment.

Some physicians choose to store prescription pads in locked
cabinets<sup>[ale3d-paper]</sup>; others keep them in their
coats at all times.<sup>[1]</sup>

---

Hover over the footnote links in the above and observe the
tool-tip text that appears. Note also that you do not see any
explicit list of the references these footnotes refer to here
in the rendered markdown file. This is because link reference
definitions in [GFM][GFM] are designed to *not* appear in the
final rendered HTML. To work-around this issue, we post-process
the markdown file producing an altered markdown file that has
the desired behavior.

## A Python Post Processing Script

A python script `wikize_refs.py` is provided to post-process a markdown file.
This script renumbers the footnotes 1...N and re-formats them slightly so that
the article's footnote links behave more Wikipedia-like.

In the following figures, we demonstrate repeated use of `wikize_refs.py`. In the
first invocation (figure 1), the originally authored file (left) is processed
producing a new file (right) where the author's original footnote and reference
numbering is modified, slightly and new content to support the Wikipedia-style
referencing is added to the bottom of the file.

![](https://raw.githubusercontent.com/betterscientificsoftware/images/mcm86-19feb21-inplace-wikize-refs/wikize-refs-docs1.png)

In subsequent work, the author makes further edits the file (stuff in red in the
figure below), adding some content and a new footnote and reference.

![](https://raw.githubusercontent.com/betterscientificsoftware/images/mcm86-19feb21-inplace-wikize-refs/wikize-refs-docs2.png)

Nonetheless, even after the author has edited the file further, the `wikize_refs.py`
tool can be re-applied to the resulting file. This is demonstrated in the figure
below (stuff in purple is what winds up being changed in this invocation).

![](https://raw.githubusercontent.com/betterscientificsoftware/images/mcm86-19feb21-inplace-wikize-refs/wikize-refs-docs3.png)

In this way, authors need only concern themselves with the main content and their
list of references. The added content to support Wikipedia-style referencing at
the bottom of the file is always re-generated from the author's content

### How `wikize_refs.py` works

The script adjusts, slightly, a markdown file so that any footnotes using reference-style markdown links and link-definitions behave more Wikipedia-like.
This can be accomplished by simply name-mangling the author's original link labels (to move them out of the way) and *adding* some lines to the file.

The author's *original* link labels get mangled.
This has the effect of breaking their connection to the footnotes referencing them.
This is later repaired when a new set of link definitions are appended to the end of the file.

The new links are bi-level.
Footnotes in the content link to entries in a visible list of references appended to the end of the document.
Items in the list of references link off-page to their intended destinations.
The resulting file is still GitHub flavored Markdown with a minimal amount of embedded HTML.

If the file contains no footnotes, it will be left unchanged.
Some minimal error checks are that there is an existing link definition for every footnote and that every link definition appears in at least one footnote.
It will also check that links are valid.
If errors are fatal, processing will stop upon encountering an error.
Otherwise only warning messages are produced.

Some of the options can be *destructive* in that the file is changed in ways not easy to reverse.

Repeated application of this tool with the same arguments to the same file should result in no changes.

To process a file...

```
./wikize_refs.py foo.md
```

...creates/updates the output file foo-wikized.md.

```
./wikize_refs.py --help
```

...prints command-line arguments and options.

If no *destructive* options are used, the following sed pipe command should be able to take the wikized file and produce the original...

```
cat foo.md | sed -e 's/^\[\(.*\)-sfer-ezikiw\]:/[\1]:/' | grep -v sfer-ezikiw
```

The script reads a markdown file and classifies its lines as either *frontmatter* (in case we ever use Jekyll) *content*, *xml-comments*, or *link definitions*.
It ignores any lines that contain the string `sfer-ezikiw` (which is `wikize-refs` spelled backwards) as such lines are auto-generated by the script.
It then scans all content lines for instances of footnotes (e.g. `<sup`&#8203;`>[LAB]<`&#8203;`/sup>`) and scans all link definition lines for their four components: `LAB`, `URL`, `TIT` and `BIB`.

All of these lines are then re-output, with options to re-number the footnotes as well as gather together at the bottom any link definitions.
There is no requirement that all the link definitions appear at the bottom of the file or that any other file parts (e.g. bssw.io metadata comments) appear in any specific order or place in the file.

## Advantages of this Approach

- Separately listed/rendered table of references at end of article
- Bi-level, Wikipedia style linking
  - Footnotes in the main content links on-page to reference table items
  - Reference table items link off-page to their intended destinations
- When hovering, tool-tip text appears with the link's title
- Mobile friendliness
- Maximally GitHub Markdown friendly
- Minimal use of in-line HTML
- Minimal post-processing for final publication-ready document
- A single source for the references defined as a list of
  [*reference style links*](https://github.github.com/gfm/#reference-link)
  - This single source is used to auto-generate the additional reference
    related lists in the file.
- The script can be repeatedly re-applied to a file and operate in place

[mcm]: https://www.osti.gov/servlets/purl/936460 "Smart Libraries {Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}"
[1]: https://# "Hello World {Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241}"
[ale3d-paper]: https://wci.llnl.gov/simulation/computer-codes/ale3d " {}"

[GFM]: https://www.markdownguide.org/basic-syntax "Basic GitHub Flavored Markdown"
