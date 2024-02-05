---
title: Blog Specific Styling Guidelines
sidebar: bssw_sidebar
permalink: bssw_styling_blogs.html
---

## Introduction

**Note**: In Feb 2024, with the establishment of the *tracks* feature in blog, the term "original article" was deprecated.

All GitHub file names for BSSw.io blogs should follow the naming conventions laid out [here](https://betterscientificsoftware.github.io/bssw.io/bssw_file_naming.html).

The main part of the blog consists of the (1) Deck, (2) Main body of the blog and (3) Metadata. 

## Deck Section
All BSSw.io resources have decks and the deck has two parts: (1) deck text/image and (2) deck attributes. Following is guidance for the deck area for blogs.

### Deck text/image
Blogs may have deck text OR deck images, but not both. Deck text is usually a couple of lines about the event. Deck images creation is out-sourced by the BSSw.io team (for now). They are however added to blog, only after approval has been obtained from the authors.
 * For guidance on the deck text, please see [common layout section](bssw_styling_common.html) of the guide.
 * Having deck text and a deck image in a blog are mutually exclusive. A way to approximate having both is to have the deck image and then put the deck as your first (short) paragraph after the image and italicize it.
 * Please note that many times in the BSSw.io literature the deck image is also called as hero image.
 * Images for content are stored under the `images/` directory in the main `bssw.io` repository. To reference the images in the blog, we put in a relative path (see [images/README.md](https://github.com/betterscientificsoftware/bssw.io/blob/main/images/README.md)).
 * There are some formatting tips described below for the deck images.
   - The formatting to include a deck/hero image is a bit finicky.
      * The `**Hero Image:**` tag must be followed by a blank line
      * The image itself must be in a Markdown list item (that is, it starts with `-`) <br>
        `- < img src="../../images/IMAGE-NAME.png" />[IMAGE TEXT]`
   - Positioning of the hero image relative to the contributor and publication date metadata doesn't matter.
   
### Deck Attributes

Mandatory deck attributes (such as Deck title, Contributor name, BSSw Topics) are part of deck for all BSSw.io content. Please see [common layout section](bssw_styling_common.html) of the guide for the mandatory deck attributes.

In addition to above, there exists a blog-specific deck attribute called Deck track and  publication date. 

**Deck track** refers to the *track* to which the blog belongs. In the source file, the *track* for the blog can be indicated in the *[metadata section](bssw_content_metadata.html#track)* of the blog. You can see a list of current tracks, supported by BSSw.io, in [metadata section](bssw_content_metadata.html#track) of this site.

**Deck Publication date** is the date when the content was published on BSSw.io. In the source file, please use the following format:
````
#### Publication date: Month DD, YYYY
````

## Main Body Section

### General guidelines
* The content of the blog is free-flowing.
* General guidance is 250-500 words, though this is flexible. Blogs belonging to certain tracks such as *Deep dive* tend to be much longer.
* BSSw.io uses [GitHub-Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for blog markup
* BSSw.io team encourages authors to point to a modest number of additional resources that enhance your blog. Too many links tend to distract readers.  In most cases, BSSw.io team would like to have the items authors refer to in BSSw.  These would usually be what BSSw.io calls "curated content", which means short items that provide a pointer to an external resource with a short description.  Authors are welcome to prepare those as separate contributions, and the BSSw.io team is happy to help.


### Structure of main body
The structure of the main body has two parts: (1) Content of the Blog; and (2) Author bios. 

#### Content of the blog
The content of the blog is free-flowing. However it may have certain sections such as:
* Description (text, images)
* Acknowledgment
* Image Attribution
* References
* Logos

All reference links and images across all content types are handled in the same way; hence please see [common layout section](bssw_styling_common.html) of the guide.


#### Author Bios
This section has details of the author in a short paragraph. The content is free flowing.

## Metadata section

For blogs, ensure that you specify the *track* metadata. This information from the metadata section, in the source file, is displayed in the deck-area of the blog. In addition, please specify the [common metadata](bssw_content_metadata.html) that is expected in all BSSw.io content.

## Citations/References

Blogs will occasionally benefit from using more formal citations/references (listed at its bottom) instead of in-text hyperlinks.
In these cases, they should use the approach documented in the [common citations/references section](bssw_styling_common.html#citationsreferences).

## Guidelines for Interview-Style blogs
For blogs written in interview style:
* Use **bold** to mark up question and answer markers.
* Where reasonable, consider structuring the piece as if "BSSw" were doing the interview instead of a named individual.
  - This eliminates the need to name a contributor who's identity isn't really relevant.
  - Reduces the number of names for readers to keep track of.
* For questions use **Question:** or **Full Name:** initially, then **Q:** or **Firstname:** following.
* For answers, use **Full Name:** initially, then **Firstname:** following.

Existing examples of interview-style blogs can be found below. 

## Existing Examples

* A skeleton Markdown template for a blog, which one can copy and customize is available at [this location](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/main/Articles/Blog/BlogArticleSkeletonA.md)

* A simple example of the usage of [formal citations/references](#citationsreferences) can be seen in in the file [WhenNotToWriteAutomatedTests.md](https://github.com/betterscientificsoftware/bssw.io/blob/main/Articles/Blog/WhenNotToWriteAutomatedTests.md).

* Interview-style blog can be seen in the file [Working Remotely: The Spack Team](https://bssw.io/blog_posts/working-remotely-the-spack-team).
  
* Example of an blog in which there is an interview component within a larger piece can be seen in the file [Experiences Replacing Master/Slave Terminology in ALE3D and Sierra](https://bssw.io/blog_posts/experiences-replacing-master-slave-terminology-in-ale3d-and-sierra).

* There are several examples available in the [betterscientificsoftware.github.io repository](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io) to use as a starting point.

{% include links.html %}
