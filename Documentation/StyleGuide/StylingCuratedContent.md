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

<!---
   Publish: no
---!>
