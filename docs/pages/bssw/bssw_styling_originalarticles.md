---
title: Original Articles Specific Styling Guidelines
sidebar: bssw_sidebar
permalink: bssw_styling_originalarticles.html
---

## Introduction

All GitHub file names for BSSw.io articles should follow the naming conventions laid out [here](https://betterscientificsoftware.github.io/bssw.io/bssw_file_naming.html).

An original article can highlight the following 2 types of resources: **(1) Blogs, (2) Short article.**

The main part of the original article consists of the (1) Deck, (2) Main body of the article and (3) Metadata. 

## Deck Section
As we know, all BSSw.io resources have decks and the deck has two parts: (1) deck text and (2) deck attributes. Following is guidance for "original articles" and their decks.

### Deck text/image
Original articles may have deck text and/or deck images. Deck text is usually a couple of lines about the event. Deck images creation is out-sourced by the BSSw.io team (for now). They are however added to articles, only after approval has been obtained from the authors.
 * Blogs *usually* have deck images and no deck text. 
 * Short articles *usually* have deck text. 
 * For guidance on the deck text, please see [common layout section](bssw_styling_common.html) of the guide.
 * Having deck text and a deck image in an original article are mutually exclusive
      * A way to approximate having both is to have the deck image and then put the deck as your first (short) paragraph after the image and italicize it.
 * Please note that many times in the BSSw.io literature the deck image is also called as hero image.
 * Images for content are stored in a different repository (and not the main repo). To reference the images in the article, we upload them [bssw.io images directory](https://github.com/betterscientificsoftware/images) and then reference them from the article.
 * There are some formatting tips described below for the deck images.
   - The formatting to include a deck/hero image is a bit finicky.
      * The `**Hero Image:**` tag must be followed by a blank line
      * The image itself must be in a Markdown list item (that is, it starts with `-`)
        ````
           - < img src="https://github.com/betterscientificsoftware/images/raw/master/IMAGE-NAME.png" />[IMAGE TEXT]
         ````
   - Positioning of the hero image relative to the contributor and publication date metadata doesn't matter.
   
### Deck Attributes

Mandatory deck attributes (such as Deck title, Contributor name, BSSw Categories, BSSw Topics) are part of deck for all BSSw.io content. Please see [common layout section](bssw_styling_common.html) of the guide for the mandatory deck attributes.

In addition to above, there exists a original content-specific deck attribute called Deck publication date. **Deck Publication date** is the date when the content was published on BSSw.io. In the source file, please use the following format:
````
#### Publication date: Month DD, YYYY
````

## Main Body Section

### General guidelines
* The content of the article is free-flowing.
* General guidance is 250-500 words, though this is flexible (some articles have been shorter, some a bit longer). 
* BSSw.io uses [GitHub-Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for original article markup
* BSSw.io team encourages authors to point to a modest number of additional resources that enhance your article. Too many links tend to distract readers.  In most cases, BSSw.io team would like to have the items authors refer to in BSSw.  These would usually be what BSSw.io calls "curated content", which means short items that provide a pointer to an external resource with a short description.  Authors are welcome to prepare those as separate contributions, and the BSSw.io team is happy to help.


### Structure of main body
The structure of the main body has two parts: (1) Content of the Article; and (2) Author bios. 

#### Content of the article
The content of the article is free-flowing. However it may have certain sections such as:
* Description (text, images)
* Acknowledgment
* Image Attribution
* References
* Logos

All reference links and images across all content types are handled in the same way; hence please see [common layout section](bssw_styling_common.html) of the guide.

#### Author Bios
This section has details of the author in a short paragraph. The content is free flowing.

## Metadata section
There is no specific guidance for this for the event content type. See [common metadata section](bssw_content_metadata.html) of the guide.

## Citations/References

Certain content types on [bssw.io](https://bssw.io) do not require formal reference styling (e.g. formal *citations*) either because the format is highly constrained (e.g. Events, Curated Content) or because the document is short and uses only a small number of inlined hyperlinks. There are, however, circumstances where formal reference styling (e.g. formal *citations*) is warranted. These include...

* Larger documents with *many* references that can benefit from formal reference styling to improve [readability and reading comprehension](https://www.psychologytoday.com/us/blog/your-childs-brain-and-behavior/201701/the-effects-digital-technology-reading?amp).

* Documents that reference multiple off-line materials (e.g. books) for which there is no, suitable on-line (e.g. hyperlink-able) proxy.

* Content that in the judgement of EB members and/or authors requires references to more fully support perhaps sensitive and/or controversial positions (e.g. the Covid19 article).

The decision to *allow* or *require* references is one that should be agreed upon by the author and EB members prior to developing the content. When references are to be used, we require authors to use the less intrusive [reference links](https://www.markdownguide.org/basic-syntax#reference-style-links) ([full spec](https://github.github.com/gfm/#reference-link)) and to follow the guidelines described [here](https://github.com/betterscientificsoftware/bssw.io/blob/master/Articles/Blog/ReferencesInMarkdownHybridApproach.md) where the [`wikize_refs.py`](https://github.com/betterscientificsoftware/bssw.io/blob/master/utils/README.md#wikize_refspy) tool can be helpful.

## Existing Examples

* A skeleton Markdown template for a blog article, which one can copy and customize is available at [this location](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/Articles/Blog/BlogArticleSkeletonA.md)

* A simple example of the usage of [formal citations/references](#citationsreferences) can be seen in in the file [WhenNotToWriteAutomatedTests.md](https://github.com/betterscientificsoftware/bssw.io/blob/master/Articles/Blog/WhenNotToWriteAutomatedTests.md).

* There are several examples available in the [betterscientificsoftware.github.io repository](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io) to use as a starting point.

{% include links.html %}
