# A Community of Practice around Peer Review for Long-Term Research Software Sustainability

**Hero Image:**

 - <img src='../../images/Blog_0820_Peer_review.png' />

#### Contributed by [Karthik Ram](https://github.com/karthik "Karthik Ram GitHub Profile"), [Carl Boettiger](https://github.com/cboettig "Carl Boettiger GitHub Profile"), [Scott Chamberlain](https://github.com/sckott "Scott Chamberlain GitHub Profile"), [Noam Ross](https://github.com/noamross "Noam Ross GitHub Profile"), [Maëlle Salmon](https://github.com/maelle "Maëlle Salmon GitHub Profile"), and [Stefanie Butland](https://github.com/stefaniebutland "Stefanie Butland GitHub Profile")

#### Publication date: August 28, 2020

### Creating a system to review research software

Software, particularly research software, impacts all parts of the modern scientific enterprise, especially the central, vital activity of data analysis and statistical inference.  One would be hard pressed to name areas of contemporary research that are not reliant on research software. These include hundreds of open-source libraries and software packages, many of which are developed by researchers themselves.  Research software is so essential that a large majority of researchers in the UK and United States say that they would no longer be able to continue their work if research software tools stopped working (Jiménez et al. 2017).  Despite the growing importance of research software, much of it is cobbled together with little regard for high standards that are characteristic of other research activities. As a result, the research software ecosystem is fragile and the source of numerous problems that afflict modern computational science (Carver et al. 2018). 

rOpenSci was founded in 2011 in part to address some of the challenges with making research software more sustainable. Our mission is to create technical infrastructure in the form of carefully vetted, staff- and community-contributed R software tools that lower barriers to working with scientific data sources on the web. Our tools support key parts of the data life cycle, from lowering barriers to access, to validation and permanent archiving.  Over  the past decade we have grown into a widely recognized effort that supports an ecosystem of hundreds of high-quality software packages to support the scientiﬁc community. Our software is maintained not just by our expert developers but also through numerous contributions from our thriving community.

Perhaps rOpenSci’s biggest contribution to improving the state of research software is not just developing and maintaining critical software tools in-house but mentoring domain scientists about good software development practices and fostering a peer review culture for research software. In 2015 we began accepting software contributions from domain researchers. Each submission is evaluated against a checklist of best practices and reviewed by two independent developers. The criteria and guidelines have grown over the years to become rOpenSci’s software review system.   In this blog post we briefly describe our efforts to improve the state of research software by creating a peer review system that shares many similarities with the publishing system but also addresses challenges that are unique to software development in research.

### Challenges with research software

**Documentation:** Sorting through large collections of software packages and finding the right tools present a serious challenge for most researchers. Beyond the software functionality itself, one of the biggest hurdles to using software is lack of good documentation. Given the tedious nature of the process and the need for  skills different from programming, most packages are documentation-poor (Geiger et al, 2018)

**Testing**: Software plays an  important role in research and is used for critical reasons such as formulating policy, supporting drug discovery, and mitigating the effects of climate change. Mistakes in implementation can have catastrophic consequences (Hatton, 1997). Yet scientific software often lacks tests, and some surveys show that only  ~66% of research software contains unit tests (Kanewala, 2014).

**Lack of community:** Nearly two-thirds of the open-source projects on GitHub have only 1--2 maintainers, a very low number that increases the likelihood that projects will go stale (Eghbal, 2016). Most scientific software is developed by scientists who rarely possess software engineering skills. The most successful projects are the ones that turn one-person projects into thriving communities.

**Long-term archiving:** Although software collaboration platforms such as GitHub bring visibility to projects, they are not a solution for long-term archiving. Nearly 30% of the software mentioned in papers surveyed by Collberg (2014) could not be located. Without permanent archiving of source code in persistent repositories such as Zenodo, one cannot ensure availability of software over time.

**Software design and code smells:**  Poorly designed software with inconsistent and unintuitive user interfaces is a problem that cannot be easily surfaced without a detailed review. Deeper design issues include attention to software dependencies, good error messages and handling of unexpected inputs, and following conventions and coding styles that are characteristic of a community.  

**Maintainability**:  Design considerations that make it easy for future developers to understand the software, extend functionality, and fix bugs are critical for preventing software from becoming stale before it reaches a natural end of cycle. 

### Software review as a service

To combat these issues, we created a peer review system for software analogous to that for scientific publications (Ross et al. 2017). Since 2015, the rOpenSci project has been piloting a system of peer code review for software submissions. This approach brings together best practices for publication peer review along with new practices that are unique to reviewing software. The system deliberately combines elements of traditional academic peer review with practices from open-source software review. Commonalities with traditional publishing workflow include a full editorial board with handling editors, two reviewers per submission and revisions before acceptance. The process differs in a few key ways. We also use heuristic tools to automatically check submitted software against a list of more than 200 best practices.  The review process is fully open, and anyone is welcome to weigh in with constructive feedback. Unlike traditional peer review where  only one to two exchanges occur between authors and reviewers over months, all exchanges in our review happen in real time, and dozens of interactions are not uncommon. The forced transparency ensures that interactions are non-adversarial (see Salmon 2018  for a sentiment analysis of review threads). We think it's important to emphasize that research software is almost never reviewed and our process not only serves as a quality filter but also works to elevate and standardize development practices within the research community.

### Advantages of rOpenSci’s software review process

The rOpenSci review process has several advantages:

* Provides opportunities for collaboration and is a rewarding experience for both authors and reviewers.

* Provides  detailed feedback on software design and implementation, from big-picture best practices (unit testing, continuous integration) to specific line-by-line feedback on code readability and organization.  

