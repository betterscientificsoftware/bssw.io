# The SciCodes Consortium: Coordinating Research Software Registries and Repositories

<!-- deck start -->
The SciCodes consortium was formed to help discipline- and institutionally-based software registries and repositories share work methods and develop standards.  They welcome involvement from both developers of research software and managers of repositories and registries.
<!-- deck end -->

#### Contributed by: [Hervé Ménager](https://github.com/hmenager), Tom Morrell, and [Alice Allen](https://github.com/asclnet)

#### Publication date: August 26, 2022

*Originally posted on the [Software Sustainability Institute](https://www.software.ac.uk/blog/2022-04-21-scicodes-consortium-coordinating-research-software-registries-and-repositories) blog.*

Scientific disciplines that rely on computational methods often have a resource, a code registry or repository, that serves as a library for the discipline and collects the software itself and/or metadata about the software. [SciCodes](https://scicodes.net/), formed in 2021, is a consortium of academic discipline and institutional software registries and repositories. Among its goals are sharing work methods and creating a virtual registry standard to enable searching across multiple software registries.

### Software in science

If you work in geodynamics, astronomy, or with biostatistics, or with any scientific research software, you are likely familiar with either the [Astrophysics Source Code Library](https://ascl.net/) (ASCL), [Computational Infrastructure for Geodynamics](https://geodynamics.org/) (CIG), [bio.tools](https://bio.tools/), or [Zenodo](https://zenodo.org/). Software registries and repositories such as these, [CaltechDATA](https://data.caltech.edu/), [CoMSES](https://www.comses.net/), [DOECODE](https://www.osti.gov/doecode/), and others improve research by making these codes discoverable, thus providing transparency and reproducibility, and by promoting reuse of software, thus potentially making research more efficient. These services are also active in promoting formal software citation in research articles.

Several years ago, managers and editors of these and other similar resources got together to share and discuss their practices, and to develop [a list of best practices](https://arxiv.org/pdf/2012.13117.pdf) for software registries and repositories. We met virtually for about a year, and then held [a workshop](https://mikehucka.smugmug.com/Work/Software-meetings/SSRCW-2019/i-fvWQt88/A) to refine our ideas. At the conclusion of that project, the group decided to continue to meet and formed the [SciCodes consortium](https://scicodes.net/).

One of the goals of the consortium is to enable the ability to search for code across multiple software registries. Software developed for one discipline may also be useful in another. For example, WND-CHARM<sup>[1]</sup>, written originally for use in biological imaging, has also proven useful in galaxy morphology research. Wouldn’t it be great if there were a way for you to query multiple research software resources to find code that solves a computational problem you have? We think so! And we are working toward a way to do this!

One of the first efforts of the group is to render our own holdings – the metadata in each software library – in the CodeMeta format (codemeta.json). This translates (or “[crosswalks](https://en.wikipedia.org/wiki/Schema_crosswalk)”) the information in each of our resources, which use different schemas, to one standard schema. Having the metadata from these various resources in one standard schema will allow us to build a search tool that can then search all of this metadata, enabling you to find the code that you need, regardless of which discipline it originated in.

The SciCodes consortium also works to improve software citation and findability, strengthen our individual resources by adopting and adapting the best practices we identified, and share advances and information through presentations at our monthly meetings. Because the consortium’s members are spread out over many time zones, the group holds two meetings, seven hours apart, on the same day each month. Meetings include discussions on best practices and [presentations](https://scicodes.net/presentations/) from group members. The consortium is currently led by Hervé Ménager and Tom Morrell, who were elected in late 2021 to overlapping terms to run the group.

### Get involved

Would you like to learn more about our activities? View our [outreach materials](https://scicodes.net/outreach-materials/), including our video above that describes SciCodes and how it may [help one particular field](https://ascl.net/wordpress/2021/10/25/ascl-poster-on-scicodes-consortium-at-adass-xxxi/) which is a good quick introduction to the consortium. We also record the presentations that are given in our meetings; these are [available online](https://scicodes.net/presentations/) and cover topics such as the [Zenodo/InvenioRDM Codemeta Integration](https://ascl.net/assets/scicodes/videos/ZenodoCaltechDATACodemeta_TomMorrell_20210617.mp4), [Research software review as part of the publication process](https://ascl.net/assets/scicodes/videos/CodeReview_AnaTrisovic_20211021.mp4), and how to [Archive and promote open source code with HAL and Software Heritage](https://drive.google.com/file/d/1OnYoGLw1Wq6emDe8GGNoTuaqpSxa7a6S/view?usp=sharing).

Are you writing software for research? If so, please consider submitting it for inclusion in a suitable registry/repository. And! Make your own software more easily cited by listing your preferred citation on your code’s download site, preferably in a standard format such as [codemeta.json](https://codemeta.github.io/) or [CITATION.cff](https://citation-file-format.github.io/).

If your discipline or institution has a software repository or registry that is not [currently represented in SciCodes](https://scicodes.net/participants/), please consider sharing the [best practices for software registries and repositories](https://scicodes.net/best-practices-for-software-registries-and-repositories/) with it, and let us know about the resource by emailing <info@scicodes.net> so we can consider it for membership.

[1-sfer-ezikiw]: https://doi.org/10.1016/j.ascom.2013.09.002 "{Shamir L., Holincheck A., Wallin J., 2013, A&C, 2, 67. doi:10.1016/j.ascom.2013.09.002}"

### Author bios

Hervé Ménager

Tom Morrell

Alice Allen

<!---
Publish: yes
Topics: software publishing and citation
--->
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[Shamir L., Holincheck A., Wallin J., 2013, A&C, 2, 67. doi:10.1016/j.ascom.2013.09.002](https://doi.org/10.1016/j.ascom.2013.09.002)
