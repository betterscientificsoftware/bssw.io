Table of Contents
===============================
[Click to Return to HomePage Table of Contents](../README.md)
[Click to Return to Content Style Guide Table of Contents](../ContentStyleGuide.md)

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
