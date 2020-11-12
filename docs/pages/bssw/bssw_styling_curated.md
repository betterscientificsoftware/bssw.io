---
title: Curated Content Specific Styling Guidelines
sidebar: bssw_sidebar
permalink: bssw_styling_curated.html
---

## Introduction

A Curated content is a brief article that highlights other web-based content/resources. The written article should describe why the CSE community might find value in the linked content. A Curated content article can highlight the following 7 types of resources: (1) book, (2) organization, (3) publication, (4) tutorial, (5) web article, (6) webinar and (7) website.

The following figure shows different parts of a curated content article.

![Parts of a curated content article](https://github.com/betterscientificsoftware/images/blob/master/documentation-cc-example.jpg)

The main part of the curated article consists of the (1) Deck, (2) Main body of the article and (3) Metadata section. The following sections describe the structure and various parts of a curated content article.

A written curated content article must follow the below style guidelines. There are several examples available in the [betterscientificsoftware.github.io repository](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/tree/master/CuratedContent) to use as a starting point.

## Deck Section
As we know, all BSSw.io resources have decks and the deck has two parts: (1) deck text and (2) deck attributes. Following is guidance for *curated* content type and their decks.

### Deck text
Deck text is usually a couple of lines about the event. Most of these items are decribed in the [common layout section](CommonLayout.md) of the guide. The following guidlines are to be followed for the writing the deck text for *curated* content type.

1. No images are allowed in the deck.
2. If it is a publication, the deck text can start with "The *title of article* article, published in the *journal name* in alphabetic month, year, explores....". For ex: The *Best Practices for Scientific Computing* article, published in the *PLOS Biology journal* in Jan 2014, explores etc.


### Deck Attributes

The deck for curated content contains the title of the article, deck resource text, contributor names, publication date, BSSw.io categories and topics that the article falls under. 

**Mandatory deck attributes** that are part of deck for all BSSw.io content are listed below. Guidance, specific for "curated content" for these common mandatory deck attributes is given below. There are no *special deck attributes* for this content type.

1. **Deck Title**: In addition to guidelines from the [common layout section](CommonLayout.md) of the guide, please also note the following:
    * Maintaining consistency with titles across articles is good. For ex: "An Introduction to..." for organizations or website, if it makes sense.

2. **Contributor name**: In addition to guidelines from the [common layout section](CommonLayout.md) of the guide, please also note the following:
    * Please indicate the *name of the person* who is *writing* this content for inclusion on the BSSw site. In case of unresolved ambiguity, please use "BSSw.io team" as an author with no github url. 
    * *Example*: `#### Contributed by BSSw.io team`

3. **Deck Publication date**, **BSSw Categories**, **BSSw Topics**: There is no specific guidance for these for the event content type. See [common layout section](CommonLayout.md) of the guide.
 

## Main Body

The usual sections of the body text for  curated content has the following parts: (1) Resource table and (2) Description. There may also be (3) Logo and (4) References section.

### General Guidelines
1. Usually curated content do not need headings, but should you need one then the first level headings should start with `###` heading format.
2. Please write the body text in "third person".
3. If you do not plan to update the text in the future, refrain from adding text such as "TBD", "Coming soon". In such cases, please rephrase text to point to links where such information may be updated by the third-parties.
4. Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized
5. Its good for body text to go into details of why the resource is interesting and to what audience. 
6. This text should not be a copy-paste from a website. Rather, please write this in your own words to avoid legal issues


### Resource Table
Following the deck, is the main body of the article. The resource table is placed at the *start* of the main body of the article. The table ensures consistency across all the curated content articles. It highlights the important links in the article. Resources pointed by the curated content article can be of 7 types. The content of the table will be different for each resource type, as described below. 

#### Book

Resource information | Details 
:--- | :--- 
Book title | Name of the book with hyperlink from a neutral non-vendor website, *Format: [name of the book](url for book)*
Authors | Author names in the following format with hyperlink from a  neutral website, if available. *Format: [firstname lastname](url for author1), [firstname lastname](url for author2)*
Publication | Year, ISBN numbers (multiple ISBN number may be available such as ISBN-10 and ISBN-13). *Format: year, ISBN1, ISBN2, ISBN3*)

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * *Complete Code: A Practical Handbook of Software Construction, 2nd Edition*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/CodeComplete2ndEdition.md) | [BSSw.io](https://bssw.io/items/code-complete-a-practical-handbook-of-software-construction)
   * *Working Effectively with Legacy Code*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/WorkingEffectivelyWithLegacyCode.md) | [Bssw.io](https://bssw.io/items/working-effectively-with-legacy-code)    
 ________________________________________________________________________________________________

#### Course

Resource information | Details 
:--- | :--- 
Course title  | Name of the course with hyperlink, *Format: [course name] (url)*
Presenters | Presenter names, *Format: [Firstname lastname](url for presenter), [Firstname lastname](url for presenter)*
Course hosting website | Name of hosting website such as coursera, youtube, udacity. *Format: [name of hosting website](url for course website)*
Web links | Links to slides, slide-synced audio, video, or link to website course etc. *Format: [Course link] (url), [Slides] (url), [Synced audio] (url), [Video] (url), [website link] (url)*

An example includes the following, listed with both GitHub.com and BSSw.io links:
   * *Understanding Software Testing and How to Make Software Fail*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/SwTestingUdacity.md) | [BSSw.io](https://bssw.io/items/understanding-software-testing-and-how-to-make-software-fail)
_______________________________________________________________________________________

#### Organization

Resource information | Details 
:--- | :--- 
Organization name | Name of Organization without hyperlink, *Format: Name of the organization*
Website | Link to website, *Format: [URL to website] (url)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2*

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * *IDEAS Software Productivity Project*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/IDEASSoftwareProductivityProject.md) | [BSSw.io](https://bssw.io/items/ideas-software-productivity-project)
   * *Introducing the FORCE11 Software Citation Implementation Working Group*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/FORCE11SoftwareCitationImplementationWorkingGroup.md) | [BSSw.io](https://bssw.io/items/introducing-the-force11-software-citation-implementation-working-group)
 ________________________________________________________________________________________________

#### Podcast

Resource information | Details 
:--- | :--- 
Podcast title  | Name of the tutorial without hyperlink, *Format: Name of the tutorial*
Presenters | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)* OR  tutorial-hosting website website name, *Format: [website-name] ( website-url)*
Web links | Links to podcast, *Format: [Name-of-podcast Podcast] (url)*

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * *Remote Working in an Agile World*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/RemoteWorkingAgileWorld.md) | [BSSw.io](https://bssw.io/items/remote-working-in-an-agile-world)
   * *What Makes PSIP Suitable for the Exascale Computing Project?*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/PsipPodcast.md) | [BSSw.io](https://bssw.io/items/what-makes-psip-suitable-for-the-exascale-computing-project)
 ________________________________________________________________________________________________

#### Publication

Resource information | Details
:--- | :--- 
Paper title  | Title of paper without hyperlink, *Format: publication title*
Authors | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)* 
Publication | Year, Journal name, DOI with link. *Format: year, journal name, DOI:[url of the DOI] [doi-url)*

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * *A Literature Review on the Use of Software Engineering Practices in Science*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/ClaimsAboutSoftwareEnginScienceReview.md) | [BSSw.io](https://bssw.io/items/a-literature-review-on-the-use-of-software-engineering-practices-in-science)
   * *Surveying Test-Driven Development in Scientific Software*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/TestDrivenDevptInScientificSwASurvey.md) | [BSSw.io](https://bssw.io/items/surveying-test-driven-development-in-scientific-software)
 ________________________________________________________________________________________________

#### Tutorial

Resource information | Details 
:--- | :--- 
Tutorial title  | Name of the tutorial without hyperlink, *Format: tutorial title*
Presenters | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)* OR  tutorial-hosting website website name, *Format: [website-name] ( website-url)*
Web links | Links to slides, slide-synced audio, video, or link to website course etc. *Format: [Course link] (url), [Slides] (url), [Synced audio] (url), [Video] (url), [website link] (url)*

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * *A Tutorial on Distributed Version Control and Continuous Integration Testing Using GitHub*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/DistributedVersionControlAndContinuousIntegrationTesting.md) | [BSSw.io](https://bssw.io/items/a-tutorial-on-distributed-version-control-and-continuous-integration-testing-using-github)
   * *Introducing Container Mythbusters*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/ContainerMythbusters.md) |  [BSSw.io](https://bssw.io/items/introducing-container-mythbusters)
 ________________________________________________________________________________________________

#### Webinar

Resource information | Details 
:--- | :--- 
Webinar title  | List title without hyperlink, *Format: webinar title*
Presenters | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)*
Web links | Links to slides, slide-synced audio, video, or link to website course etc. *Format: [Course link] (url), [Slides] (url), [Synced audio] (url), [Video] (url), [website link] (url)*

 Examples include the following, listed with both GitHub.com and BSSw.io links:
 **COULD NOT FIND ANY EXAMPLES IN CURATED CONTENT**
 ________________________________________________________________________________________________

