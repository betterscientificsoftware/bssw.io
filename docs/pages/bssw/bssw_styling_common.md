---
title: Common Styling Elements Across all Content
sidebar: bssw_sidebar
permalink: bssw_styling_common.html
toc: true
---
## Introduction

All GitHub file names for BSSw.io articles should follow the naming conventions laid out [here](https://betterscientificsoftware.github.io/bssw.io/bssw_file_naming.html).

All BSSw.io resources have the following three sections, in common: 
- Deck
- Main body
- Metadata. 

The following image shows the deck and main body of a resource. Metadata section is not seen on the main site.

- <img src='https://github.com/betterscientificsoftware/images/raw/master/documentation-common-elements-small.jpg'/>

Following is a description of the common elements.

## Deck Section
The deck is the top shaded portion of the article. The elements of the deck are mostly the same across all the BSSw.io content types but with a few variations. The deck has two parts: (1) deck text/image and (2) deck attributes.

### Deck Text/Image
Most content types will have  the deck text, which is usually couple of lines highlighting the article. For curated content and events, deck text contains a two-sentence descriptive text about the resource. Some content types, such as original content, may have a deck image instead of the deck text, as described in the [original article styling](bssw_styling_originalarticles.html) section.

Following is some general guidance for deck text:
- Please add comments around deck text in the source file, as shown below: 
````
<!-- deck text start --> 
This is deck text 
<!-- deck text end -->
````
- No hyperlinks are allowed in the deck.
- If text is used, then the deck contains one or atmost two sentences about the article which piques user interest.
- Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized.

### Deck Attributes
The deck section, of every content type, will *always* contain the following *mandatory deck attributes*. These mandatory deck attributes may have some specific guidelines for the different content types, and these guidelines can be found in the styling guides for that particular content type. In general, the mandatory deck attributes are: (1) title of the article, (2) author/contributor/organizer names, and (3) BSSw.io topics that the article falls under. 

However, the different content types may have additional *content-specific deck attributes* as well. Please refer to the styling guides for each content type for these content-specific deck attributes.

#### Deck Title
A deck title should be simple and straighforward.
* The title of the article also becomes a portion of the article URL (as of Apr 2020); hence changing the title after publishing it is strictly discouraged.
* Conjuctions and Prepositions, used in the title, should be lowercase. Every other word should be sentence-case.

#### Contributor Name
This is name of the contributor/author/organizer. This contains the full name of the contributor and a URL, usually to the github profile, of the contributor. In the source file, please use the following format: 
````
#### Contributed by [Firstname Lastname](github profile url "Firstname Lastname")
````

#### BSSw Topics
These indicate which BSSw.io topic areas the article belongs to. The most up-to-date topic areas can be obtained from the BSSw.io website (click Resources link at https://bssw.io/ to find the list of topics). In the source file, the topics for the article can be indicated in the *[metadata section](bssw_content_metadata.html#categories)* of the article. 

## Main Body Section
The main body is the portion of the article below the deck. BSSw.io uses [Github-Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for writing content. The elements of the main body differ based on content type. The main body should explain the content from the perspective of the CSE community. There may be image file (e.g., logo, relevant diagram, science image) in the body text, although these are optional (but encouraged when this exists). Please read *styling rules* for individual types of content.

## Handling images
Images for content are stored in a different repository (and not the main repo). To reference the images in the article, we upload them [bssw.io images directory](https://github.com/betterscientificsoftware/images) and then reference them from the article.
- Add the following url. Using the "logo" class helps constrain the size of the image.
````
< img src='<img src='https://github.com/betterscientificsoftware/images/raw/master/YOUR-IMAGE-NAME.png' class='logo' />
````
- Please ensure we have permission to use the logo/image 
- Please ensure logo is clear and high resolution

## Metadata Section

We include metadata as *formatted comments* at the end of the file.  Metadata helps define rules about publishing an article, tagging them, selecting topics, etc. Be sure to include metadata with each entry, as this will be used to organize content, provide filters, and support searches on the BSSw front-end site. Please read the [common metadata section](bssw_content_metadata.html) to get detailed insight on the different metadata parameters and their importance.

## Citations/References

Certain content types on [bssw.io](https://bssw.io) do not require formal reference styling (e.g. formal *citations*) either because the format is highly constrained (e.g. Events, Curated Content) or because the document is short and uses only a small number of inlined hyperlinks. There are, however, circumstances where formal reference styling (e.g. formal *citations*) is warranted. These include...

* Larger documents with *many* references that can benefit from formal reference styling to improve [readability and reading comprehension](https://www.psychologytoday.com/us/blog/your-childs-brain-and-behavior/201701/the-effects-digital-technology-reading?amp).

* Documents that reference multiple off-line materials (e.g. books) for which there is no, suitable on-line (e.g. hyperlink-able) proxy.

* Content that in the judgment of EB members and/or authors requires references to more fully support perhaps sensitive and/or controversial positions (e.g. the Covid19 article).

The decision to *allow* or *require* references is one that should be agreed upon by the author and EB members prior to developing the content. When references are to be used, we require authors to use the less intrusive [reference links](https://www.markdownguide.org/basic-syntax#reference-style-links) ([full spec](https://github.github.com/gfm/#reference-link)) and to follow the guidelines described [here](https://github.com/betterscientificsoftware/bssw.io/blob/master/Articles/Blog/ReferencesInMarkdownHybridApproach.md) where the [`wikize_refs.py`](https://github.com/betterscientificsoftware/bssw.io/blob/master/utils/README.md#wikize_refspy) tool can be helpful.

## Unpublishing Content

Please follow the below rules

1. There needs to be  documentation about why content is being unpublished. On top of the content file, please add

   ````
   Date1: mm-dd-yyyy: Reason for unpublishing
   Date2: mm-dd-yyyy: Reason for unpublishing
   ````
 
2. Add the word UNPUB to file file name. For example: `GitversionUNPUB.md`


{% include links.html %}
