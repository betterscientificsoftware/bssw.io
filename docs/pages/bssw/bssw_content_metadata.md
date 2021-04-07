---
title: Understanding Metadata
sidebar: bssw_sidebar
permalink: bssw_content_metadata.html
---

## Introduction

We include metadata as *formatted comments* at the end of the file.  Metadata helps define rules about publishing an article, selecting categories etc. Metadata information is internally parsed by the BSSw.io website and used for operational and functional purposes. This metadata is not visible on the website.  If metadata is missing, the file will not be published/visible on the website. Missing metadata will not cause the website to break. But be sure to include metadata with each entry, as this will be used to organize content, provide filters, and support searches on the BSSw front-end site. 

## Metadata format and examples

Listed here is the format of a typical metadata.

```
<!---
Publish: yes
Pinned: no
Topics: software engineering, testing
RSS update: 2020-12-17
--->
```

Please note above:
* The use of `<!--- --->` surrounding the metadata.
* Each metadata parameter is on a separate line.
* Please follow the rules of use colon and commas as specified above. Letter case does not matter.

The easiest approach to writing metadata is to copy/paste the formatted example and modify it, as needed. Alternatively, copy the metadata from any of the content files ([curated content](https://github.com/betterscientificsoftware/bssw.io/tree/master/CuratedContent), [events](https://github.com/betterscientificsoftware/bssw.io/tree/master/Events) and [articles](https://github.com/betterscientificsoftware/bssw.io/tree/master/Articles)) in the BSSw.io repository, modify and use them in your content file.

## Metadata description

Following is the set of metadata parameters used on the BSSw.io, currently.

### Publish
This is used to decide if the content needs to be published, previewed or not on the BSSw front-end site.
````
publish: preview

publish: yes

publish: no
````

BSSw.io has a stand-alone website for previewing content before publishing. Using 'publish: preview' ensures that content is visible on the preview website and not on the main site.
Only files designated as 'publish: yes' will be published on the front-end BSSw site. 
Work that has not been finalized or is not intended for the front-end site should be designated 'publish: no'. 

### Pinned
This is used to decide if a content needs to show up as "recommended", when a particular category or topic is selected. Recommended articles will show up on the top of the list of articles. Only 1-2 articles are supposed to be listed as "recommended" at a given time in each topic area. Selecting a category will show up all the recommended articles of all the topic areas that comprise that category.
````
pinned: yes

pinned: no
````

### Topics

Topics are visible filters displayed on the BSSw website interface that provide readers with easier navigation and content searching abilities. A family of topics that make sense together are grouped together in a category. There are around 4-7 topics per category. **The BSSw editorial team may add/revise topics as needed over time.**

````
Topics: software engineering, testing
````

The current topics are as follows:

- **Planning** category has the following topics:
    - Software process improvement
    - Software engineering
    - Requirements
    - Design
    - Software interoperability
- **Development** category has the following topics:
    - Documentation
    - Configuration and builds
    - Revision control
    - Release and deployment
    - Issue tracking
    - Programming languages
    - Development tools
    - Refactoring
- **Performance** category has the following topics:
    - High-performance computing (HPC)
    - Performance at leadership computing facilities (LCFs)
    - Performance portability
- **Reliability** category has the following topics:
    - Testing
    - Continuous integration testing
    - Reproducibility
    - Debugging
- **Collaboration** category has the following topics:
    - Projects and organizations
    - Strategies for more effective teams
    - Funding sources and programs
    - Software publishing and citation
    - Licensing
    - Discussion and question sites
    - Conferences and workshops
- **Skills** category has the following topics:
    - Online learning
    - Personal productivity and sustainability
    
### RSS update
This is used to set the date for RSS update in format yyyy-mm-dd.

The BSSw.io site automatically generates an RSS feed. Currently, it is capped at the 10 most recent items (we can change this with help of our frontend partners, should we need to). The rule is to use the newer of the Publication Date (within the article) or the RSS Date (in the article metadata).

Please note that if you edit an article and don't change the Publication Date or the RSS Date, the RSS feed will not change. This what you'd typically want to do for minor updates, corrections, etc.

If you want the article to reappear in the RSS feed, as if it were newly published, set the RSS Date metadata tag to the current date (or an appropriate near-future date).

````
RSS update: 2020-12-17
````

## Deprecated metadata

Listed below are metadata that were created for various feature-related experiments, but **are not in use** currently.

**Tags**

Tags were optional additional keywords for searches. 


**Categories**

Categories were displayed on BSSw.io to provide easier navigation. Each article could belong to one or more categories. Categories have been replaced by the "topic" tag in metadata. 

The categories were defined as follows:
- Planning
- Development
- Performance
- Reliability
- Collaboration
- Skills


**Level**

The *level* metadata was used to specify level of detail and depth of content.
- **Level 0**:  BSSw WhatIs document
- **Level 1**:  BSSw HowTo document (or equivalent level of detail)
- **Level 2**:  More detailed content, beginner or intermediate levels
- **Level 3**:  Advanced content

**Prerequisites**

This option was used to specify files for any assumed knowledge on the BSSw site.
- Most prerequisites are specified automatically according to Topics. In this case, use:
   - Prerequisites: default
- Specify additional prerequisites only for information not already covered by Topics.
   - Prerequisites: filename1.md, filename2.md, etc.

**Aggregate**

This was optional info used for aggregating content to define a more complex resource.
 - Aggregate: none
   - Note an aggregate resource

 - Aggregate: base
   - The "base" designation of an aggregate resource indicates that content and metadata will be included from subresource files, as specified in a bulletted list of subresources.  See the file [CuratedContent/ResourceTemplate.AggregateBase.md](CuratedContent/ResourceTemplate.AggregateBase.md) for an example "base" file that demonstrates how to specify subresources.

- Aggregate: subresource
  - The "subresource" specification indicates that the item will not be displayed as a separate resource on the front-end BSSw site.  We expect this to be the most common usage.  

- Aggregate: stand-alone and subresource
   - The "stand-alone and subresource" specification indicates that the item will be both (1) listed as a separate resource on the front-end site and (2) used as a subresource, as specified by an aggregate "base" resource.


{% include links.html %}
