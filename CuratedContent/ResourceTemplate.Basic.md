# Resource Template

This is a template file to use as a starting point for a new resource for the Better Scientific Software site.  The comments section of this file includes guidelines on naming conventions and metadata, as provided in the [BSSw Style Guide](../StyleGuide.md).

While this template is appropriate for most new resources on the site, we also provide templates for aggregate resources, composed of an introduction to a topic and then multiple subresources (topical sections), contributed by potentially different authors.  For this case, see [ResourceTemplate.AggregateBase](ResourceTemplate.AggregateBase.md) and [ResourceTemplate.AggregateSubresource](ResourceTemplate.AggregateSubresource.md).

**To add a new resource using this file as a starting point:**
- View this file in Raw mode.
- Copy all text.
- Select `Create New File`.
- Paste text into your new document, as a starting point.  Then edit as you like.
- Continue following instructions in [How To Contribute](../HowToContribute.md).

To incorporate images, see the guidelines in the [Better Scientific Software images repository](../images/README.md).

<!---
Publish: no
Categories: specify 1 or more categories
Topics: specify 1 or more topics (corresponding to each category)
Tags: bssw-internal
Level: specify level of content
Prerequisites: specify prerequisites
Aggregate: none
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
    Categories: Specify 1 or more categories (primary display via BSSw website)
    Topics: Specify 1 or more topics (visible filters via BSSw website)
    Tags: Specify additional tags as keywords for searches (optional)
    Level: Specify level of content
    Prerequisites: Specify any assumed knowledge on the BSSw site (usually 'defaults')
    Aggregate: Optional info for aggregating content to define a more complex resource

Each aspect of metadata is described below.

Publish: Publish on the BSSw front-end site?
Publish: Yes
Publish: No

Categories: [Primary display via BSSW website interface]

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

--->
