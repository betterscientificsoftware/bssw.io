# A Style Guide for BSSw content
This is a work-in-progress style guide for all content that goes on the BSSw site. 

Content is of three major types on BSSw: (1) Events, (2) Curated content and (3) Original Article.

Currently, this style guide only talks about curated content.

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

#### Table
We have decided to introduce a table at the start of the curated content document to give consistency and a brief picture of what the curated content contains. Curated content can be of the following 7 types: book, organization, publication, tutorial, web article, webinar and website. The content of the table will be different for each curated content type and is described below. 
We havent yet discussed if such a table is needed outside of curated content resources.

Tables should follow the below format:
##### Book
Resource information | Details 
:--- | :--- 
Book title | Name of the book with hyperlink from a neutral non-vendor website (format: [book-name](url to book))
Authors | Author names in the following format with hyperlink from a  neutral website, if available (format: [author name in format "firstname lastname" seperated by comma](url to author))
Publication | Year, ISBN numbers (multiple ISBN number may be available such as ISBN-10 and ISBN-13) (format: "year, ISBN numbers seperated by comma")

###### Organization
Resource information | Details 
:--- | :--- 
Organization name | Name of Organization without hyperlink
Website | Link to website (format: [url](url))
Focus | Custom focus area 

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

##### Webinar
Resource information | Details 
:--- | :--- 
Webinar title  | List title without hyperlink 
Presenters | Author names  (format: author name in format "firstname lastname" seperated by comma)
Web links | Links to slides, slide-synced audio, video (format : [Slides](url), [Synced audio](url), [Video](url)) 

##### Website
Resource information | Details 
:--- | :--- 
Resource name | Name of website
Website | Link to website (format : [website name](url))
Focus | Custom focus area

##### Web article
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

#### Logo
Sometimes, logos may be present at the end. This is especially relevant for organizations, websites etc.
1. Please upload logo to https://github.com/betterscientificsoftware/images . *Do images have to be a certain format or size*
2. Add following text with url to end of body text "<img src='url' class='logo' />"
3. *Do we need copyright or permissions for logos? Doublecheck*

#### References
What are rules for these?

#### Contributor name.
This is usually at the end of the article, with a hyperlink if available. For ex: Contributed by [Foo Foo](http://github.com/Foo "Foo Foo")
