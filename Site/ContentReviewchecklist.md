# Checklist for review of content types

Before we can develop review checklists for various types of content, we need to have a clear idea of the types of content we expect to support.  Issue [#361](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/issues/361) attempts to revise the content types and their attributes. These proposed changes are listed in the [content types and their attributes](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/markcmiller86-content-types-doc/Site/ContentTypes.md) document. We will follow this new document for our checklist discussion.

## Common review criteria
Once the document is ready for review, there are some checks that will be common across all the content types. The following is a list of such common review criteria
- [x] Spell checks, grammar, punctuation and syntax
- [x] Hyperlinks and their validity
- [x] Gender nuetrality checking
- [x] Check "Tone" of the article and whether it fits BSSw policies (its assumed that the article was judged appropriate for BSSw and has hence reached this stage)
- [x] Reference checking
- [x] Title format (what is bold?, capitalized?)
- [x] Deck format
- [x] Logos/images formatting
- [x] Image copyright permissions
- [x] Licensing
- [x] Check if professional proof-reading required. If yes, initiate and follow-through the entire proecedure
- [x] Check if it conforms to .md requirements of bssw.io frontend website and not just github
- [x] Category list (what category will the resource fall under?)
- [x] Check is tags are set properly for displaying (these are usually at the bottom of the article)
- [x] Check the document against the preview site


## Content Types Criteria Checklist
Based on the type of content, additonal review criteria may come into picture.

### Event
- [x] Does it conform to event format?  (we havent yet figured out this format)
- [x] TBD


### Curated Content: can be of the following types
We have decided to introduce a table (Example: [Bitbucket](https://bssw.io/items/an-introduction-to-bitbucket/) shows table for a website, [Legacy-code](https://bssw.io/items/working-effectively-with-legacy-code/) shows for a book, [Case studies paper](https://bssw.io/items/software-development-practices-in-academia-a-case-study-comparison/) shows for a paper, [Intro to Licensing](https://bssw.io/items/an-introduction-to-software-licensing/) for tutorials, [WSSSPE](https://bssw.io/items/an-introduction-to-the-wssspe-organization/) for organization) at the start of the curated content document to give consistency and a brief picture of what the curated content contains. The content of the table will be different for each curated content type (do we describe the layout of the table for each curated content in this document?). We havent yet discussed if such a table is needed outside of curated content resources.

- [x] Curated content table formatted correctly? (headings need to be bold)
- [x] TBD

#### Publications
- [x] Does it follow the rules for publications table?
- [x] DOI verified
- [x] Publication year, author list verified?
- [x] Does body text mention why this paper is interesting, for what audience is may be suitable etc? (this should already have been done by reviewers as well - do we need this here??)

#### Tutorials
- [x] Does it follow the rules for tutorials table?
- [x] Links to slide, slide-synced audio, video?
- [x] Check if older versions of the tutorial existed on BSSw and are they candidates for removal? Check traffic statistics before removing older tutorials

#### Web articles
- [x] Does it follow the rules for web articles table?
- [x] TBD

#### Websites or Organization
- [x] Does it follow the rules for organization/website table?
- [x] Organization or website logo?

#### Book
- [x] Does it follow the rules for book table?
- [x] ISBN numbers
- [x] Does body text mention why this book is interesting, for what audience is may be suitable etc.? (this should already have been done by reviewers as well - do we need this here??)

### Original Article: can be of the following types

#### Blogs and original experiences
- [x] Review for senstitive information (this should already have been done by reviewers as well)
- [x] PI approval (if article talks about anything that can be contrued as sensitive information)
- [x] TBD

### How-to and What-is
- [x] Does it follow the format of the how-to and what-is article? (we havent yet figured out this format)
- [x] TBD

----------
### Other checks that need to be done at prior stages
 - [x] Topic is of interest to readers
 - [x] Relevance of the article
 - [x] Judging whether an article idea is appropriate for BSSw - This is done when the topic is in backlog column
 - [x] Judging the actual content of a contribution i.e PR is aceeptable or not - This needs to be done by the reviewers
 - [x] Judging whether content is ready for publication - This "content" needs to be done by the reviewers but the auxillary things can be done following this current document.
 
 ----------
### Style Guide for Content
### Curated Content:
Curated content follow the below style guide. There are several examples available in the repo for you to use as a starting point.

#### Title
1. Conjuctions and Prepositions will be lowercase. Everything else would usually be uppercase
2. Maintain consistency with titles. For ex: "An Introduction to..." for organizations or website
3. As of Jul 2019, the title of the article continues to be the url of the article. Be smart while selecting title and avoid changing it after publishing (in case the article gets bookmarked by readers)


#### Deck
0. No links in the deck
1. Contains one or two sentences about the article which piques user interest.
2. If it is a publication, it can start with "The *title of article* article, published in the *journal name* in *alphabetic month, year*, explores....". For ex: The *Best Practices for Scientific Computing* article, published in the *PLOS Biology journal* in *Jan 2014*, explores..


#### Tables
For specific websites, organizations: 

Resource information | Details 
:--- | :--- 
Name  | Name of website (Ex: Python for HPC)
Website  | Link to website (Ex: [Python For HPC Community Materials](https://betterscientificsoftware.github.io/python-for-hpc/))
Focus | Custom focus area (Ex: Python language and its application in HPC)

For publications: 

Resource information | Details
:--- | :--- 
Title  | Title of paper (Ex: Best Practices for Scientific Computing)
Authors | Author list. See example for format(Ex: Greg Wilson, Ben Waugh and Paul Wilson)
Publication | Mention "Year, Journal name, DOI with link". See example for format (Ex: Year  2014, PLOS Biology Journal, DOI: [10.1371/journal.pbio.1001745](https://doi.org/10.1371/journal.pbio.1001745))

#### Body text
1. Contains one or more paragraph about the resource.
2. Usually when the resource is mentioned verbatim in the body text, it is italicized.

#### Logos
Sometimes, logos may be present at the end. This is especially relevant for organizations, websites etc.

#### Contributor name.
This is usually at the end of the article, with a hyperlink if available. For ex: 
####Contributed by [Foo Foo](http://github.com/Foo "Foo Foo")

  
