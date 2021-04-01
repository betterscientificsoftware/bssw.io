---
title: Curated Content Specific Styling Guidelines
sidebar: bssw_sidebar
permalink: bssw_styling_curated.html
---

## Introduction

All GitHub file names for BSSw.io articles should follow the naming conventions laid out [here](https://betterscientificsoftware.github.io/bssw.io/bssw_file_naming.html).

A Curated content is a brief article that highlights other web-based
content/resources. The written article should describe why the CSE
community might find value in the linked content. A curated content
article can highlight several types of resources, including the following: book, organization, publication, tutorial, web article, webinar and website.

The following figure shows different parts of a curated content article.

- <img src='https://github.com/betterscientificsoftware/images/raw/master/documentation-cc-example.jpg'/>

The main part of the curated article consists of the (1) Deck, (2)
Main body of the article and (3) Metadata section. The following
sections describe the structure and various parts of a curated
content article. There are several examples available in the
[betterscientificsoftware.github.io
repository](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/tree/master/CuratedContent)
to use as a starting point.

## Deck section
All BSSw.io resources have decks and the deck has two
parts: (1) deck text and (2) deck attributes. 

### Deck text
Deck text is usually a couple of lines about the content. Follow the guidance in the [common styling section](bssw_styling_common.html). No images are allowed in the deck section of curated content.
   * **Example:** If it is a publication, the deck text can start with "The *title of article* article, published in the *journal name* in alphabetic month, year, explores....". For ex: The *Best Practices for Scientific Computing* article, published in the *PLOS Biology journal* in Jan 2014, explores etc. | 

### Deck attributes

The deck for curated content contains the title of the article,
deck text, contributor names, and BSSw.io topics that the article falls under. These are all
mandatory deck attributes and apply to all content on BSSw.io. 

* **Deck title**: Refer to [common styling section](bssw_styling_common.html)
of the guide. Please note  that maintaining consistency with titles
across articles is good. For ex: Start title with "An Introduction to..." for
organizations or website, if it makes sense.

* **Contributor name**: Refer to [common styling section](bssw_styling_common.html)
of the guide. Please note that contributor name is the *name of the
person* who is *writing* (and not just submitting the idea of) this
content for inclusion on the BSSw site. In case of unresolved
ambiguity, please use "BSSw.io team" as an author with no github
url (Example*: `#### Contributed by BSSw.io team`).

* **BSSw Topics**: Refer to [common styling section](bssw_styling_common.html) of the guide.

In addition to above, there exists a curated content-specific deck attribute called **Deck publication date**.
* **Deck Publication date**
The date when the content was published on BSSw.io. In the source file, please use the following format:
````
#### Publication date: Month DD, YYYY
````

## Main body

The usual sections of the body text for  curated content has the following parts: (1) resource table and (2) description. There may also be (3) logo and (4) references section.

### Resource table

Following the deck, is the main body of the article. The resource
table is placed at the *start* of the main body of the article. The
table ensures consistency across all the curated content articles.
It highlights the important links in the article. Resources pointed
by the curated content article can be of several types. The content of
the table will be different for each resource type, as described
below

#### Markdown Code
Here is the raw markdown for the resource table
````
Resource information | Details
:--- | :--- 
Foobar | Foobar
Foobar | Foobar
Foobar | Foobar
````

#### Book/Publication

Resource information | Details 
:--- | :--- 
Book/Paper title | If book, then name of the book with hyperlink from a neutral non-vendor website, *Format: [name of the book] 	(url for book)* <br /> OR <br /> If paper, then title of paper without hyperlink, *Format: publication title*
Authors | Author names in the following format with hyperlink from a  neutral website, if available. *Format: [firstname lastname](url for author1), [firstname lastname](url for author2)*
Publication | If book, then: Year, ISBN numbers (multiple ISBN number may be available such as ISBN-10 and ISBN-13). *Format: year, ISBN1, ISBN2, ISBN3* <br /> OR <br /> If paper, then : Year, Journal name, DOI with link. *Format: year, journal name, DOI:[url of the DOI] [doi-url)*

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * Book: *Complete Code: A Practical Handbook of Software Construction, 2nd Edition*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/CodeComplete2ndEdition.md) | [BSSw.io](https://bssw.io/items/code-complete-a-practical-handbook-of-software-construction)
   * Publication: *A Literature Review on the Use of Software Engineering Practices in Science*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/ClaimsAboutSoftwareEnginScienceReview.md) | [BSSw.io](https://bssw.io/items/a-literature-review-on-the-use-of-software-engineering-practices-in-science)

#### Tutorial/Webinar/Podcast/Courses

Resource information | Details 
:--- | :--- 
Tutorial/Webinar/Podcast/Course Title  | Title of the content without hyperlink, *Format: title*
Presenters | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)* OR <br /> content-hosting website name, *Format: [website-name] ( website-url)*
Web links | Links to slides, slide-synced audio, video, or link to tutorial/webinar. *Format: [Course link] (url), [Slides] (url), [Synced audio] (url), [Video] (url), [website link] (url)* OR  <br /> If single link: *Format: [Name-of-podcast Podcast] (url)*

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * Tutorial: *Introducing Container Mythbusters*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/ContainerMythbusters.md) |  [BSSw.io](https://bssw.io/items/introducing-container-mythbusters)
   * Webinar: *Developing, Configuring, Building, and Deploying HPC Software*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/DevelopingConfiguringBuildingAndDeployingHpcSwUNPUB.md) | 
   * Podcast: *What Makes PSIP Suitable for the Exascale Computing Project?*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/PsipPodcast.md) | [BSSw.io](https://bssw.io/items/what-makes-psip-suitable-for-the-exascale-computing-project)
   * Courses: *Understanding Software Testing and How to Make Software Fail*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/SwTestingUdacity.md) | [BSSw.io](https://bssw.io/items/understanding-software-testing-and-how-to-make-software-fail)


#### Website/Organization

Resource information | Details 
:--- | :--- 
Resource name OR Organization name | Name of website/organization without hyperlink, *Format: website name*
Website | Link to website, *Format : [website url] (url)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

 Examples include the following, listed with both GitHub.com and BSSw.io links:
   * Website: *An Introduction to Creative Commons*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/CreativeCommons.md) | [BSSw.io](https://bssw.io/items/an-introduction-to-creative-commons)
   * Organization: *IDEAS Software Productivity Project*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/IDEASSoftwareProductivityProject.md) | [BSSw.io](https://bssw.io/items/ideas-software-productivity-project)

#### Web article

Resource information | Details
:--- | :--- 
Article title  | Title of the article with hyperlink, *Format:  [title of article] (url)*
Authors | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * *What Constitutes Constructive Code Critique?*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/ConstructiveCodeCritique.md) | [BSSw.io](https://bssw.io/items/what-constitutes-constructive-code-critique)
   * *Using Personal Kanban for Productivity*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/UsingPersonalKanban.md) | [BSSw.io](https://bssw.io/items/using-personal-kanban-for-productivity)


#### Tables with multiple resources

##### Multiple resources of the same type

Many times, a curated article may mention multiple resources of the same type. In such cases, please use the following table format.

Resource information | Details 
:--- | :--- 
Resource name | Text that describes the overall websites. *Format: Brief 2-3 word text description*
Websites | Link to websites separated by commas, *Format : [website name1] (url1), [website name2] (url2)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

Examples include the following, listed with both GitHub and BSSw.io links:
   * *An Introduction to Documentation Tools*: [Github](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/DocumentationTools.md) | [BSSw.io](https://bssw.io/items/an-introduction-to-documentation-tools)
   * *An Introduction to National RSE Organizations*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/NationalRSEOrgs.md) | [BSSw.io](https://bssw.io/items/an-introduction-to-national-rse-organizations)
   * *Where and How to Publish CSE Software?*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/PublishingCseSw.md) | [BSSw.io](https://bssw.io/items/where-and-how-to-publish-cse-software)

##### Multiple resources of the assorted type

Many times, a curated article may have a collection of various types of resources. In that case, it may be difficult to create a table at the very start of the article for these different types of entities. So, please create tables as and when needed throughout the article. 

Examples includes the following, listed with both GitHub and BSSw.io links:
   * *A Collection of Resources for Sustaining Open Source Software*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/OSSSustainabilityResources.md) | [BSSw.io](https://bssw.io/items/a-collection-of-resources-for-sustaining-open-source-software)
   * *Resources for Maximizing Remote Working*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/RemoteWorking.md) | [BSSw.io](https://bssw.io/items/resources-for-maximizing-remote-working)

### Main body description

The description is usually two-three paragraphs of text. In the
description on the article, usually towards the end, depending on
the nature of the curated content, a logo and/or references to the
article may be inserted.

Following are general guidelines when writing the main body description.
1. Usually curated content do not need headings, but should you need one then the first level headings should start with `###` heading format.
2. Please write the body text in "third person".
3. If you do not plan to update the text in the future, refrain from adding text such as "TBD", "Coming soon". In such cases, please rephrase text to point to links where such information may be updated by the third-parties.
4. Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized
5. Its good for body text to go into details of why the resource is interesting and to what audience. 
6. This text should not be a copy-paste from a website. Rather, please write this in your own words to avoid legal issues

### Logo declaration
Logos are treated as images. All images across all content types are handled in the same way; hence please see [common styling section](bssw_styling_common.html) of the guide.

### Links and References
This section will be added in the future, as the need arises.

## Metadata section
See the [common metadata section](bssw_content_metadata.html) of the guide.

## Citations/References

Curated content articles should **almost never** need to use more formal citations/references documented in the [common citations/references section](bssw_styling_common.html#citationsreferences).

{% include links.html %}
