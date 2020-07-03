
Table of Contents
===============================
[Click to Return to HomePage Table of Contents](../../README.md)

[Click to Return to Content Style Guide main page](ContentStyleGuide.md)

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
1. It is good to add the comments  `<!-- deck start -->` and  `<!-- deck end -->` around the deck text in the raw file: 
*Example*: `<!-- deck start --> This is deck text <!-- deck end -->`
2. No hyperlinks are allowed in the deck.
3. If text is used, then the deck contains one or atmost two sentences about the article which piques user interest.
4. Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized.

#### Deck Attributes
From the perspective of deck attributes, the deck will *always* contain the title of the article, author/contributor/organizer names, publication date, BSSw.io categories and topics that the article falls under. These deck attributes that are independent of content type are called *mandatory deck attributes*. And then there are deck attributes that are specific to a particular content-type. For such *content-type specific deck attributes*, please read the *styling rules section* (present in this guide) for that particular content type. Sometimes, the *styling rules section* for different content types may have some additional guidelines for the *mandatory deck attributes* as well.

##### Deck Title
A Deck title should be simple and straighforward. Please read *styling rules* for individual types of content in this guide to see if there are any specific guidelines for each content type.

##### Deck Publication date
The date when the content was published on BSSw.io. In the source file, please use the following format:`#### Publication date: Month DD, YYYY`. 

##### Contributor Name
This is name of the contributor/author/organizer. This contains the full name of the contributor and a URL, usually to the github profile, of the contributor. In the source file, please use the following format: `#### Contributed by [Firstname Lastname](github profile url "Firstname Lastname")`

##### BSSw Categories
The indicates which BSSw.io categories the article belongs to. As of April 2020, BSSw.io has six categories: (1) better planning, (2) better development, (3) better performance, (4) better reliability, (5) better collaboration, and (6) better skills. The most up-to-date categories can be obtained from the BSSw.io website (click Resources link at https://bssw.io/). In the source file, the categories for the article can be indicated in the *metadata section* of the article. 

##### BSSw Topics
The indicates which BSSw.io topic areas the article belongs to. Each of the six categories on BSSw.io has several topic areas.  The most up-to-date topic areas can be obtained from the BSSw.io website (click Resources link at https://bssw.io/  to see the categories; and the topics are listed under each of the categories). In the source file, the topic areas for the article can be indicated in the *metadata section* of the article. 

## MAIN BODY SECTION
The main body is the portion of the article below the deck.  The elements of the main body differ based on content type. 
The main body should explain the content from the perspective of the CSE community. There may be image file (e.g., logo, relevant diagram, science image) in the body text, although these are optional (but encouraged when this exists). Please read *styling rules* for individual types of content described later in this guide.

## METADATA SECTION
We include metadata as *formatted comments* at the end of the file.  Metadata helps define rules about publishing an article, tagging them, selecting categories etc. Be sure to include metadata with each entry, as this will be used to organize content, provide filters, and support searches on the BSSw front-end site. Please read the the section on Metadata to get detailed insight on the different tags and their importance.
