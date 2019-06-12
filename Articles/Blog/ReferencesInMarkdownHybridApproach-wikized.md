<!--- WARNING: Auto-generated with wikize_refs.py from ReferencesInMarkdownHybridApproach.md --->
# Wikipedia-Like Citations and References In GitHub Markdown

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: May 1, 2019

This document describes conventions in the use of 
[GitHub Flavored Markdown (GFM)][GFM]
([full spec](https://github.github.com/gfm/))
to implement [Wikipedia style](https://en.wikipedia.org/wiki/Note_(typography)#References)
footnote citations and references.

It is important to be aware that there are several implementations of markdown
and they don't all support the same features. Here, we are focused on the style of
markdown supported natively on GitHub, [GFM][GFM].

A key issue is that [GFM][GFM] does not support creation of user-defined *anchors*.
It does support implict *anchors* to level 1 (`#`) through level 6 (`######`)
headings which is too limited for our purposes here.

Features of this approach include...

- Separately listed/rendered references at end of article
- Bi-level linking
  - Footnote links on-page to reference table item
  - Reference table item links off-page to indended destination 
- Tool-tips/balloon-help teaser text about a link's topic/purpose
- Ease of use for authors
  - No need for duplication of link/reference content
- Mobile friendliness
- Maximally GitHib Markdown friendly
- Minimal use of in-line HTML
- Minimal post-processing for final publication-ready document

## List References as [GFM][GFM] Reference Style Links

Authors should use [GFM][GFM]
[reference style links](https://www.markdownguide.org/basic-syntax/#reference-style-links)
to define the list of references used in an article.

To do this, the author should list each reference used in the article using
a *link definition* line, by convention at the end of the markdown file, of
the form

    [<ID>]: <URL> "<DESC> {<BIB>}"

- All characters outside the `<` and `>` delimiters are *required*
- Must begin at column 0 in the markdown file
- `<ID>`: Alphanumeric identifier for the reference
- `<URL>`: The URL for the reference
- `<DESC>`: A short description of the reference (appears as tool-top/balloon-help hover)
- `<BIB>`: Full bibliographic information for the reference (Optional. Use `{}` if none)

Here, we are using the `{<BIB>}` entry as a *conventional* field inside the
[link title](https://www.markdownguide.org/basic-syntax#adding-titles) we have
defined to support our needs here.

Examples:

    [mcm]: https://wci.llnl.gov/codes/smartlibs/index.html "Smart Libraries {Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}"
    [1]: "Hello World {Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241}"
    [ale3d-paper]: https://wci.llnl.gov/simulation/computer-codes/ale3d " {}"

Note that link defintions such as this will not appear in the rendered HTML
for the document. This is taken care of with a Python post-processing script.

## Footnotes in GitHub Flavored Markdown
Authors can cite items in the list of references in their main article
flow using footnotes of the form `<sup>[<ID>]</sup>` where `<ID>` is the
identifier for a link and following proper style for footnote usage
following these rules

Reference numbers should appear:
- After the fact, quotation, or idea being cited
- Outside periods and commas
- Inside colons and semi-colons
- If citing more than one reference (max of 3) at the same point, separate the numbers with commas and no spaces between.

Examples:

    This drug is used to treat hepatitis.<sup>[2]</sup>

    Storing latex at high heat may cause degradation,<sup>[1],[2]</sup>
    but it is difficult to keep materials cool in a desert environment.

    Some physicians choose to store prescription pads in locked
    cabinets<sup>[3]</sup>; others keep them in their
    coats at all times.<sup>[2]</sup>

Which would appear as...

This drug is used to treat hepatitis.<sup>[2]</sup>

Storing latex at high heat may cause degradation,<sup>[1],[2]</sup>
but it is difficult to keep materials cool in a desert environment.

Some physicians choose to store prescription pads in locked
cabinets<sup>[3]</sup>; others keep them in their
coats at all times.<sup>[2]</sup>

Hover over the footnote links in the above and observe the
tool-tip/ballon-help.

## A Python Post Processing Script
Once an author is finished with all references, a python script
`wikize_refs.py` is provided to post-process the markdown file
creating a new markdown file. This script renumbers 1...N and
re-formats, slightly, footnotes and the series of reference style
links in a GitHub Markdown file so that the article's footnote
links behave more Wikipedia-like. In the new file, the original
reference style link definitions are copied over but commented out by
bracketing in `<!---` and `--->`. The renumbered and re-formatted
links are bi-level. Footnotes in the content link to entries in a
table of references. Entries in the table of references link off-page
to their intended destinations. The resulting file is still GitHub
flavored Markdown, with a minimal amount of embedded HTML and with
the references enumerated essentially twice; once for internal links
and once for the reference list at the end of the document.

For example, running script on this markdown file...

    ./wikize_refs.py ReferencesInMarkdownHybridApproach.md

produces the new markdown file [`ReferencesInMarkdownHybridApproach-wikized.md`](./ReferencesInMarkdownHybridApproach-wikized.md)


[GFM]: https://www.markdownguide.org/basic-syntax "Basic GitHub Flavored Markdown"

<br>

<!---
[mcm]: https://wci.llnl.gov/codes/smartlibs/index.html "Smart Libraries {Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}"
[1]: https:// "Hello World {Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241}"
[ale3d-paper]: https://wci.llnl.gov/simulation/computer-codes/ale3d " {}"

--->
<br>

[1]: #ref1 "Smart Libraries"
[2]: #ref2 "Hello World"
[3]: #ref3 ""

<br>

References | &nbsp;
:--- | :---
<a name="ref1"></a>1 | [Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636](https://wci.llnl.gov/codes/smartlibs/index.html)
<a name="ref2"></a>2 | [Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241](https://)
<a name="ref3"></a>3 | https://wci.llnl.gov/simulation/computer-codes/ale3d

<br>


