# Common Layout of All Resources

All BSSw.io resources have the following three sections, in common: 
* Deck
* Main body
* Metadata. 

The following image shows the deck and main body of a resource.

![Common Parts of a BSSw.io resource](https://github.com/betterscientificsoftware/images/blob/master/documentation-common-elements-small.jpg)

Following is a description of the common elements.

## DECK SECTION
The deck is the top shaded portion of the article. The elements of the deck are mostly the same across all the BSSw.io content types but with a few variations. The deck has two parts: (1) deck text/image and (2) deck attributes.

#### Deck Text/Image
Most content types will have  the deck text, which is usually couple of lines highlighting the article. For curated content and events, deck text contains a two-sentence descriptive text about the resource. Some content types may have an image instead of the deck text. In the context of blogs, deck section will usually contain an image.

**General guidelines:**
1. It is good to add the comments  `<!-- deck text start -->` and  `<!-- deck text end -->` around the deck text in the raw file: 
*Example*: `<!-- deck text start --> This is deck text <!-- deck text end -->`
2. No hyperlinks are allowed in the deck.
3. If text is used, then the deck contains one or atmost two sentences about the article which piques user interest.
4. Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized.

#### Deck Attributes
From the perspective of deck attributes, the deck will *always* contain the (1) title of the article, (2) author/contributor/organizer names, (3) publication date, (4) BSSw.io categories and (5) BSSw.io topics that the article falls under. These deck attributes that are independent of content type are called *mandatory deck attributes*. Sometimes, the *styling rules section* for different content types may have some additional guidelines for these *mandatory deck attributes* as well.

*Special deck attributes* are specific to content-type and can be found in the *styling rules section* (present in this guide) for each content type. 

##### Deck Title
A Deck title should be simple and straighforward. Please read *styling rules* for individual types of content in this guide to see if there are any specific guidelines for each content type.
* The title of the article also becomes a portion of the article URL (as of Apr 2020); hence changing the title after publishing it is strictly discouraged.
* Conjuctions and Prepositions, used in the title, should be lowercase. Every other word should be sentence-case.

##### Contributor Name
This is name of the contributor/author/organizer. This contains the full name of the contributor and a URL, usually to the github profile, of the contributor. In the source file, please use the following format: `#### Contributed by [Firstname Lastname](github profile url "Firstname Lastname")`

##### Deck Publication date
The date when the content was published on BSSw.io. In the source file, please use the following format:`#### Publication date: Month DD, YYYY`. 

##### BSSw Categories
The indicates which BSSw.io categories the article belongs to. As of April 2020, BSSw.io has six categories: (1) better planning, (2) better development, (3) better performance, (4) better reliability, (5) better collaboration, and (6) better skills. The most up-to-date categories can be obtained from the BSSw.io website (click Resources link at https://bssw.io/). In the source file, the categories for the article can be indicated in the *metadata section* of the article. 

##### BSSw Topics
The indicates which BSSw.io topic areas the article belongs to. Each of the six categories on BSSw.io has several topic areas.  The most up-to-date topic areas can be obtained from the BSSw.io website (click Resources link at https://bssw.io/  to see the categories; and the topics are listed under each of the categories). In the source file, the topic areas for the article can be indicated in the *metadata section* of the article. 

## MAIN BODY SECTION
The main body is the portion of the article below the deck.  The elements of the main body differ based on content type. 
The main body should explain the content from the perspective of the CSE community. There may be image file (e.g., logo, relevant diagram, science image) in the body text, although these are optional (but encouraged when this exists). Please read *styling rules* for individual types of content described later in this guide.

### Handling images
Images for content are stored in a different repository (and not the main repo). There are several reasons for this decision which this guide will not delve into.  To reference the images in the article, we upload them to a specific bssw.io images directory and then reference them from the article.
1. Please upload logo to https://github.com/betterscientificsoftware/images.
2. Add following text with url to end of body text in the article `< img src='url to image file in the images directory' class='logo' / >`
3. Please ensure we have permission to use the logo 
4. Please ensure logo is clear and high resolution

If this process if not clear, please contact the Editor-in-chief for more information on this. 

### Links and References
Very rarely, but possibly, we may have references/citations at the end of the article. There is a certain process for this. Please contact the Editor-in-chief for more information on this. 

## METADATA SECTION
We include metadata as *formatted comments* at the end of the file.  Metadata helps define rules about publishing an article, tagging them, selecting categories etc. Be sure to include metadata with each entry, as this will be used to organize content, provide filters, and support searches on the BSSw front-end site. Please read the the section on Metadata to get detailed insight on the different tags and their importance.

## UNPUBLISHING CONTENT
Please follow the below rules
1. There needs to be  documentation about why content is being unpublished. On top of the content file, please add
 `Date1: mm-dd-yyyy: Reason for unpublishing`
 `Date2: mm-dd-yyyy: Reason for unpublishing`
2. Add the word UNPUB to file file name. For examplw: `GitversionUNPUB.md`
