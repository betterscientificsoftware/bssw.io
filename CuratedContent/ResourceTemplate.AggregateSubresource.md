# Resource Template: Aggregate Subresource

This is a template "subresource" file to use as a starting point for a new subresource for the Better Scientific Software site.  The comments section of this file includes guidelines on naming conventions and metadata, as provided in the [BSSw Style Guide](../StyleGuide.md).

Provide introductory text for the topic in a separate "base" file and then information on various subtopics in separate "subresource" files (possibly contributed by different authors).  In the "base" file, use the following format to specify subresources, listed in the order to be shown on front-end BSSw site:

Subresources:
- [Name of Subresource1](CuratedContent/SubresourceFile1.md)
- [Name of Subresource2](CuratedContent/SubresourceFile2.md)
- etc.

The front-end for the BSSw site will then combine the information into an aggregate resource.  Used the following metadata to describe the aggregate resource components:

Aggregate resource "base" file:  
- Aggregate: base
   - The "base" designation indicates that content and metadata will be included from subresource files, as specified in the bulleted list of subresources.

Subtopic resource files:
- Aggregate: subresource
  - The "subresource" specification indicates that the item will not be displayed as a separate resource on the front-end BSSW site.  We expect this to be the most common usage.  

- Aggregate: stand-alone and subresource
   - The "stand-alone and subresource" specification indicates that the item will be both (1) listed as a separate resource on the front-end site and (2) used as a subresource, as specified by an aggregate "base" resource.

**To add a new resource using this file as a starting point:**
- View this file in Raw mode.
- Copy all text.
- Select `Create New File`.
- Paste text into your new document, as a starting point. Then edit as you like.
- Continue following instructions in [How To Contribute](../HowToContribute.md).

To incorporate images, see the guidelines in the [Better Scientific Software images repository](../images/README.md).

See also [ResourceTemplate.AggregateBase](ResourceTemplate.AggregateBase.md).

A template for a new resource that can be handled effectively in a single file, rather than as an aggregate, is:
[ResourceTemplate.Basic](ResourceTemplate.Basic.md).

<!---
Publish: no
Categories: specify 1 or more categories
Topics: specify 1 or more topics (corresponding to each category)
Tags: bssw-internal
Level: specify level of content
Prerequisites: specify prerequisites
Aggregate: subresource
--->

<!---
Please follow these guidelines for naming resources and files. Be sure to include metadata with each entry, as this will be used to organize content, provide filters, and support searches on the BSSW site.

Resource Name:
    Brief, essential words only, nothing extra
    For curated content: Follow name of content (e.g., title of book, article, event, site)
    Filename: Same as resource name, adding the suffix ".md" to indicate a Markdown file
        No spaces
        Cap for first letter of each word
        Abbreviations:
            Apps = Applications
            Cse = CSE = Computational Science and Engineering
            Devpt = Development
            Eng = Engineering
            Hpc = HPC = High-Performance Computing
            Perf = Performance
            Sw = Software
            etc.
        Example filename: MyNewArticleTopic.md
            
Resource Deck:
    One-sentence resource description (limited length, appears in header area of frontend)
    
Resource Description:
    Concise paragraph explaining resource from the perspective of the CSE community
    Image file (e.g., logo) - optional (encouraged when this exists)

Contributor:
    Name(s) of contributor(s), hyperlinked to GitHub profile(s)

Metadata: Include metadata as formatted comments at the end of the file
    Publish: Publish on the BSSw front-end site?
    Categories: Specify 1 or more categories (primary display via BSSW website)
    Topics: Specify 1 or more topics (visible filters via BSSw website)
    Tags: Specify additional tags as keywords for searches (optional)
    Level: Specify level of content
    Prerequisites: Specify any assumed knowledge on the BSSw site (usually Level 0 and Level 1 BSSw docs)
    Aggregate: Optional info for aggregating content to define a more complex resource

Each aspect of metadata is described below.

Publish: Publish on the BSSw front-end site?
Publish: Yes
Publish: No

Categories: [Primary display via BSSw website interface]

[BSSw curators may add/revise categories as needed over time.]

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
     - Software engineering
     - Requirements
     - Design
     - Software interoperability
 - **Development**
     - Documentation
     - Configuration and builds
     - Revision control
     - Release and deployment
     - Issue tracking
     - Programming languages
     - Development tools
     - Refactoring
 - **Performance**
     - High-performance computing (HPC)
     - Performance at leadership computing facilities
     - Performance portability
 - **Reliability**
     - Testing
     - Continuous integration testing
     - Reproducibility
     - Debugging
 - **Collaboration**
     - Projects and organizations
     - Strategies for more effective teams
     - Funding sources and programs
     - Software publishing and citation
     - Licensing
     - Discussion and question sites
     - Conferences and workshops
 - **Skills**
     - Personal productivity and sustainability
     - Online learning

Tags: [optional additional keywords for searches]

 [under revision -- not currently used]

Levels: Specify level of detail and depth of content

    Level 0: BSSw WhatIs document
    Level 1: BSSw HowTo document (or equivalent level of detail)
    Level 2: More detailed content, beginner or intermediate levels
    Level 3: Advanced content

Prerequisites: Specify files for any assumed knowledge on the BSSW site (usually Level 0 and Level1 BSSw docs)

    - Most prerequisites are specified automatically according to Topics. In this case, use:
       - Prerequisites: default
    - Specify additional prerequisites only for information not already covered by Topics.
       - Prerequisites: filename1.md, filename2.md, etc.

Aggregate:

    Optional info for aggregating content to define a more complex resource
    Aggregate: base (to specify the base of an aggregate resources)
       - The "base" designation indicates that content and metadata will be included from specified subresource files.  See the file [ResourceTemplate.AggregateBase.md](ResourceTemplate.AggregateBase.md) for an example "base" file.

    Aggregate: subresource (to specify a subresource for an aggregate resource)

     - The "subresource" specification indicates that the item will not be displayed as a separate resource on the front-end BSSW site.  We expect this to be the most common usage.  However, omitting this subresource designation will enable the item to be both (1) listed as a separate resource on the front-end site and (2) used as a subresource in the aggregate.

--->
