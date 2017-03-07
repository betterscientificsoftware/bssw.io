
# Resource Skeleton: Aggregate: Base

This is a skeleton file to use as a starting point for a new aggregate resource for the Better Scientific Software site.  The comments section of this file includes guidelines on naming conventions and metadata, as provided in the [BSSW Style Guide](StyleGuide.md).

This is a sample "base" file for an aggregate resource.  Provide general introductory text for the topic in this file and then information on various subtopics in separate "section" files. Use the following metadata to describe the aggregate resource components:

This file ("base" for aggregate resource):  
- Aggregate: Base: [NameOfAggregateResourceBaseFile].md

Subtopic resource files:
- Aggregate: Base: [NameOfAggregateResourceBaseFile].md
- Aggregate: Section: [number of section in the aggregate, e.g., 1, 2, 3, ...]

The front-end for the BSSW site will combine the information into an aggregate resource as follows:
 - Aggregate: Base
 - Aggregate: Section 1
 - Aggregate: Section 2
 - Aggregate: Section 3
 - Etc.
 
See also [ResourceSkeleton.Aggregate.SectionX](ResourceSkeleton.Aggregate.SectionX.md).

A skeleton for new resources that can be covered well in a single file, rather than as an aggregate, see instead 
[ResourceSkeleton.Basic](ResourceSkeleton.Basic.md).

For more information on better scientific software, go to the [Better Scientific Software main page](http://betterscientificsoftware.info).

<!--- 
Categories: specify 1 or more categories
Topics: specify 1 or more topics (corresponding to each category)
Tags: specify optional tags
Level: specify level of content 
Prerequisites: specify prerequisites 
Base: none
--->

<!---
Please follow these guidelines for naming resources and files. Be sure to include metadata with each entry, as this will be used to organize content, provide filters, and support searches on the BSSW site.

Resource Name:

    Brief, essential words only, nothing extra
    For curated content: Follow name of content (e.g., title of book, article, event, site)
    Filename: Same as resource name
        No spaces
        Cap for first letter of each word
        Abbreviations:
            Apps = Applications
            Cse = CSE = Computational Science and Engineering
            Eng = Engineering
            Hpc = HPC = High-Performance Computing
            Perf = Performance
            Sw = Software

Resource Description:

    Concise paragraph explaining resource from the perspective of the CSE community
    Use links to WhatIs and HowTo docs when appropriate for background info
    Image file (e.g., logo) - optional (encouraged when this exists)

Contributor:

    Name of contributor, hyperlinked to website

Footer: Add the following at the bottom of each page:

For more information on better scientific software, go to the [Better Scientific Software main page](http://betterscientificsoftware.info).

Metadata: Include metadata as formatted comments at the end of the file

    Categories: Specify 1 or more categories (primary display via BSSW website)
    Topics: Specify 1 or more topics (visible filters via BSSW website)
    Tags: Specify additional tags as keywords for searches (optional)
    Level: Specify level of content
    Prerequisites: Specify any assumed knowledge on the BSSW site (usually Level 0 and Level 1 BSSW docs)
    Aggregate: Optional info for aggregating content to define a more complex resource

Each aspect of metadata is described below.

Categories: [Primary display via BSSW website interface]

[BSSW curators may add/revise topics as needed over time.]

    Planning
    Reliability
    Performance
    Collaboration
    Individual Productivity
    Crosscutting Resources

Topics: [Visible filters via BSS website interface]

    All categories and also finer grain topics within categories [BSSW curators may add/revise topics as needed over time.]
    [Topics: 4-7 per category: family of topics that make sense together]
    Planning
        Improving productivity and sustainability
        Requirements
        Design
        Development
        Refactoring
        Configuration and builds
        Legacy code
        Software engineering
    Reliability
        Testing
        Debugging
        Continuous integration testing
        Reproducibility
    Performance
        Performance portability
        Software interoperability
        Performance at leadership computing facilities (LCFs)
        High-performance computing (HPC)
    Collaboration
        Version control
        Documentation
        Issue tracking
        Licensing
        Strategies for more effective teams
        Coordination with stakeholders
    Individual Productivity
        Personal kanban
        Personal learning plans
    Crosscutting Resources
        Funding sources and programs
        Projects and organizations
        Discussion forums, Q&A sites
        Software publishing and citation
        On-line learning

Tags: [optional additional keywords for searches]

    Add/revise topics as needed (important terms from curated content; aim for comprehensive coverage to facilitate searches)
    ATPESC
    Bitbucket
    Computational Science Stack Exchange
    Conference
    Doxygen
    FORCE11
    Git
    Gitlab
    HPC
    Jenkins
    Minisymposium
    SoftwareX
    Software Carpentry
    Software Sustainability Institute
    Strategy
    Team
    Test-driven development
    Travis CI
    TutorialsPoint
    Udacity
    Workshop
    etc.

Levels: Specify level of detail and depth of content

    Level 0: BSSW WhatIs document
    Level 1: BSSW HowTo document (or equivalent level of detail)
    Level 2: More detailed content, beginner or intermediate levels
    Level 3: Advanced content

Prerequisites: Specify files for any assumed knowledge on the BSSW site (usually Level 0 and Level1 BSSW docs)

    prerequisites: filename1.md, filename2.md, etc.
    
 Aggregate:

    Optional info for aggregating content to define a more complex resource
    Aggregate: Base: filename
    Aggregate: Section 1
    Aggregate: Section 2
    Aggregate: Section 3
    etc.
   
--->
