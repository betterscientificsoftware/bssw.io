# A Style Guide for BSSw content
This is a work-in-progress style guide for all content that goes on the BSSw site. 

Please note that the word "Content" and "Resource" may be used interchangeably in this document. 

Content is of three major types on BSSw: (1) Events, (2) Curated content and (3) Original Article.

## Creating "Content Name" in Github repo
This section talks about how to name the ".md" file that is put in Github for ANY type of content/resource. Most points have been taken from the original [Styleguide.md](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/StyleGuide.md) file, present in the main betterscientificsoftware.github.io repo.

For naming a content, please follow the below rules.
- Filename:  Same as resource/content name, adding the suffix ".md" to indicate a Markdown file
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
     
## Common Layout of the Resource
All resources have the following sections, in common:

### Content Deck
A Content deck is a one or two sentence resource description of limited length and whichappears in header area of articles on the frontend bssw.io site. Please read *Styling Rules* for individual types of content (below) to see if there are any specific guidelines for each content type.

### Content Description:
This is the main body, explaining the content from the perspective of the CSE community. There may be image file (e.g., logo, relevant diagram, science image) in the body text, although these are optional (but encouraged when this exists). Please read *Styling Rules* for individual types of content described later in the article.

### Contributor name
This is name of the contributor, usually at the end of the resource text, with a hyperlink (usually to a GitHub profile(s)) if available. For ex: Contributed by [Foo Foo](http://github.com/Foo "Foo Foo")

### Metadata
We include metadata as formatted comments at the end of the file. Metadata helps define rules about publishing an article, tagging them, selecting categories etc. Please read the the section on Meta-data to get detailed insight on the different tags and their importance.



## Styling Rules for Individual Content Type
Currently, this style guide only talks about curated content.

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
4. This text should not be a copy-paste from a website. Rather, please write this in your onwards to avoid legal issues

#### Logo
Sometimes, logos may be present at the end. This is especially relevant for organizations, websites etc.
1. Please upload logo to https://github.com/betterscientificsoftware/images . *Do images have to be a certain format or size*
2. Add following text with url to end of body text "<img src='url' class='logo' />"
3. *Do we need copyright or permissions for logos? Doublecheck*

#### References
What are rules for these?


## Understanding Metadata
For all content types, we have the following meta-data that needs to be put, at the bottom of the file.
- **Publish**: Publish on the BSSw front-end site?
- **Categories**: Specify 1 or more categories (primary display via BSSw website)
- **Topics**: Specify 1 or more topics (visible filters via BSSw website)
- **Tags**: Specify additional tags as keywords for searches (optional -- not currently used on front-end website)
- **Level**: Specify level of content
- **Aggregate**: Optional info for aggregating content to define a more complex resource

Each aspect of metadata is described below.

#### Publish: Publish on the BSSw front-end site?
- Publish: Yes
- Publish: No

Only files designated as 'Publish: Yes' will be published on the front-end BSSw site.  Work that has not been finalized or is not intended for the front-end site should be designated 'Publish: No'. *ISNT THERE A PREVIEW OPTION, AS WELL?*

#### Categories: Primary display via BSSw website interface
[BSSw curators may add/revise topics as needed over time.]
- Planning
- Development
- Performance
- Reliability
- Collaboration
- Skills

#### Topics: Visible filters via BSSw website interface
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

#### Tags: Optional additional keywords for searches
*This needs to be described better. Its not clear to me how we are using this*
- We currently do not use them for on front-end website. 

#### Level: Specify level of detail and depth of content
*This needs to be described better. Its not clear to me how we are using this*
- **Level 0**:  BSSw WhatIs document
- **Level 1**:  BSSw HowTo document (or equivalent level of detail)
- **Level 2**:  More detailed content, beginner or intermediate levels
- **Level 3**:  Advanced content

#### Prerequisites: Specify files for any assumed knowledge on the BSSw site (usually Level 0 and Level1 BSSw docs)
*This needs to be described better. Its not clear to me how we are using this*
- Most prerequisites are specified automatically according to Topics. In this case, use:
   - Prerequisites: default
- Specify additional prerequisites only for information not already covered by Topics.
   - Prerequisites: filename1.md, filename2.md, etc.

#### Aggregate: Optional info for aggregating content to define a more complex resource
*This needs to be described better. Its not clear to me how we are using this*
 - Aggregate: none
   - Note an aggregate resource

 - Aggregate: base
   - The "base" designation of an aggregate resource indicates that content and metadata will be included from subresource files, as specified in a bulletted list of subresources.  See the file [CuratedContent/ResourceTemplate.AggregateBase.md](CuratedContent/ResourceTemplate.AggregateBase.md) for an example "base" file that demonstrates how to specify subresources.

- Aggregate: subresource
  - The "subresource" specification indicates that the item will not be displayed as a separate resource on the front-end BSSw site.  We expect this to be the most common usage.  

- Aggregate: stand-alone and subresource
   - The "stand-alone and subresource" specification indicates that the item will be both (1) listed as a separate resource on the front-end site and (2) used as a subresource, as specified by an aggregate "base" resource.

     


