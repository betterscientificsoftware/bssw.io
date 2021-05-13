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
[`wikize_refs.py`](../../utils/README.md#wikize_refspy)
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

    [ID]: URL "TIT {BIB}"

- Must begin at column 0 in the markdown file
- `ID`: (**REQUIRED**) Alphanumeric identifier for the reference
  - **Note**: The post-processing script renumbers them 1...N
- `URL`: (**REQUIRED**) The URL for the reference
- `TIT`: (*optional*) A title for the reference (appears as tool-tip during hover)
- `{BIB}`: (*optional*) Full bibliographic information for the reference
  - Here, we are using the `{BIB}` field, embedded in the [link's title](https://www.markdownguide.org/basic-syntax#adding-titles) text as a notational *extension*.
- **Note**: Be sure whatever editor you are using is not inadvertently sneaking in [*smart quotes* or *curly quotes*](https://practicaltypography.com/straight-and-curly-quotes.html) and that you are using only *straight* quotes.
  If you are drafting content in whatever editor you have available locally and then cutting from that local editor and pasting into a web browser editing directly on GitHub, be aware that it is possible smart quotes can get carried along.

Examples:

    [mcm]: https://wci.llnl.gov/codes/smartlibs/index.html "Smart Libraries {Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}"
    [1]: "Hello World {Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241}"
    [ale3d-paper]: https://wci.llnl.gov/simulation/computer-codes/ale3d

In (most) markdown processors link definitions such as this will, by convention,
not appear in the rendered HTML for the document. Thus, in order to make them 
appear, we post-process the file with a Python script, `wikize_refs.py` which
adds various auto-generated content to the *bottom* of the file to support
the better referencing style. More on that later.

## Footnotes in GitHub Flavored Markdown

Authors can cite items in the list of references in their main article
flow using footnotes of the form `<sup`&#8203;`>[ID]<`&#8203;`/sup>` where `ID` is the
identifier for a link and following proper grammatical style for footnote
usage following these rules.

Reference numbers should appear:
- After the fact, quotation, or idea being cited
- Outside periods and commas
- Inside colons and semi-colons
- If citing more than one reference (max of 3) in the same footnote,
  separate the numbers with commas and no spaces between like so (`<sup`&#8203;`>[1],[2],[3]<`&#8203;`/sup>`).

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

The `wikize_refs.py` script treats the document structure in four successive
blocks...

1. The main content block, including any bssw.io metadata, *above* link
   definitions.
1. The author's link definitions block (which upon output will be *hidden* from
   markdown processing by XML comment bracketing).
1. An *intermediate* link definitions block (lines beginning with `^[J]: #refJ`)
   for internal links to the table of references.
1. The table of references (lines beginning with `^<a name="refJ"></a>J | [`) for
   actual links to referenced content.

Blocks 2, 3 and 4 are optional. Blocks 3 and 4, which support the Wikipedia style
references, are generated from block 2 if it exists. Repeated application of
`wikize_refs.py` will result in no changes to the file. Intermediate link definition
lines of the form `^[J]: #refJ` are ignored. These are re-generated anew upon each
invocation. Likewise, reference table lines of the form `^<a name="refJ"></a>J | [`
are also ignored. These too will be re-generated anew upon each invocation.

Link definitions as *authored*, if they exist, all appear together in a block at the
*bottom* of the file, *after* the main content and even after any bssw.io metadata
blocks. Thus, in line-by-line processing, the *first* such link definition line is
used to demarcate the end of the main content block and the beginning of the author's
link definition block.

The author's link definitions are renumbered 1...N and all footnote references in the
main content are updated accordingly. These link definitions are output but bracketed by
multi-line XML comments to hide them from any markdown processing.

The renumbered and re-formatted links are bi-level. Footnotes in the content link to
entries in a table of references at the bottom of the document. Items in the table of
references link off-page to their intended destinations. The resulting file is still
GitHub flavored Markdown with a minimal amount of embedded HTML.

For example, running this script on this markdown file...

    ./wikize_refs.py -i ReferencesInMarkdownHybridApproach.md

makes a backup of the original file to `ReferencesInMarkdownHybridApproach.md~` and
then overwrites the original file. Use the `-s` option to skip this backup
operation.

Comparing the [raw original](https://raw.githubusercontent.com/betterscientificsoftware/betterscientificsoftware.github.io/master/Articles/Blog/ReferencesInMarkdownHybridApproach.md)
version of this file to the
[raw post-processed](https://raw.githubusercontent.com/betterscientificsoftware/betterscientificsoftware.github.io/master/Articles/Blog/ReferencesInMarkdownHybridApproach-wikized.md)
version can also be helpful in understanding what the script is doing (and diffing the raw files locally is also very informative).

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

[mcm]: https://wci.llnl.gov/codes/smartlibs/index.html "Smart Libraries {Miller MC, Reus JF, Koziol QA, Cheng AP. December 2004. Smart Libraries: Best SQE Practices for Libraries with an Emphasis on Scientific Computing. Proc. NECDC UCRL-JRNL-208636}"
[1]: https:// "Hello World {Miller MC. March 2026 Hello World in 500 different languages. Jrnl of Computer Science 5(3):237-241}"
[ale3d-paper]: https://wci.llnl.gov/simulation/computer-codes/ale3d " {}"

[GFM]: https://www.markdownguide.org/basic-syntax "Basic GitHub Flavored Markdown"
