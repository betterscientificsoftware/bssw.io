# A Style Guide for BSSw content

<!-- this is manual table of contents. We need a better way to write one. This is a good tool: https://ecotrust-canada.github.io/markdown-toc/) -->
- [A Style Guide for BSSw content](#a-style-guide-for-bssw-content)
  * [Background](#background)
  * [Where to place your content in Github repo?](#where-to-place-your-content-in-github-repo-)
  * [Naming your content in Github repo](#naming-your-content-in-github-repo)
  * [Common Layout of All Resources](#common-layout-of-all-resources)
    + [Content Title](#content-title)
    + [Content Deck](#content-deck)
    + [Content Description:](#content-description-)
    + [Contributor name](#contributor-name)
    + [Metadata](#metadata)
  * [Styling Rules for Individual Content Type](#styling-rules-for-individual-content-type)
    + [Curated Content:](#curated-content-)
      - [Title](#title)
      - [Deck](#deck)
      - [Table](#table)
          + [Book](#book)
          + [Course](#course)
          + [Organization](#organization)
          + [Podcast](#podcast)
          + [Publication](#publication)
          + [Tutorial](#tutorial)
          + [Webinar](#webinar)
          + [Website](#website)
          + [Web article](#web-article)
          + [Notes on tables](#notes-on-tables)
      - [Body text](#body-text)
      - [Logo](#logo)
      - [References](#references)
    + [Original Article](#original-article)
    + [Blog Articles](#blog-articles)
      - [Publication and Announcements](#publication-and-announcements)
      - [Length](#length)
      - [Source Format](#source-format)
        * [Detailed Formatting Tips](#detailed-formatting-tips)
      - [Employer Approval](#employer-approval)
      - [Content](#content)
        * [General](#general)
        * [Links, and References](#links--and-references)
        * [Images](#images)
    + [Events](#events)
  * [Understanding Metadata](#understanding-metadata)
      - [Publish](#publish)
      - [Categories](#categories)
      - [Topics](#topics)
      - [Tags](#tags)
      - [Level](#level)
      - [Prerequisites](#prerequisites)
      - [Aggregate](#aggregate)

## Background

This is a work-in-progress style guide for all content that goes on the BSSw site. 

The [betterscientificsoftware.github.io](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io) repository is for collaborative content development on general topics related to [developer productivity](Site/Categories/Topics/WhatIsProductivity.md) and [software sustainability](Site/Categories/Topics/WhatIsSustainability.md). Please also see information on [How to Contribute](HowToContribute.md).

Please note that the word "Content" and "Resource" may be used interchangeably in this document.

To start with, see details on [What to Contribute](WhatToContribute.md).  Please note that resources/content is of three major types on BSSw: (1) Events, (2) Curated content and (3) Original Article.

## Where to place your content in Github repo?
Please place your new file in one of the following folders on the site, according to the type of content you are creating:

**The below folder need to be clarified - since they do not match our content types. We may need a folder for howto, whatis etc etc**
- Articles
- Articles/Blog
- CuratedContent
- Events

Following are the guidelines below for naming resources/contents and their files.

## Naming your content in Github repo
This section talks about how to name the ".md" file that is put in Github for ANY type of content/resource. Most points have been taken from the original [Styleguide.md](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/StyleGuide.md) file, present in the main betterscientificsoftware.github.io repo.

For naming a content i.e. creating a filename, please follow the following rules: Filename should be same as resource/content name, adding the suffix ".md" to indicate a Markdown file

- For curated content: Follow name of content (e.g., title of book, article, event, site)
- No spaces
- Cap for first letter of each word
- Abbreviations:
  - Apps = Applications
  - Cse = CSE = Computational Science and Engineering
  - Devpt = Development
  - Eng = Engineering
  - Hpc = HPC = High-Performance Computing
  - Perf = Performance
  - Sw = Software
  - etc.
- Example filename: MyNewArticleTopic.md
     
## Common Layout of All Resources
All resources have the following sections, in common:

### Content Title
A Content title should be simple and straighforward. Please read *Styling Rules* for individual types of content (below) to see if there are any specific guidelines for each content type.

### Content Deck
A Content deck is a one or two sentence resource description of limited length and which appears in header area of articles on the frontend bssw.io site. Please read *Styling Rules* for individual types of content (below) to see if there are any specific guidelines for each content type.

### Content Description:
This is the main body, explaining the content from the perspective of the CSE community. There may be image file (e.g., logo, relevant diagram, science image) in the body text, although these are optional (but encouraged when this exists). Please read *Styling Rules* for individual types of content described later in the article.

### Contributor name
This is name of the contributor, usually at the end of the resource text, with a hyperlink (usually to a GitHub profile(s)) if available. For ex: Contributed by [Foo Foo](http://github.com/Foo "Foo Foo")

### Metadata
We include metadata as formatted comments at the end of the file. Metadata helps define rules about publishing an article, tagging them, selecting categories etc. Be sure to include metadata with each entry, as this will be used to organize content, provide filters, and support searches on the BSSw front-end site. Please read the the section on Meta-data to get detailed insight on the different tags and their importance.


## Styling Rules for Individual Content Type
Resources/content are of three major types on BSSw: (1) Events, (2) Curated content and (3) Original Article.

### Curated Content:
Curated content follow the below style guide. There are several examples available in the repo for you to use as a starting point.

#### Title
1. Conjuctions and Prepositions will be lowercase. Everything else would usually be uppercase
2. Maintain consistency with titles. For ex: "An Introduction to..." for organizations or website, if it makes sense
3. As of Jul 2019, the title of the article continues to be the url of the article. Be smart while selecting title and avoid changing it after publishing (in case the article gets bookmarked by readers)

#### Deck
0. No hyperlinks in the deck
1. Contains one or two sentences about the article which piques user interest.
2. If it is a publication, it can start with "The *title of article* article, published in the *journal name* in *alphabetic month, year*, explores....". For ex: The *Best Practices for Scientific Computing* article, published in the *PLOS Biology journal* in *Jan 2014*, explores..
3.  Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized

#### Table
We have decided to introduce a table at the start of the curated content document to give consistency and a brief picture of what the curated content contains. Curated content can be of the following 7 types: book, organization, publication, tutorial, web article, webinar and website. The content of the table will be different for each curated content type and is described below. 
We havent yet discussed if such a table is needed outside of curated content resources.

Tables should follow the below format:
###### Book
Resource information | Details 
:--- | :--- 
Book title | Name of the book with hyperlink from a neutral non-vendor website (format: [book-name](url to book))
Authors | Author names in the following format with hyperlink from a  neutral website, if available (format: [author name in format "firstname lastname" seperated by comma](url to author))
Publication | Year, ISBN numbers (multiple ISBN number may be available such as ISBN-10 and ISBN-13) (format: "year, ISBN numbers seperated by comma")

###### Course
Resource information | Details 
:--- | :--- 
Course title  | Name of the course with hyperlink 
Presenters | Presenter names  (format: author name in format "firstname lastname" seperated by comma) 
Course hosting website | Name of hosting website such as coursera, youtube, udacity [name of hosting website](url)
Web links | Links to slides, slide-synced audio, video, or link to website course (format : [Course link](url), [Slides](url), [Synced audio](url)), [Video](url), [website link](url) etc) 

###### Organization
Resource information | Details 
:--- | :--- 
Organization name | Name of Organization without hyperlink
Website | Link to website (format: [url](url))
Focus | Custom focus area 

###### Podcast
Resource information | Details 
:--- | :--- 
Podcast title  | Name of the tutorial without hyperlink 
Presenters | Author names  (format: author name in format "firstname lastname" seperated by comma) OR  tutorial-hosting website website name (format: [website-name](website-url)]
Web links | Links to podcast (format: [Name-of-podcast Podcast](url)) 

###### Publication
Resource information | Details
:--- | :--- 
Paper title  | Title of paper without hyperlink 
Authors | Author names  (format: author name in format "firstname lastname" seperated by comma)
Publication | Year, Journal name, DOI with link (format: "year, journal name, DOI:[doi-url][doi-url)")

###### Tutorial
Resource information | Details 
:--- | :--- 
Tutorial title  | Name of the tutorial without hyperlink 
Presenters | Author names  (format: author name in format "firstname lastname" seperated by comma) OR  tutorial-hosting website website name (format: [website-name](website-url)]
Web links | Links to slides, slide-synced audio, video, or link to website tutorial (format : [Slides](url), [Synced audio](url)), [Video](url), [website link](url)) 

###### Webinar
Resource information | Details 
:--- | :--- 
Webinar title  | List title without hyperlink 
Presenters | Author names  (format: author name in format "firstname lastname" seperated by comma)
Web links | Links to slides, slide-synced audio, video (format : [Slides](url), [Synced audio](url), [Video](url)) 

###### Website
Resource information | Details 
:--- | :--- 
Resource name | Name of website
Website | Link to website (format : [website name](url))
Focus | Custom focus area

Many times, a curated article may mention many websites (for ex: links to coding-tools). In that case, use the following format:

Resource information | Details 
:--- | :--- 
Resource name | Text that describes the overall websites 
Websites | Link to website (format : [website name](url)) separated by commas
Focus | Custom focus area

###### Web article
Resource information | Details
:--- | :--- 
Article title  | Title of the article with hyperlink (format:  [title of article](url))
Authors | Author names  (format: author name in format "firstname lastname" seperated by comma), with hyperlink if available (format: [author name](url))
Focus | Custom focus area

###### Notes on tables
Many times, a curated article may have a collection of various types of resources. In that case, it may be difficult to create a table at the very start of the article for these different types of entities. So, please create tables as and when needed throughout the article. An example of this is the article [A Collection of Resources for Sustaining Open Source Software](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/CuratedContent/OSSSustainabilityResources.md) in the curated content directory

#### Body text
1. Contains one or more paragraph about the resource.
2. Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized
3. Its good for body text to go into details of why the resource is interesting and to what audience. 
4. This text should not be a copy-paste from a website. Rather, please write this in your own words to avoid legal issues

#### Logo
Sometimes, logos may be present at the end. This is especially relevant for organizations, websites etc.
1. Please upload logo to https://github.com/betterscientificsoftware/images . *Do images have to be a certain format or size*
2. Add following text with url to end of body text "<img src='url' class='logo' />"
3. *Do we need copyright or permissions for logos? Doublecheck*

#### References
What are rules for these?

### Original Article
There is a style guide for blogs in the main bssw directory called "StyleGuideBlog.md". This needs to be reviewed, applicable parts need to be put in this document and refined further

------------------
### Blog Articles

All text under blog articles is taken from the old blog guide. The text needs to be reviewed and corrected.

#### Publication and Announcements
Blog articles appear here: https://bssw.io/blog_posts and also are announced on the [BSSw email digest](https://bssw.io/pages/receive-our-email-digest) (monthly).

#### Length
General guidance is 250-500 words, though this is flexible (some articles have been shorter, some a bit longer). 

#### Source Format
We use [Github-Flavored Markdown](https://guides.github.com/features/mastering-markdown/) for blog article markup.  However we'll work with you at accept other formats.

A skeleton Markdown template for a blog article, which you can copy and customize is available at https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/Articles/Blog/BlogArticleSkeletonA.md

You can provide a pull request for the article in the appropriate directory of the repository: https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/tree/master/Articles/Blog

If you prefer to use another format, you can email the draft to the editor you've been dealing with.

##### Detailed Formatting Tips
 - The formatting to include a hero image is a bit finicky.
   - The `**Hero Image:**` tag must be followed by a blank line
   - The image itself must be in a Markdown list item (that is, it starts with `-`)
 - Positioning of the hero image relative to the contributor and publication date metadata doesn't matter
 - Having a deck and having a hero image in a blog post are mutually exclusive
   - A way to approximate having both is to have the hero image and then put the deck as your first (short) paragraph after the image and italicize it.
 - `#### Publication date:` is case sensitive (`d` in particular)

#### Employer Approval
If your employer requires an internal review and approval process prior to publication, please let us know.

#### Content
##### General

*Need to say something here*

##### Links, and References
We encourage you to point to a modest numder of additional resources that enhance your article.  Too many links tend to distract readers.  In most cases, we would like to have the items you refer to in BSSw.  These would usually be what we call "curated content", which means short items that provide a pointer to an extenral resource with a short description.  You're welcome to prepate those as separate contributions, and we're happy to help.

##### Images
*Need to say something about what kind of images we want to encourage/discourage and point to writeup of how to deal with images in the other repo.*


### Events
Is there an existing style guide for events? I did not find any.


## Understanding Metadata
For all content types, we have the following meta-data that needs to be put, at the bottom of the file.
- **Publish**: Publish on the BSSw front-end site?
- **Categories**: Specify 1 or more categories (primary display via BSSw website)
- **Topics**: Specify 1 or more topics (visible filters via BSSw website)
- **Tags**: Specify additional tags as keywords for searches (optional -- not currently used on front-end website)
- **Level**: Specify level of content
- **Aggregate**: Optional info for aggregating content to define a more complex resource

Each aspect of metadata is described below.

#### Publish
This is used to Publish on the BSSw front-end site.
- Publish: Yes
- Publish: No

Only files designated as 'Publish: Yes' will be published on the front-end BSSw site.  Work that has not been finalized or is not intended for the front-end site should be designated 'Publish: No'. *ISNT THERE A PREVIEW OPTION, AS WELL?*

#### Categories
Categories are primaily display via BSSw website interface.
[BSSw curators may add/revise topics as needed over time.]
- Planning
- Development
- Performance
- Reliability
- Collaboration
- Skills

#### Topics
Topics are visible filters via BSSw website interface.
- All categories and also finer grain topics within categories
  [Topics: 4-7 per category: family of topics that make sense together. BSSw curators may add/revise topics as needed over time.]
- **Planning**
    - Requirements
    - Design
    - Software interoperability
- **Development**
    - Documentation
    - Version control
    - Configuration and builds
    - Deployment
    - Issue tracking
    - Refactoring
    - Software engineering
    - Programming languages and tools
- **Performance**
    - High-performance computing (HPC)
    - Performance at leadership computing facilities (LCFs)
    - Performance portability
- **Reliability**
    - Testing
    - Continuous integration testing
    - Reproducibility
    - Debugging
- **Collaboration**
    - Licensing
    - Strategies for more effective teams
    - Funding sources and programs
    - Projects and organizations
    - Software publishing and citation
    - Discussion and question sites
- **Skills**
    - Personal productivity and sustainability
    - Online learning

#### Tags
Tags are optional additional keywords for searches
*This needs to be described better. Its not clear to me how we are using this*
- We currently do not use them for on front-end website. 

#### Level
We specify level of detail and depth of content.
*This needs to be described better. Its not clear to me how we are using this*
- **Level 0**:  BSSw WhatIs document
- **Level 1**:  BSSw HowTo document (or equivalent level of detail)
- **Level 2**:  More detailed content, beginner or intermediate levels
- **Level 3**:  Advanced content

#### Prerequisites
Used to specify files for any assumed knowledge on the BSSw site (usually Level 0 and Level1 BSSw docs)/
*This needs to be described better. Its not clear to me how we are using this*
- Most prerequisites are specified automatically according to Topics. In this case, use:
   - Prerequisites: default
- Specify additional prerequisites only for information not already covered by Topics.
   - Prerequisites: filename1.md, filename2.md, etc.

#### Aggregate
This is optional info for aggregating content to define a more complex resource.
*This needs to be described better. Its not clear to me how we are using this*
 - Aggregate: none
   - Note an aggregate resource

 - Aggregate: base
   - The "base" designation of an aggregate resource indicates that content and metadata will be included from subresource files, as specified in a bulletted list of subresources.  See the file [CuratedContent/ResourceTemplate.AggregateBase.md](CuratedContent/ResourceTemplate.AggregateBase.md) for an example "base" file that demonstrates how to specify subresources.

- Aggregate: subresource
  - The "subresource" specification indicates that the item will not be displayed as a separate resource on the front-end BSSw site.  We expect this to be the most common usage.  

- Aggregate: stand-alone and subresource
   - The "stand-alone and subresource" specification indicates that the item will be both (1) listed as a separate resource on the front-end site and (2) used as a subresource, as specified by an aggregate "base" resource.


<!---
   Publish: no
---!>
