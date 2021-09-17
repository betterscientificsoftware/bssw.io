# The CII Best Practices Badge Program

<!-- deck text start -->
The Linux Foundation's CII Best Practices Badge Program represents an impressive collection of the open source communitie's knowledge base for creating, maintaining, and sustaining robust, high-quality -- and most importantly secure -- open-source software.
At its core is a BadgeApp website which provides a database of projects that document what best practices they support and provide supporting evidence.
This set of best practices along with the detailed documentation and supporting justification also serves as an incremental learning tool for software engineering practice and as a foundation for incremental software process and quality improvements efforts.
<!-- deck text end --> 

#### Contributed by [Roscoe A. Bartlett](http://github.com/bartlettroscoe "Roscoe A. Bartlett")
#### Publication date: ???, 2021

The Linux Foundation's<sup>[lf]</sup> Open Source Security Foundation (OpenSSF)<sup>[openssf]</sup> (the successor to its Core Infrastructure Initiative (CII)<sup>[cii]</sup>) is an effort to improve the security and quality of open source software.
The CII Best Practices Badge Program<sup>[ciibpbp]</sup> (started under the CII and being continued under the OpenSSF) is an effort to collect, document, advocate, and help apply a comprehensive collection of best practices from the open-source software development community.
The core of this badge program is a "Badge App" site<sup>[ciibpba]</sup> that allows projects to create an entry for their project and then to specify if their project meets each best practice, descriptions for how they met the criteria, URLs to evidence, and justification for how the criteria was met or not met.

The CII Best Practices and the supporting Badge App site provides a number of benefits by providing:

* a set of practices that have specific actionable criteria which require supporting evidence,

* a particularly strong focus on software security which addresses the White House Executive Order 14028 "Improving the Nation's Cybersecurity"<sup>[eo14028]</sup>

* a badge that can be displayed on GitHub, GitLab and other project hosting sites,

* a learning tool for best practices for developers and projects,

* a means for continual improvement for a project as it incrementally adopts more practices and improves its scores in different areas,

* a standard catalog into the parts of the projects and how it handles different types of processes,

* a website template and database implementation that can be forked and customized for more targeted communities,


## Details of the CII Best Practices

The CII Best Practices are broken down in several different ways:

* Three different badge levels (N/A allowed on some MUST practices):
  * Passing: 43 MUST, 10 SHOULD, 14 SUGGESTED
  * Silver: +44 MUST, +10 SHOULD, +1 SUGGESTED
  * Gold: +21 MUST, +2 SHOULD
* Required or optional practices:
  * MUST
  * SHOULD
  * SUGGESTED
* Six different categories in each badge level:
  * Basic
  * Change Control
  * Reporting
  * Quality
  * Security
  * Analysis

As noted above, some of the practices can be opted-out as not applicable "N/A".

The CII Best Practices are listed as a full set<sup>[ciibpa]</sup> and also for each badge level individually.  They are also listed with or without the detailed description/justification and links to more information.  Each best practice is composted of a short statement of the practice (with the word MUST, SHOULD, or SUGGESTED) and short HTML anchor name link name that serves as a link to the practice and as an unambiguous shorthand identifier for that best practice criteria.  Many items also require a short comment field be filled out and a URL to evidence.   For example, the first four best "Basic" practices in the passing level are stated as:

**Basics**<br>
**Basic project website content**</br>

* The project website MUST succinctly describe what the software does (what problem does it solve?). <sup>[[description_good]]</sup>
* The project website MUST provide information on how to: obtain, provide feedback (as bug reports or enhancements), and contribute to the software. <sup>[[interact]]</sup>
* The information on how to contribute MUST explain the contribution process (e.g., are pull requests used?) {Met URL} <sup>[[contribution]]</sup>
* The information on how to contribute SHOULD include the requirements for acceptable contributions (e.g., a reference to any required coding standard). {Met URL} <sup>[[contribution_requirements]]</sup>

The detailed listing of criteria is given in the following table.

<a name="cii_best_practices_stats_table"/>

**Table: CII Best Practice Breakdown**

| Level | Total active | MUST | SHOULD | SUGGESTED | Allow N/A | Met justification required | Require URL | Met justification or URL required | Includes details | New at this level |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: | --: | --: |
| **Passing** | 67 | 43 | 10 | 14 | 27 | 1 | 8 | 9 | 52 | 67 |
| **Silver** | 55 | 44 | 10 | 1 | 40 | 38 | 17 | 54 | 39 | 48 |
| **Gold** | 23 | 21 | 2 | 0 | 9 | 13 | 9 | 22 | 16 | 14 |

Some practices that are listed as SUGGESTED or SHOULD at a lower level are re-listed as MUST at a higher level.  For example, the Silver level lists the "bus factor" practice as SHOULD:

* The project **SHOULD** have a "bus factor" of 2 or more. {Met URL} <sup>[[bus_factor]]</sup>

but at the Gold level, it re-lists it as MUST:

* The project **MUST** have a "bus factor" of 2 or more. {Met URL} <sup>[[bus_factor]]</sup>

(That is why the number of "Total active" practices in the Silver and Gold levels is higher than the number "New at this  level".)

The badge website provides scores for each of the six categories separately in each level and provides the percentage completion for the current badge being sought.

ToDo: Show a screenshot of the different categories.

ToDo: Show an screen shot of the badge that can appear on GitHub README.md file.





ToDo: Describe:

* Provide subsections for each of the bullets above.

* Scores in each level a provided separately for each level (show screen shot).

* Provides a standard catalog into the parts of the projects and how it handles different types of processes.

* Produced a badge that can be displayed on GitHub, GitLab and other project hosting sites that advertises that a project follows accepted community best practices.

* Provides a learning tool for best practices for developers and projects.

* Provides an incremental road map for incremental process and quality improvements for a software project.

* Provides a means for continual improvement for a project as it incrementally adopts more practices and improves its scores in different areas.

* Provides a website template and database implementation that can be forked and customized for more targeted communities.

* White House Executive Order 14028 that requires government and DOE software improve software security may impact CSE software.

* ???


[lf]: https://www.linuxfoundation.org/
[openssf]: https://openssf.org/
[cii]: https://www.coreinfrastructure.org/
[ciibpbp]: https://www.coreinfrastructure.org/programs/best-practices-program/ "CII Best Practices Badge Program"
[ciibpba]: https://bestpractices.coreinfrastructure.org/en/projects "CII Best Practices Badge App"
[ciibpa]: https://bestpractices.coreinfrastructure.org/en/criteria "FLOSS Best Practices Criteria (All Levels)"
[eo14028]: https://www.whitehouse.gov/briefing-room/presidential-actions/2021/05/12/executive-order-on-improving-the-nations-cybersecurity/

[description_good]: https://bestpractices.coreinfrastructure.org/en/criteria/0#0.description_good
[interact]: https://bestpractices.coreinfrastructure.org/en/criteria/0#0.interact
[contribution]: https://bestpractices.coreinfrastructure.org/en/criteria/0#0.contribution
[contribution_requirements]: https://bestpractices.coreinfrastructure.org/en/criteria/0#0.contribution_requirements
[bus_factor]: https://bestpractices.coreinfrastructure.org/en/criteria#1.bus_factor


<!---
 Publish: yes
 Pinned: no
 Topics: revision control, development tools
 RSS update: ???
--->
