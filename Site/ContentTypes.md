# Proposed Content Types and Attributes

Before we can develop editorial *workflow* for various types of content, we need to
have a clear idea of the types of content we expect to support. We also need to
identify what criteria we use to determine what a given content type is and/or any
specific requirements it may have.

As of the writing of this document, our understanding of our content types was
described in the
[What to Contribute](https://github.com/betterscientificsoftware/betterscientificsoftware.github.io/blob/91648f8f992639ad8a9f5467e00cf6dc1bec21a7/WhatToContribute.md) document. This document is a revision of those
original ideas based on the discussion in #361.

The content types we support are outlined in the first column of the table below.

| Content Type| Sourcing|Complexity|Originality|Quality Threshold|Time Sensitivity|
|-------------|---------|----------|-----------|-----------------|----------------|
| Event       |  L      | L        | L         | L               | H              |
| Curated     |  L-M    | M        | L-M       | M               | L              |
| Article     |  M-H    | M-H      | H         | M-H             | L              |

## Content Types

### Event

The **Event** content type is used for events or announcements. Examples might
be an upcoming workshop on software susitainability or the announcement of the
Python 2 sunsetting date.

Some of the criteria for **Event** content on BSSw are:

* Likely to impact or inform HPC/CSE software development processes or planning.
* Not likely to be broadly covered in other common HPC/CSE venues.

A key aspect of an **Event** is time sensitivity.

We want the editorial *workflow* for the **Event** content type to be a lightweight
process which we anticipate can be handled by simple issue submission using an
**Event** specific GitHub issue template. In particular, we foresee no need for
handling **Event** submissions with project boards or pull requests.

### Curated

The **Curated** content type is typically a short-ish article to briefly
highlight or describe another resource, developed and published elsewhere,
that is believed to impact or inform HPC/CSE software development processes.
A **Curated** article may also summarize or cull out key points from the
resource(s) it serves to highlight. In this case, the article may be longer
than typical. As an example of the two extremes a **Curated** article may
take, see [CppUnit](../CuratedContent/CppUnit.md) for a really short example
and see
[Working Effectively With Legacy Code](../CuratedContent/WorkingEffectivelyWithLegacyCode.md)
as an example of a longer one.

### Article

If a proposed piece of content is neither of type **Event** or **Curated**, it is
treated as type **Article**. Within the this content type, there may be one or
more sub-types. This includes *blog* articles, *what is* and *how to* articles
as well as *original experience* articles. Such articles may vary significantly
in length, contain images, references, occur in series, etc. 

## Attributes
The remaining columns in the table above identify key attributes of the content
which are likely to impact editorial *workflow* needed to support them along with
guess-timates of *amount* of the attribute (Low, Medium or High) we expect to be
associated with each type of content.

### Sourcing
This is a measure of the level of effort **EB Members** put into soliciting,
encouraging and helping to guide an (invited) author to develop some content,
typically an article. Some content is actively solicited from specific SMEs
whereas other content (we hope) is submitted unsolicited.

### Complexity
*Complexity* has to do with the amount of *effort* needed by **EB Members** or
**EB Assistants** in supporting the development of the content. This includes
review of the content for relevance, tone of evaluative statements, the shear
length/size of the article, etc.

Low complexity content requires only a basic sanity check for review whereas
other content may require a degree of vetting similar to that used for a
conference proceedings.

We expect **Event** type to be of low complexity, **Curated** low-medium and
**Article** medium-high.

### Originality
*Originality* has to do with how new the content is likely to be to an HPC/CSE
audience. An example of something with high originality is the
[tech. refresh blog article](../Articles/Blog/ContinuousTechnologyRefreshment.md).
The concept of technology refreshment itself is not new or original. However, its
characterization within the context of HPC/CSE software development practices is.
The more original a given piece of content is, the more scrutiny it may require
before final publication.

### Quality Threshold
The *quality threshold* of a piece of content is a measure of the effort required
to finaly properly publish the article including whatever special needs it might
have. An example of a higher than normal quality threshold is the article on the
[Apollo Guidance Computer](../Articles/Blog/ApolloGuidanceComputerPart1.md) which
required the development of a style for handling footnote references and a script
to post-process them.

(Or, is this a measure of the effort required to review...in which case how is
this different from *complexity*).

### Time Sensitivity
This is a measure of how critical it is to publish the article by a certain
date. Certainly, **Event** content has high time sensitivity whereas other
types of content probably do not.

We should expect any generalist in SWE for HPC/CSE to provide adequate levels of
vetting for most of the content we publish. The threshold simply should not be all
that high. Only for a subset of articles, the most complex and/or original, should
we expect to review at a deep enough level that we have to worry about whether the
needed expertise is available among **EB Members**.

## Identification and Origanization by Content Type

We have several options for identify and organizing the repository by
content type. These are...

- YAML tagging
- Location in Folder Hierarchy
- File Naming Convention

We should understand the implications of each of these before we settle
on one. At present, we seem to be using mostly the Folder Hierarchy
approach. Different web technologies for actually generating and hosting
the site may benefit from one more than another.
