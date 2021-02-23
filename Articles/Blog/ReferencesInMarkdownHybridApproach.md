# Wikipedia-Like Citations and References In GitHub Markdown

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: May 1, 2019

Managing a list of references and footnotes to them as is demonstrated in
[this bssw.io article](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap)
using *just* [GitHub Flavored Markdown (GFM)][GFM] (or, frankly, any
[markdown implementation](https://en.wikipedia.org/wiki/Markdown#Implementations)) is
not convenient.

Here, we describe conventions in the use of [GitHub Flavored Markdown (GFM)][GFM]
together with a Python post-processing script
[`wikize_refs.py`](https://github.com/betterscientificsoftware/bssw.io/blob/master/Articles/Blog/wikize_refs.py)
to make it easier to manage such references in a
[Wikipedia-like way](https://en.wikipedia.org/wiki/Note_(typography)#References).

Here, we focus on the use of [GFM][GFM] and, in particular,
[*reference style links*](https://github.github.com/gfm/#reference-link).
A key issue is that [GFM][GFM] does not support easy creation of *user-defined*
anchors (other than by embedding raw html). It does support *implict* anchors to level
1 (`#`) through level 6 (`######`) headings but this is too limited for our purposes
here.

## List References as [GFM][GFM] Reference Style Links

Authors should use [GFM][GFM]
[reference style links](https://www.markdownguide.org/basic-syntax/#reference-style-links)
to define the list of references used in an article.

To do this, the author should list each reference used in the article using
[*reference style links*](https://github.github.com/gfm/#reference-link) by convention
at the end of the markdown file, of the form

    [<ID>]: <URL> "<TIT> {<BIB>}"

- All characters outside the `<` and `>` delimiters are *required*
- Must begin at column 0 in the markdown file
- `<ID>`: (**REQUIRED**) Alphanumeric identifier for the reference
- `<URL>`: (**REQUIRED**) The URL for the reference
- `<TIT>`: (*optional*) A title for the reference (appears as tool-tip during hover)
- `<BIB>`: (*optional*) Full bibliographic information for the reference
  - Here, we are using the `{<BIB>}` field, embeded between `{` and `}` in the
    [link's title](https://www.markdownguide.org/basic-syntax#adding-titles) text
    as a notational *extension*.

Examples:

    [mcm]: https://wci.llnl.gov/codes/smartlibs/index.html "Smart Libraries {Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}"
    [1]: "Hello World {Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241}"
    [ale3d-paper]: https://wci.llnl.gov/simulation/computer-codes/ale3d

In (most) markdown processors link defintions such as this will, by convention,
not appear in the rendered HTML for the document. Thus, in order to make them 
appear, we post-process the file with a Python script, `wikize_refs.py` which
adds various auto-generated content to the *bottom* of the file to support
the better referencing style. More on that later.

## Footnotes in GitHub Flavored Markdown
Authors can cite items in the list of references in their main article
flow using footnotes of the form `<sup>[<ID>]</sup>` where `<ID>` is the
identifier for a link and following proper style for footnote usage
following these rules

Reference numbers should appear:
- After the fact, quotation, or idea being cited
- Outside periods and commas
- Inside colons and semi-colons
- If citing more than one reference (max of 3) in the same footnote,
  separate the numbers with commas and no spaces between like so (`<sup>[1],[2],[3]</sup>`).

Examples:

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

In the new file, the original reference style link definitions are copied over
but re-numbered and commented out by bracketing them in XML comments `<!---` and
`--->`. The script also adds auto-generated content based on the original
list references. The renumbered and re-formatted links are bi-level. Footnotes in
the main content link to entries in a table of references. Entries in the table of
references link off-page to their intended destinations. The resulting file is
still GitHub flavored Markdown, with a minimal amount of embedded HTML.

For example, running script on this markdown file...

    ./wikize_refs.py ReferencesInMarkdownHybridApproach.md

copies the original file to `ReferencesInMarkdownHybridApproach.md~` and
then overwrites the original file with footnotes
produces the new markdown file [`ReferencesInMarkdownHybridApproach-wikized.md`](./ReferencesInMarkdownHybridApproach-wikized.md)

To view and compare the actual markdown of both of these files on
GitHub, use the `Raw` button next to `Raw | Blame | History` in the
upper right corner of the file(s) or follow the links below.





Advantages of the approach taken here include...

- Separately listed/rendered table of references at end of article
- Bi-level linking
  - Footnotes in the main content links on-page to reference table items
  - Reference table items link off-page to their indended destinations
- When hovering, tool-tip text appears with the link's title
- Mobile friendliness
- Maximally GitHib Markdown friendly
- Minimal use of in-line HTML
- Minimal post-processing for final publication-ready document
- A single source for the references defined as a list of
  [*reference style links*](https://github.github.com/gfm/#reference-link)
  - This single source is used to auto-generate the additional reference
    related lists in the file.


- [Raw Original](https://raw.githubusercontent.com/betterscientificsoftware/betterscientificsoftware.github.io/master/Articles/Blog/ReferencesInMarkdownHybridApproach.md)
- [Raw Post-Processed](https://raw.githubusercontent.com/betterscientificsoftware/betterscientificsoftware.github.io/master/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md)

[mcm]: https://wci.llnl.gov/codes/smartlibs/index.html "Smart Libraries {Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}"
[1]: https:// "Hello World {Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241}"
[ale3d-paper]: https://wci.llnl.gov/simulation/computer-codes/ale3d " {}"

[GFM]: https://www.markdownguide.org/basic-syntax "Basic GitHub Flavored Markdown"
