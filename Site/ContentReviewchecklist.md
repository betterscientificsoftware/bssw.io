# Checklist for review of content types

Before we can develop review checklists for various types of content, we need to have a clear idea of the types of content we expect to support.  Issue [#361](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/issues/361) attempts to revise the content types and their attributes. These proposed changes are listed in the [content types and their attributes](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/markcmiller86-content-types-doc/Site/ContentTypes.md) document. We will follow this new document for our checklist discussion.

## Checks that need to be done at prior stages
Following is a list of checks that need to be done before the article reaches the final review stage:

- [x] Topic is of interest to readers
- [x] Relevance of the article
- [x] Judging whether an article idea is appropriate for BSSw - This is done when the topic is in backlog column
- [x] Judging the actual content of a contribution i.e PR is aceeptable or not - This needs to be done by the reviewers
- [x] Judging whether content is ready for publication - This "content" needs to be done by the reviewers but the auxillary things can be done following this current document.
- [x] Document follows style guide

--------------------------------------------------


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


### Curated Content: 

Curated content can be of the following 7 types: book, organization, publication, tutorial, web article, webinar and website
- [x] Curated content table formatted correctly as per style guide?

#### Book
- [x] TBD

#### Organizations 
- [x] TBD

#### Publications 
- [x] TBD

#### Tutorials
- [x] Check if older versions of the tutorial existed on BSSw and are they candidates for removal? Check traffic statistics before removing older tutorials

#### Web articles
- [x] TBD

#### Webinars
- [x] TBD

#### Websites 
- [x] TBD



### Original Article: can be of the following types

#### Blogs and original experiences
- [x] Review for senstitive information (this should already have been done by reviewers as well)
- [x] PI approval (if article talks about anything that can be contrued as sensitive information)
- [x] TBD

### How-to and What-is
- [x] Does it follow the format of the how-to and what-is article? (we havent yet figured out this format)
- [x] TBD

---------------------------------------
## Style Guide for Content

This is a work-in-progress style guide for all content that goes on the BSSw site.

### Curated Content:
Curated content follow the below style guide. There are several examples available in the repo for you to use as a starting point.

#### Title
1. Conjuctions and Prepositions will be lowercase. Everything else would usually be uppercase
2. Maintain consistency with titles. For ex: "An Introduction to..." for organizations or website
3. As of Jul 2019, the title of the article continues to be the url of the article. Be smart while selecting title and avoid changing it after publishing (in case the article gets bookmarked by readers)


#### Deck
0. No hyperlinks in the deck
1. Contains one or two sentences about the article which piques user interest.
2. If it is a publication, it can start with "The *title of article* article, published in the *journal name* in *alphabetic month, year*, explores....". For ex: The *Best Practices for Scientific Computing* article, published in the *PLOS Biology journal* in *Jan 2014*, explores..
3.  Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized


#### Tables

We have decided to introduce a table at the start of the curated content document to give consistency and a brief picture of what the curated content contains. Curated content can be of the following 7 types: book, organization, publication, tutorial, web article, webinar and website. The content of the table will be different for each curated content type and is described below. 

We havent yet discussed if such a table is needed outside of curated content resources.

Tables should follow the below format:

#### For Books,
Resource information | Details 
:--- | :--- 
Book title | Name of the book with hyperlink from a neutral non-vendor website (format: [book-name](url to book))
Authors | Author names in the following format with hyperlink from a  neutral website, if available (format: [author name in format "firstname lastname" seperated by comma](url to author))
Publication | Year, ISBN numbers (multiple ISBN number may be available such as ISBN-10 and ISBN-13) (format: "year, ISBN numbers seperated by comma")

##### For Organization
Resource information | Details 
:--- | :--- 
Organization name | Name of Organization without hyperlink
Website | Link to website (format: [url](url))
Focus | Custom focus area 

##### For Publications: 
Resource information | Details
:--- | :--- 
Paper title  | Title of paper without hyperlink 
Authors | Author names  (format: author name in format "firstname lastname" seperated by comma)
Publication | Year, Journal name, DOI with link (format: "year, journal name, DOI:[doi-url][doi-url)")

##### For Tutorials,
Resource information | Details 
:--- | :--- 
Tutorial title  | Name of the tutorial without hyperlink 
Presenters | Author names  (format: author name in format "firstname lastname" seperated by comma) OR  tutorial-hosting website website name (format: [website-name](website-url)]
Web links | Links to slides, slide-synced audio, video, or link to website tutorial (format : [Slides](url), [Synced audio](url)), [Video](url), [website link](url)) 

##### For Webinars,
Resource information | Details 
:--- | :--- 
Webinar title  | List title without hyperlink 
Presenters | Author names  (format: author name in format "firstname lastname" seperated by comma)
Web links | Links to slides, slide-synced audio, video (format : [Slides](url), [Synced audio](url)), [Video](url)) 

##### Websites 
Resource information | Details 
:--- | :--- 
Resource name | Name of website
Website | Link to website (format : [website name](url)
Focus | Custom focus area

##### For Web articles:
Resource information | Details
:--- | :--- 
Article title  | Title of the article with hyperlink (format:  [title of article](url))
Authors | Author names  (format: author name in format "firstname lastname" seperated by comma), with hyperlink if available (format: [author name](url))
Focus | Custom focus area

#### Body text
1. Contains one or more paragraph about the resource.
2. Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized
3. Its good for body text to go into details of why the resource is interesting and to what audience. 
4. This text should not be a copy-paste from a website. Rather, please write this in your onwards to avoid legal issues

#### Logos
Sometimes, logos may be present at the end. This is especially relevant for organizations, websites etc.
1. Please upload logo to https://github.com/betterscientificsoftware/images . *Do images have to be a certain format or size*
2. Add following text with url to end of body text <img src='url' class='logo' />
3. *Do we need copyright or permissions for logos? Doublecheck*

#### References
What are rules for these?


#### Contributor name.
This is usually at the end of the article, with a hyperlink if available. For ex: Contributed by [Foo Foo](http://github.com/Foo "Foo Foo")

  
