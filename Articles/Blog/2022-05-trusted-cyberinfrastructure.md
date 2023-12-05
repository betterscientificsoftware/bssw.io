# Trusted Cyberinfrastructure Evaluation, Guidance, and Programs for Assurance of Scientific Software

**Hero Image:**

 - [Vera C. Rubin Observatory. Credit: Rubin Obs/NSF/AURA]<img src='../../images/Blog_2205_VRubin.png' />
 

#### Contributed by Elisa Heymann Pignolo, Barton Miller, and [Sean Peisert](https://github.com/peisert)

#### Publication date: May 13, 2022

The mission of [Trusted CI, the NSF Cybersecurity Center of Excellence](https://trustedci.org), is to lead in the development of an NSF Cybersecurity Ecosystem with the workforce, knowledge, processes, and cyberinfrastructure that enables trustworthy science and NSF's vision of a nation that is a global leader in research and innovation.  Trusted CI has a long history in supporting [improvements in assurance of scientific software](https://www.trustedci.org/software-assurance) via secure software training and in-depth vulnerability assessments.

In 2021, Trusted CI embarked on a year-long focused activity to understand the state of assurance in scientific software. The goal of the challenge was to broadly improve the robustness of software used in scientific computing with respect to security. In the first part of 2021, we interviewed six large cyberinfrastructure project teams developing scientific software, and we compiled the findings from those interviews into a [report](https://hdl.handle.net/2022/26799). In the second part 2021, we developed a [guide](https://zenodo.org/record/5777646#.YbjuVL3MKUk) to help scientific software developers begin bridging the secure software gap.  The Trusted CI *[Guide to Securing Scientific Software](https://zenodo.org/record/5777646#.YbjuVL3MKUk)* is intended to be a living document that evolves as the field evolves and expands to cover more topics as time permits.

### Findings

**First, Some Positive Notes**

As you might imagine, our study noticed numerous areas in which scientific software developers faced challenges.  But let's start with the good news — all the projects that we examined used code repositories that include version control, such as GitHub.  In addition, all the projects used bug/issue-tracking software, such as Jira, RT, or, again, GitHub.  Further, most of the projects used modern languages such as Java or Python and generally avoided older languages that are harder to write _safe_ code in, such as C and C++.  Most projects also used dependency-tracking tools, such as the "Dependabot" tool built into GitHub.

**Room for Improvement**

Now for the bad news.  

*Management.*  Most of the projects we looked at lacked any kind of process and policy documentation — that is, documentation for onboarding and offboarding, identification of who is allowed to submit/approve commits, development standards, or design documents.  Indeed, most of the projects lacked documentation of any kind.  Where documentation did exist, it was often out of date and/or, in the case of standards and requirements documentation, was ignored by developers.   Yet such documentation is vital.  Consider the recent issue with a [developer altering open source software to sabotage computers in Russia](https://www.wired.com/story/developer-altered-open-source-software-to-wipe-files-in-russia/), The same such approach could be used against computers in any country.

*Organization and Mission.* Most of the projects that we looked at lacked a point of contact for software security issues, someone who is responsible for managing and coordinating security matters.  This is a key gap, and it is a fundamental tenet (Must 7) of the [Trusted CI Framework](https://www.trustedci.org/framework).  Many of the projects that we spoke with 
were housed in a larger institution that provided supporting IT resources. However, the projects tended to reject support from those institutions that could provide a variety of mechanisms to support software security, often feeling that the additional resources would provide no additional benefit.

*Tools and Testing.* We found the use of manual functional testing was common but automated testing, _security_ testing, or use of software assurance tools was limited.  While dependency-tracking tools tend to be used, there is often misunderstanding about how to use them effectively, a situation that creates challenges for evaluating software supply chain issues and developing a software bill of materials.  With regard to the lack of use of static analysis, we believe the reason is  in part that developers tend to lack the ability to interpret the reporting from these tools.

*Training.*  We observed many obstacles to wide adoption of software security training. Developers did not find training useful, found it difficult to identify training focused on the areas where there they had a specific need, and found training to be too expensive or at least too costly to have developers offline attending several-day training sessions.

*Code Management.*  Many projects were missing a formal review process for repository updates, such as style, functionality, and security checkoffs. And many were mired in "dependency hell" with unconstrained use of third-party libraries and packages and little explicit risk assessment of the use of third-party code.

### Best Practices

After interviewing scientific software developers, our team developed a set of best practices specifically targeted at the needs, resources, and experiences of scientific software developers.

*Governance.* The best practices that we recommended included identifying and appointing a cybersecurity lead (Framework Must 7) who is responsible for securing software design and advises leadership and stakeholders of potential risk.  Moreover, leadership must be involved in cybersecurity decision making (Framework Must 5) and not be surprised about risks.  Organizations must also apply the principle of least privilege to limit access and rights according to the needs and responsibilities of individuals' positions.  We note that documentation — including process and policy documentation, code and development standards, and also design documents — is vital and must be kept up to date.

*Training.*  Software security training is vital for developing secure, robust code.  Such training can be internally created by large universities, but outside trainers 
and tutorials at workshops and conferences such as SC can be good alternatives.  Sometimes even university classes can be good resources.  We note that [free, online software security training from Trusted CI is available](https://research.cs.wisc.edu/mist/SoftwareSecurityCourse/).

*Tools.*  Software analysis tools find flaws in a program and increase the security of software.
A first step is to use dependency analysis tools to detect publicly disclosed vulnerabilities present in a project's dependencies.  A second step is to use static analysis tools starting from day one. These can address huge swaths of vulnerabilities including buffer overruns, cross-site scripting, improper input validation, and hard-coded credentials.  More advanced developers might consider dynamic analysis tools to monitor a program's execution to detect errors such as memory leaks and races.

*Code Storage.* Centralized version control is an essential first step.  Beyond that, separating
testing branches from release versions can avoid bugs and confusion. Separating feature releases from security releases can reduce "update hesitation" by assuring users that security updates won't break their setup.

Ensuring robust and verifiable community communication methods for vulnerabilities is extremely important. These methods  can range from issue tracking in GitHub to mailing lists, social media, and even Common Vulnerabilities and Exposures, captured in the National 
Vulnerability Database.

### Looking Forward

Trusted CI has been supporting improving assurance of scientific software since its inception ten years ago. It plans to continue its efforts in this space by refining and expanding the guide it developed in 2021, continuing to work with the community to seek feedback and contributions on the guide, supporting broad adoption, and continuing its software security teaching and training materials, including online video content, hands-on exercises and text chapters, and in-person tutorials.  

### Acknowledgments

The work described in this post is a product of Trusted CI. Trusted CI is supported by the National Science Foundation under [Grant #1920430](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1920430). For more information about Trusted CI, please visit: [https://trustedci.org/](https://trustedci.org/). Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.

We gratefully acknowledge the rest of the team that contributed to this work, including Andrew Adams, Kay Avila, Mark Krenz, and Jason R. Lee.

In support of this effort, Trusted CI gratefully acknowledges the input from the following software development teams who contributed to this effort:

* FABRIC: Charles Carpenter, Yongwook Song, Michael Stealey, Maruicio Tavarres, Komal Thareja
* The Galaxy Project: Enis Afghan, Dannon Baker, Nate Coraor, Marius van den Beek
* High Performance SSH/SCP (HPN-SSH) by the Pittsburgh Supercomputing Center (PSC):
Chris Rapier
* Open OnDemand by the Ohio Supercomputer Center: Alan Chalker, Eric Franz, Jeff Ohrstrom
* Rolling Deck to Repository (R2R) by Columbia University
* Vera C. Rubin Observatory: Yusra AlSayyad, Frossie Economou, Wil O'Mullane

### Additional Resources

<a href="https://www.trustedci.org/software-assurance" class="link-row">Trusted CI Software Assurance resources</a>
<a href="https://research.cs.wisc.edu/mist/SoftwareSecurityCourse/" class="link-row">Trusted CI Software Assurance On-Line Training</a>
<a href="https://github.com/analysis-tools-dev/static-analysis" class="link-row">Static Analysis tools for different languages</a>
<a href="https://github.com/analysis-tools-dev/dynamic-analysis" class="link-row">Dynamic Analysis tools for different languages</a>

### Author bios

[Elisa Heymann Pignolo](https://www.cs.wisc.edu/staff/heymann-pignolo-elisa/) is a senior scientist on the NSF Cybersecurity Center of Excellence at the University of Wisconsin and an associate professor at the Autonomous University of Barcelona. She was in charge of the Grid/Cloud security group at the UAB and participated in two major Grid European projects: EGI-InSPIRE and European Middleware Initiative. Heymann's research interests include security and resource management for Grid and cloud environments. Her research is supported by the NSF, Spanish government, the European Commission, and NATO. 

[Barton Miller](https://pages.cs.wisc.edu/~bart/) is the Vilas Distinguished Achievement Professor and Amar & Belinder Sohi Professor in computer science at the University of Wisconsin-Madison. Prof. Miller founded the field of fuzz random testing, which is foundational to computer security and software testing. In addition, he founded (with his then-student Prof. Jeffrey Hollingsworth) the field of dynamic binary instrumentation, which is a widely used critical technology for cyberforensics. Prof. Miller advises the Department of Defense on computer security issues though his position at the Institute for Defense Analysis and was on the Los Alamos National Laboratory Computing, Communications and Networking Division Review Committee and the U.S. Secret Service Electronic Crimes Task Force (Chicago Area). He is currently an advisor to the Wisconsin Security Research Council. Prof. Miller is a fellow of the ACM.

[Sean Peisert](https://www.cs.ucdavis.edu/~peisert/) leads applied research and development in computer security at the Berkeley Lab and UC Davis. He is also chief cybersecurity strategist for CENIC; co-lead of Trusted CI, the NSF Cybersecurity Center of Excellence; editor-in-chief of IEEE Security & Privacy; a member of the Distinguished Expert Review Panel for the NSA Annual Best Scientific Cybersecurity Paper Competition; a member of the DARPA Information Science and Technology Study Group; an ACSA Senior Fellow; past chair of the IEEE Technical Committee on Security & Privacy; and a steering committee member and past general chair of the IEEE Symposium on Security and Privacy ("Oakland").

<!---
Publish: yes
Track: deep dive
Pinned: no
Topics: software process improvement, software engineering, projects and organizations, online learning
--->