* Helps package authors plan for sustainability by focusing many of our package standards on maintainability.  rOpenSci packages are required to have comprehensive testing, continuous integration, and community contribution guidelines and are reviewed for features such as code readability and likely maintenance challenges so as to make ongoing maintenance and contribution for a community easier.  By participating in the process, we also introduce authors to a community of practice that often leads to additional programmers contributing to the packages in large and small ways. We also act as a maintainer of last resort.  rOpenSci monitors the status of packages, reaching out to authors if they do not respond to failed package tests due to dependency changes and making changes ourselves if necessary.

* Combines an open peer review model with a portable review  model. Although rOpenSci curates packages, it is not a publisher. The editors help authors smoothly navigate submission to various package managers such as CRAN and Bioconductor but also to two journals as part of a pilot. Given that rOpenSci inspired the Journal of Open Source Software (JOSS), since the inception of JOSS it has been possible to have a rOpenSci submission fast tracked through JOSS for rapid acceptance without further review. We extended this model in November 2017 and established a partnership with the journal Methods in Ecology and Evolution (MEE), a member of Wiley Publishing. MEE accepts software with ecology and evolution applications as ``applications papers.'' This model shows a lot of promise and has potential to extend to other journals.

* Evolves based on feedback from reviewers and authors, such as the adoption of additional guidelines on what makes software more user-friendly (Ross et al. 2018)]. Current recommendations and review practices are described in a living developers guide ([https://devguide.ropensci.org/](https://devguide.ropensci.org/)). 

* Has been steadily working toward automating as many software checks as possible, freeing up the reviewers to use their limited time for assessing other aspects that cannot be easily automated. 

### Limitations and challenges of software onboarding

**Scope**. Currently rOpenSci only accepts packages that fit a narrow scope of topics -- those that support the data management lifecycle and facilitate computational reproducibility for scientific research.  This scope is based on our organization's mission and the expertise of the editor and reviewer base we have developed, and such a scope is necessary because of a finite (though growing) number of volunteers.   This leaves a large fraction of packages and authors without a similar peer review forum.  Other forums, such as the Journal of Open Source Software, Bioconductor, and the Journal of Statistical Software, have limited scope or less full-featured review processes.  In particular, authors of small packages that implement statistical methods lack a place for comprehensive feedback. 

**Expertise**. Our approach requires expert reviewers who understand not only algorithms implemented by the software but also details of software engineering. Nevertheless, the average time required for reviewing is not considerably different from a traditional research paper (https://ropensci.org/blog/2018/05/03/onboarding-is-work/)

**Time**. Since open-source software is typically in a constant state of development, defining an appropriate stage for external review is challenging.  Reviewers are not available to return to evaluate every change or release.  

### Changing academia’s incentive structures

The results of scientific endeavors are communicated primarily  as peer-reviewed publications. The citation impact of such products is captured by using metrics such as the h-index and form the basis for hiring, promotion, and tenure. The changing nature of science means that researchers now produce many more valuable outputs than just papers, one of which is software. While software research products often have a greater overall impact than publications have, both the reward and review systems have failed to keep up. Scientists have little incentive to release high-quality software; and although more and more researchers are releasing their software in some form, the lack of formal review mechanisms is contributing to the fragility of the system.

More recently several journals have emerged as venues for software papers. These include Journal of Open Source Software, Journal of Open Research Software (JORS), and Software X. By providing traditional citations, these venues allow researchers to obtain credit in more traditional forms.  For a more details on rOpenSci’s software review process, please read the the [full paper](https://doi.org/10.1109/MCSE.2018.2882753) on which this blog article is based.

rOpenSci continues to address an unmet need by helping researchers develop high-quality software that is easier to sustain in the long run. Since 2015 we have peer reviewed and published over 140 software packages and worked to elevate and standardize development practices in the research community. We have just begun an effort to develop new standards for statistical software.

### Further reading
This article is based on a paper in the IEEE Computing in Science and Engineering special issue on Accelerating Scientific Discovery with Reusable Software: Karthik Ram, Carl Boettiger, Scott Chamberlain, Noam Ross, Maëlle Salmon, and Stefanie Butland, *A Community of Practice Around Peer Review for Long-Term Research Software Sustainability*, Computing in Science and Engineering 21, 59--65 (2019). DOI: [10.1109/MCSE.2018.2882753](https://doi.org/10.1109/MCSE.2018.2882753)

Complete citations for the references mentioned in this article can also be found in the full paper.

### Author bios

Karthik Ram is a senior staff scientist with the Berkeley Institute for Data Science, a research faculty member with the Berkeley Museum of Paleontology, University of California, Berkeley, and the co-founder of the rOpenSci project. Contact him at karthik.ram@berkeley.edu. 

Carl Boettiger is an assistant professor with the Department of Environmental Science, Policy, and Management, University of California, Berkeley, and a member of the rOpenSci leadership team. Contact him at cboettig@berkeley.edu. 

Scott Chamberlain is the co-Founder of rOpenSci and a software developer with rOpenSci. Contact him at scott@ropensci.org. 

Noam Ross is a senior scientist with EcoHealth Alliance and an editor with rOpenSci. Contact him at noam.ross@gmail.com

Maëlle Salmon is a volunteer editor and a part-time software engineer with rOpenSci. Contact her at maelle@ropensci.org

Stefanie Butland is the community manager with rOpenSci. Contact her at stefanie@ropensci.org

<!---
Publish: yes
Track: community
Topics: Software Process Improvement, Software Engineering, peer code review, Software Sustainability
--->
