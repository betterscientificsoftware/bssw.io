**[Table of Contents: Content Style Guide](../ContentStyleGuide.md)**
* [Introduction](../ContentStyleGuide.md)
* [Content Placement](ContentPlacement.md)
* [Content Naming](ContentNaming.md)
* [Common Layout Description (All Resources)](CommonLayout.md) 
* [Styling Rules for Content Type](StylingContentOverview.md)
    + [Original Article](StylingOriginalArticle.md)
    + [Curated Content](StylingCuratedContent.md)
      - [Title declaration](#title-declaration)
      - [Deck definition](#deck-definition)
      - [Table definitions for resource types](#table-definition)
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
      - [Main Body text](#body-text)
      - [Logo declaration](#logo)
      - [Citations for the article](#references)
    + [Events](StylingEvents.md)
* [Understanding Metadata](Metadata.md)


### Styling Rules for Curated Content:

A Curated content is a brief article that highlights other web-based content. The written article should describe why the CSE community might find value in the linked content.

Curated content can be of the following 7 types: (1) book, (2) organization, (3) publication, (4) tutorial, (5) web article, (6) webinar and (7) website. A written curated content article must follow the below style guidelines. There are several examples available in the [betterscientificsoftware.github.io repository](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/tree/master/CuratedContent) to use as a starting point.

The following sections describe the structure and various parts of a curated content article.

#### Title declaration
1. While there are no strict rules for titles; maintaining consistency with titles across articles is good. For ex: "An Introduction to..." for organizations or website, if it makes sense.
2. The title of the article also becomes a portion of the **article URL** (as of Apr 2020); hence changing the title after publishing it is strictly discouraged.
3. Conjuctions and Prepositions, used in the title, should be lowercase. Every other would would be sentence-case.


#### Deck definition
1. No hyperlinks are allowed in the deck.
2. No images are allowed in the deck.
3. The deck contains one or atmost two sentences about the article which piques user interest.
4. Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized.
5. If it is a publication, it can start with "The *title of article* article, published in the *journal name* in *alphabetic month, year*, explores....". For ex: The *Best Practices for Scientific Computing* article, published in the *PLOS Biology journal* in *Jan 2014*, explores etc.
 
#### Table definition
The curated content table is placed at the *start* of the curated content document. The table maintains consistency across all the curated content article and provides the important links highlighted by the article. Curated content can be of the following 7 types: book, organization, publication, tutorial, web article, webinar and website. The content of the table will be different for each curated content type and is described below. 
We havent yet discussed if such a table is needed outside of curated content resources.

Tables should follow the below format:
###### Book
Resource information | Details 
:--- | :--- 
Book title | Name of the book with hyperlink from a neutral non-vendor website. *Format: [name of the book](url for book)*
Authors | Author names in the following format with hyperlink from a  neutral website, if available. *Format: [firstname lastname](url for author1), [firstname lastname](url for author2)*
Publication | Year, ISBN numbers (multiple ISBN number may be available such as ISBN-10 and ISBN-13). *Format: year, ISBN1, ISBN2, ISBN3*)

###### Course
Resource information | Details 
:--- | :--- 
Course title  | Name of the course with hyperlink. *Format: [course name](url)*
Presenters | Presenter names. *Format: [Firstname lastname](url for presenter), [Firstname lastname](url for presenter)*
Course hosting website | Name of hosting website such as coursera, youtube, udacity. *Format: [name of hosting website](url for course website)*
Web links | Links to slides, slide-synced audio, video, or link to website course etc. *Format: [Course link] (url), [Slides] (url), [Synced audio] (url), [Video] (url), [website link] (url)*

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
