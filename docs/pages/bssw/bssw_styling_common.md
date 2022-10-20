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
- Blog articles must have *either* a hero image or deck text.

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

## Handling absolute and relative links/URLs
Several times, BSSw.io content will contain links to resources which are hosted in the bssw.io site itself. Such links are treated as internal links and they should be relative and should point to the actual ".md" file. They should not point to the absolute URL of the linked article on the bssw.io site.

- Example: If one refers to an article called foo.md, it should be refered to as something like  "../../blog/foo.md" (depending on the relative location in the github reposity) rather than absolute (which is the URL on the bssw.io site and may perhaps be something like https://bssw.io/items/some-words-indicating-title-of-linked-article.html)

When bssw.io content contains links to resources which are hosted external to the bssw.io website, then those links have to be the absolute URL. 

## Handling images

From structural perspective, there are two types of images.  *Hero* images appear at the top of blog articles, and are also use to highlight the article in the [blog list](https://bssw.io/blog_posts) when it is newly published. *Body* images appear in the body of the article and are available in any article type.

### General notes

- Please ensure we have permission to use the logo/image
- Please ensure image is clear and high resolution
- Please remember to commit the image file with the `*.md` file on your git branch
- Add an image credit as appropriate.
- Captions are optional (and in general, mildly discouraged) and must immediately follow the img tag if used.
- Captions should not include hyperlinks.  They are undesirable from the design standpoint: it disrupts reading the text (your eye jumps straight to the link) and any critical links would be best placed in the story itself.  Further, hyperlinks prevent the front-end from actually interpreting the caption as a caption.
- If we are providing image credits that include links, it seems unnecessary to link to the image resource, especially if not a scientific source, even if the URL is part of the identifier. (For example, we did not to link to nasa.gov on the Apollo series since it is such a vast resource, we credited Image Source: NASA.)

### Where to store images

Images for bssw.io content are stored in the main `bssw.io` repository in the `images/` subdirectory.

### Hero images

Only blog articles use heros. 
The hero immediately follows the title in the article's `*.md` file:

```
**Hero Image:**
 
- <img src='../../images/YOUR-IMAGE-NAME.png' />
```

- Blog articles must have *either* a hero image or deck text.

- Hero image captions: Many images are illustrative and self-explanatory or have tangential relevance to the article (e.g. data visualization) so a caption is unnecessary. With images that benefit from descriptions that provide insight into the BSSw activities or the rigorousness of the science we have added a sentence of text. For an example, see <https://github.com/betterscientificsoftware/bssw.io/blob/master/Articles/Blog/2020-11-PSIP4HDF5.md> (source) and <https://bssw.io/blog_posts/recent-successes-with-psip-on-hdf5> (rendered).

- Hero image credits: We've come up with a way to lead the article but not detract from the lede paragraph by leading body text with image credits but shrinking them with a superscript tag. For an example, see <https://github.com/betterscientificsoftware/bssw.io/blob/master/Articles/Blog/2021-03-useful-practices-for-SEoMsDSP.md> (source) and <https://bssw.io/blog_posts/useful-practices-for-software-engineering-on-medium-sized-distributed-scientific-projects> (rendered).

### Body images

Images can appear anywhere in the body of any type of article, but they should be used judiciously.  We do *not* use the normal Markdown specification for images.  Instead, use:

````
<br>
<img src='../../images/YOUR-IMAGE-NAME.png' class='logo'/>[optional caption]
<br>
````

- All body images should include a `class` specification to ensure proper styling (details below).
- The `<br>` tags should be included to ensure proper spacing around he image.
- Body image captions: Body images can be esoteric or diagrammatic and often need clarification. We prefer to limit these to two sentences max, but that's not a hard rule. And as stated above, critical links should be in the body text.

### Use of image classes

We can accommodate images of all shapes in the main text area and have come up with standard styles to allow them to appear appropriately alongside text content. You should define one of three different classes when you place your image tag. Not indicating a class will cause display problems.

- Use the `logo` class for images like headshots or logos, to constrain then to a width of 202 px. (Logos with a horizontal orientation may scale quite small, portraits should be cropped to square proportions.)
- Use the `page` class to ensure your image conforms to a 775 x 450 px proportion no matter its shape. Your image will appear bounded by a grey box.
- Use the `page lightbox` class for vertical images, diagrams, or images with small details to present an image that can be expanded to fill the screen. (Not recommended for images under 1000 px wide.)

## Metadata Section

We include metadata as *formatted comments* at the end of the file.  Metadata helps define rules about publishing an article, tagging them, selecting topics, etc. Be sure to include metadata with each entry, as this will be used to organize content, provide filters, and support searches on the BSSw front-end site. Please read the [common metadata section](bssw_content_metadata.html) to get detailed insight on the different metadata parameters and their importance.

## Citations/References

Certain content types on [bssw.io](https://bssw.io) do not require formal reference styling (e.g. formal *citations*) either because the format is highly constrained (e.g. Events, Curated Content) or because the document is short and uses only a small number of inlined hyperlinks. There are, however, circumstances where formal reference styling (e.g. formal *citations*) is warranted. These include...

* Larger documents with *many* inlined hyperlinks that can benefit from formal reference styling to improve [readability and reading comprehension](https://www.psychologytoday.com/us/blog/your-childs-brain-and-behavior/201701/the-effects-digital-technology-reading?amp).

* Documents that reference multiple off-line materials (e.g. books) for which there is no, suitable on-line (e.g. hyperlink-able) proxy.

* Content that in the judgment of EB members and/or authors requires references to more fully support perhaps sensitive and/or controversial positions (e.g. the Covid19 article).

The decision to *allow* or *require* references is one that should be agreed upon by the author and EB members prior to developing the content. When references are to be used, we require authors to use the less intrusive [reference links](https://www.markdownguide.org/basic-syntax#reference-style-links) ([full spec](https://github.github.com/gfm/#reference-link)) and to follow the guidelines described [here](bssw_wikize_refs.html) where the [`wikize_refs.py`](https://github.com/betterscientificsoftware/bssw.io/blob/master/utils/README.md#wikize_refspy) tool can be helpful.

## Nonstandard handling of Markdown

The [bssw.io] site uses as custom tool to translate the Markdown in each `*.md` file into HTML.
This tool deals with Markdown differently in several ways compared to other common Markdown renderers (such as GitHub and GitHub Pages).
It is important to know about these differences up front to avoid problems once the `*.md` files are previewed on preview.bssw.io and finally published to [bssw.io].
Here, we list some of the major differences in how Markdown is handled that we currently know about.

### Page URL on bssw.io is generated from first the title

The URL of the page on the bssw.io site is the "slugified" text of the title (level 1 section heading) in the article.md file.  The [slug](https://en.wikipedia.org/wiki/Clean_URL#Slug) is basically the lowercase version of the text with the punctuation removed and hyphens (`-`) replacing spaces.
For example, the file `ATPESC.md` with the title `# Preparing the Next Generation of Supercomputer Users` is given, the slug `preparing-the-next-generation-of-supercomputer-users` will be used in the URL on the bssw.io site.
When the same title occurs in multiple articles on bssw.io, a random character string is appended to the slug to ensure uniqueness.

### Section links are not supported

Where most standard Markdown renderers will create a internal link for (sub)section headers, the bssw.io site generator will not.
For example, the section name `## Nonstandard handling of Markdown` would typically trigger the creation of the HTML anchor `nonstandard-handling-of-markdown` which allows referring to that section using references like `[nonstandard handling](#nonstandard-handling-of-markdown)` (on the same page).
But the bssw.io site generator will not create these section anchors.
To get around this problem, one can manually add an anchor like `<a name="nonstandard-handling-of-markdown"></a>` directly above the section `## Nonstandard handling of Markdown` in the `*.md` file and then links to `#nonstandard-handling-of-markdown` will work.
(NOTE: This also works with the GitHub Markdown renderer as well and does not create a conflict.)

### Words with two underscores become *emphasis* markers

For example, a raw word with two or more underscores "`_`" like "this_has_underscores" will get translated to the HTML `this<em>has</em>underscores`.
Since this is typically not what you want, consider replacing underscores "`_`" with dashes "`-`" or use unformatted text with:

```
`this_has_underscores`
```

### Tables with more than 4 columns are too wide

It would seem that the custom bssw.io Markdown site generator has problems with tables with more than 4 columns.
If a table has 5 or more columns, then those columns extend past the right margin of the text on the page.
For example, the table in [one of the AGC articles](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap) has 5 columns and has column spacing that is too wide and extends beyond the right margin.
It seems that the column widths in this table could be compressed to easily fit in the margins and still be very readable.

NOTE: We will add more examples of nonstandard handling of Markdown in the future as we discover them.



## Updating/re-publishing published articles

Articles that are already published and are current public may sometimes need to be updated. Minor updates such as grammar/spellings/errors/formatting can be done anytime. If you wish to make siginificant updates to the articles (for ex: new updates links, new content etc.) OR if you simply wish to bring the article into focus again with a new publish date, then please mention the following verbiage at the *end of the article*.

```
This article was originally published on Month day, year
```

## Unpublishing Content

Please follow the below rules

1. There needs to be  documentation about why content is being unpublished. On top of the content file, please add

   ````
   Date1: mm-dd-yyyy: Reason for unpublishing
   Date2: mm-dd-yyyy: Reason for unpublishing
   ````
 
2. Add the word UNPUB to file file name. For example: `GitversionUNPUB.md`

<!-- Common hyperlinks/>

[bssw.io]: https://bssw.io
[preview.bssw.io]: https://preview.bssw.io

{% include links.html %}
