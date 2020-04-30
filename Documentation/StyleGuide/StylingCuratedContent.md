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
      - [Resource-specific Table declaration](#resource-table-declaration)
          + [Book](#book)
          + [Course](#course)
          + [Organization](#organization)
          + [Podcast](#podcast)
          + [Publication](#publication)
          + [Tutorial](#tutorial)
          + [Webinar](#webinar)
          + [Website](#website)
          + [Web article](#web-article)
          + [Special tables](#special-tables)
      - [Main Body text](#main-body-text)
      - [Logo declaration](#logo-declaration)
      - [References for the article](#references)
    + [Events](StylingEvents.md)
* [Understanding Metadata](Metadata.md)


### Styling Rules for Curated Content:

A Curated content is a brief article that highlights other web-based content/resources. The written article should describe why the CSE community might find value in the linked content.

A Curated content article can highlight the following 7 types of resources: (1) book, (2) organization, (3) publication, (4) tutorial, (5) web article, (6) webinar and (7) website. A written curated content article must follow the below style guidelines. There are several examples available in the [betterscientificsoftware.github.io repository](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/tree/master/CuratedContent) to use as a starting point.

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
 
#### Resource Table declaration
The resource declaration table is placed at the *start* of the curated content document. The table maintains consistency across all the curated content article and provides the important links highlighted by the article. Resources pointed by the curated content article can be of the following 7 types, as discussed above. The content of the table will be different for each resource and is described below. 

###### Book
Resource information | Details 
:--- | :--- 
Book title | Name of the book with hyperlink from a neutral non-vendor website. *Format: [name of the book](url for book)*
Authors | Author names in the following format with hyperlink from a  neutral website, if available. *Format: [firstname lastname](url for author1), [firstname lastname](url for author2)*
Publication | Year, ISBN numbers (multiple ISBN number may be available such as ISBN-10 and ISBN-13). *Format: year, ISBN1, ISBN2, ISBN3*)

###### Course
Resource information | Details 
:--- | :--- 
Course title  | Name of the course with hyperlink, *Format: [course name] (url)*
Presenters | Presenter names, *Format: [Firstname lastname](url for presenter), [Firstname lastname](url for presenter)*
Course hosting website | Name of hosting website such as coursera, youtube, udacity. *Format: [name of hosting website](url for course website)*
Web links | Links to slides, slide-synced audio, video, or link to website course etc. *Format: [Course link] (url), [Slides] (url), [Synced audio] (url), [Video] (url), [website link] (url)*

###### Organization
Resource information | Details 
:--- | :--- 
Organization name | Name of Organization without hyperlink, *Format: Name of the organization*
Website | Link to website, *Format: [URL to website] (url)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2*

###### Podcast
Resource information | Details 
:--- | :--- 
Podcast title  | Name of the tutorial without hyperlink, *Format: Name of the tutorial*
Presenters | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)* OR  tutorial-hosting website website name, *Format: [website-name] ( website-url)*
Web links | Links to podcast, *Format: [Name-of-podcast Podcast] (url)*

###### Publication
Resource information | Details
:--- | :--- 
Paper title  | Title of paper without hyperlink, *Format: publication title*
Authors | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)* 
Publication | Year, Journal name, DOI with link. *Format: year, journal name, DOI:[url of the DOI] [doi-url)*

###### Tutorial
Resource information | Details 
:--- | :--- 
Tutorial title  | Name of the tutorial without hyperlink, *Format: tutorial title*
Presenters | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)* OR  tutorial-hosting website website name, *Format: [website-name] ( website-url)*
Web links | Links to slides, slide-synced audio, video, or link to website course etc. *Format: [Course link] (url), [Slides] (url), [Synced audio] (url), [Video] (url), [website link] (url)*

###### Webinar
Resource information | Details 
:--- | :--- 
Webinar title  | List title without hyperlink, *Format: webinar title*
Presenters | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)*
Web links | Links to slides, slide-synced audio, video, or link to website course etc. *Format: [Course link] (url), [Slides] (url), [Synced audio] (url), [Video] (url), [website link] (url)*

###### Website
Resource information | Details 
:--- | :--- 
Resource name | Name of website, *Format: website name*
Website | Link to website, *Format : [website url] (url)
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

###### Web article
Resource information | Details
:--- | :--- 
Article title  | Title of the article with hyperlink, *Format:  [title of article] (url)
Authors | Author names, *Format: [Firstname lastname] (url for author), [Firstname lastname] (url for author)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

###### Special tables

###### *Mutliple resources of the same type*

Many times, a curated article may mention many multiple resources of the same type. An example of this is the curated content article, titled *[An Introduction to Documentation tools](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/CuratedContent/DocumentationTools.md)*, located in the curated content directory. In that case, use the following format for the table:

Resource information | Details 
:--- | :--- 
Resource name | Text that describes the overall websites. *Format: Brief 2-3 word text description *
Websites | Link to websites separated by commas, *Format : [website name1] (url1), [website name2] (url2)*
Focus | Custom focus area - this is a 3 word description of the focus area of the article, *Format: focus area1, focus area2.*

###### *Mutliple resources of the assorted type*

Many times, a curated article may have a collection of various types of resources. In that case, it may be difficult to create a table at the very start of the article for these different types of entities. So, please create tables as and when needed throughout the article. An example of this is the curateed content article, titled *[A Collection of Resources for Sustaining Open Source Software](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/master/CuratedContent/OSSSustainabilityResources.md)*, located in the curated content directory

#### Main Body text
1. Contains one or more paragraph about the resource.
2. Whenever resource is mentioned in deck or body text in verbatim, it needs to be italicized
3. Its good for body text to go into details of why the resource is interesting and to what audience. 
4. This text should not be a copy-paste from a website. Rather, please write this in your own words to avoid legal issues

#### Logo declaration
Sometimes, logos may be present at the end. This is especially relevant for organizations, websites etc.
1. Please upload logo to https://github.com/betterscientificsoftware/images . *Do images have to be a certain format or size*
2. Add following text with url to end of body text * < img src='url' class='logo' / > *
3. Please ensure we have permission to use the logo 

#### References for the article
Many times, we may have references/citations at the end of the article. There is a certain process for this. Please contact the Editor-in-chief for more information on this. Details: To be described.


<!---
   Publish: no
---!>