#### Website

Resource information | Details 
:--- | :--- 
Resource name | Name of website, *Format: website name*
Website | Link to website, *Format : [website url] (url)
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

 Examples include the following, listed with both GitHub.com and BSSw.io links:
   * *An Introduction to Creative Commons*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/CreativeCommons.md) | [BSSw.io](https://bssw.io/items/an-introduction-to-creative-commons)
   * *An Introduction to GitHub*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/GitHub.md) | [BSSw.io](https://bssw.io/items/an-introduction-to-github)
 ________________________________________________________________________________________________

#### Web article

Resource information | Details
:--- | :--- 
Article title  | Title of the article with hyperlink, *Format:  [title of article] (url)*
Authors | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

Examples include the following, listed with both GitHub.com and BSSw.io links:
   * *What Constitutes Constructive Code Critique?*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/ConstructiveCodeCritique.md) | [BSSw.io](https://bssw.io/items/what-constitutes-constructive-code-critique)
   * *Using Personal Kanban for Productivity*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/UsingPersonalKanban.md) | [BSSw.io](https://bssw.io/items/using-personal-kanban-for-productivity)


### Special Tables

#### Multiple resources of the same type

Many times, a curated article may mention multiple resources of the same type. An example of this is the curated content article, titled *[An Introduction to Documentation tools](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/CuratedContent/DocumentationTools.md)*, located in the curated content directory. In that case, use the following format for the table (below example assumes multiple websites in a single curated content article):

Resource information | Details 
:--- | :--- 
Resource name | Text that describes the overall websites. *Format: Brief 2-3 word text description*
Websites | Link to websites separated by commas, *Format : [website name1] (url1), [website name2] (url2)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

Examples include the following, listed with both GitHub and BSSw.io links:
   * *An Introduction to National RSE Organizations*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/NationalRSEOrgs.md) | [BSSw.io](https://bssw.io/items/an-introduction-to-national-rse-organizations)
   * *Where and How to Publish CSE Software?*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/PublishingCseSw.md) | [BSSw.io](https://bssw.io/items/where-and-how-to-publish-cse-software)
 ________________________________________________________________________________________________

#### Multiple resources of the assorted type

Many times, a curated article may have a collection of various types of resources. In that case, it may be difficult to create a table at the very start of the article for these different types of entities. So, please create tables as and when needed throughout the article. 

Examples includes the following, listed with both GitHub and BSSw.io links:
   * *A Collection of Resources for Sustaining Open Source Software*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/OSSSustainabilityResources.md) | [BSSw.io](https://bssw.io/items/a-collection-of-resources-for-sustaining-open-source-software)
   * *Resources for Maximizing Remote Working*: [GitHub](https://github.com/betterscientificsoftware/bssw.io/blob/master/CuratedContent/RemoteWorking.md) | [BSSw.io](https://bssw.io/items/resources-for-maximizing-remote-working)
 ________________________________________________________________________________________________

### Main Body Description

The description is usually two-three paragraphs of text. In the description on the article, usually towards the end, depending on the nature of the curated content, a logo and/or references to the article may be inserted. 

### Logo declaration
Sometimes, curated content article may have logos. Logos are treated as images. All images across all content types are handled in the same way; hence please see [common layout section](CommonLayout.md) of the guide.

### Links and References
All references across all content types are handled in the same way; hence please see [common layout section](CommonLayout.md) of the guide.

## Metadata Section
There is no specific guidance for this for the event content type. See [common layout section](CommonLayout.md) of the guide.


{% include links.html %}
