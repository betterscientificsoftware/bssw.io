# Growing Resilient Scientific Software Ecosystems: Introducing the Software Gardening Almanack

#### Contributed by: [Dave Bunten](https://github.com/d33bs), [Will Davidson](https://github.com/willdavidson05), and [Gregory P. Way](https://github.com/gwaybio)

#### Publication date: April 15, 2025

<!-- start of deck text -->
Scientific software underpins modern research, yet much of it suffers from fragility due to poor design and maintenance, threatening sustainability and trust. The Software Gardening Almanack introduces a new paradigm, treating software as a living ecosystem that can be nurtured to promote long-term resilience and reproducibility.
<!-- end of deck text -->

<img id="fig-1" src='../../images/French_Orchard_at_Harvest_Time_(Le_verger)_(SM_1444).png' class='page lightbox' />[Figure 1. Following guidelines and practices outlined in an Almanack enhances software development, much like it nurtures growth in a garden.]

Scientific software is at the heart of modern discovery, powering advancements across many fields.<sup>[1],[2],[3],[4]</sup>  Yet, beneath the surface of these achievements lies a sobering reality: much of scientific software is fragile due to low quality implementation or design<sup>[5]</sup>, which leads to challenges related to software collapse.<sup>[6]</sup> These challenges jeopardize software sustainability, productivity, and trustworthiness, posing threats to the very foundations of research.<sup>[1]</sup> The Software Gardening Almanack<sup>[7]</sup> offers a new way forward: treating software as an emergent, living ecosystem (<a href="#fig-1">Figure 1</a>). The Almanack describes and implements Software Gardening principles that help to cultivate sustainable, reproducible, and high-quality scientific software.

### Proliferation of fragile software ecosystems

The Consortium for Information & Software Quality (CISQ) estimated, in 2022 alone, that poor software quality cost the global economy a staggering $2.41 trillion.<sup>[5]</sup> Scientific software is no exception. In many fields, it is the norm for scientists to publish articles that contain unusable, low-quality software and other analysis code. For example, the code might lack installation instructions, omit reproducible examples, or exclude critical documentation to understand the work.<sup>[2]</sup> These observations paint a clear picture of 1) significant training gaps for research software engineering<sup>[8]</sup>, 2) misaligned incentives for delivering reproducible software, 3) the difficulty evaluating software quality, and 4) codebases growing brittle with age.<sup>[6]</sup> Despite these challenges, scientific software has experienced tremendous growth. For example, about 1.5 million repositories on GitHub that were created in 2024 contained at least one Jupyter notebook, showing 170% growth since 2022.<sup>[9]</sup>

But not all software decays so quickly, and some software can last decades. What measurements indicate whether a software repository will resist the challenges associated with poor quality and decay? GitHub Stars are often used to infer quality, but they may be fake and they may only demonstrate popularity as opposed to sustainability.<sup>[10]</sup> Furthermore, publication and citation metrics indicate usage, but they suffer from diminishing returns due to increases in the overall number of citations in recent years, larger author or reference lists, and proliferation of self-citations.<sup>[11]</sup> While easy to see and measure, these metrics paint an incomplete picture. Instead, embracing software as a complex and evolving ecosystem enables us to quantify sustainability with many measurements and perspectives.

### Tending software gardens

<img id="fig-2" src='../../images/software-gardening-lifecycle.png' class='page lightbox' />[Figure 2. All software faces lifecycles that can be better understood through a Software Gardening lens to guide sustainable development.]

We wrote about Software Gardening in an earlier blog post.<sup>[12]</sup> In that post, we compared Software Gardening to the more traditional metaphor of scientific software development as “software carpentry”.<sup>[13]</sup> In software carpentry, software is viewed as a craft that emphasizes precision, reproducibility, and start-to-finish construction. However, this analogy falls short of addressing the multidimensional challenges of time. Software decays, requirements evolve, and development grows through collaborative teams. Software Gardening<sup>[12]</sup> offers a new, complementary lens for rethinking software development. While carpentry emphasizes the skills and tools to build software, the lessons are static and product focused. Instead, Software Gardening is about nurturing growth, adapting to changes, and preparing for inevitable elements of decay (<a href="#fig-2">Figure 2</a>). A software gardener tends to their "code ecosystem" much like a gardener cultivates a garden. A software gardener removes weeds, enriches the soil, and ensures that the environment where software development happens supports healthy, sustainable growth.

### Introducing the Software Gardening Almanack

<img id="fig-3" src='../../images/software-gardening-almanack-components.png' class='page lightbox' />[Figure 3. The Software Gardening Almanack is an open-source digital book and open-source Python package. The Python package includes both reporting and linting functionality.]

The Software Gardening Almanack ([https://github.com/software-gardening/almanack](https://github.com/software-gardening/almanack)) brings these metaphors of Software Gardening to reality. The Almanack offers practical tools, insights, and strategies for creating sustainable software ecosystems. It provides guidance to solve today’s software development challenges. We conceived the Almanack out of a need to strengthen software ecosystems, reduce proliferation of fragile software, and stop exorbitant waste in scientific software development. With the Almanack, we aim to bring long-term software sustainability to the forefront of and prime consideration for scientific software development. The Almanack provides educational technology to equip software developers with knowledge and pragmatic, functional tools that lead to software that is more robust to the demands of time.

We present the Software Gardening Almanack as two open-source components: a digital book and a Python package (<a href="#fig-3">Figure 3</a>). First, the book, available through [GitHub as a Jupyter Book](https://software-gardening.github.io/almanack), acts as a learning guide, providing a curriculum of sustainable software development practices. It provides conceptual and practical advice on sustainable software development practices, illustrated with real-world examples.

<img id="fig-4" src='../../images/software-gardening-almanack-demo.png' class='page lightbox' />[Figure 4. The Almanack Python package may be used to find metrics associated with a specific repository.]

Second, the Python package, [available on PyPI](https://pypi.org/project/almanack/), transforms these ideas into software sustainability reports and software linting checks. Developers install the Software Gardening Almanack package and can immediately analyze any repository code base, which will guide their efforts toward developing software robust to decay (<a href="#fig-4">Figure 4</a>). This dual approach of education combined with applied learning ensures that the Almanack not only informs but also empowers developers to act, and, when taken together, improve the overall state of scientific software.

<img id="fig-5" src='../../images/software-gardening-almanack-package.png' class='page lightbox' />[Figure 5. A repository may be analyzed using the Almanack Python package to gather a report of metrics or perform a software linting style check of the repository.]

The Python package provides two core capabilities: a JSON-based report of sustainability metrics and a software linting-style check for specific metrics (<a href="#fig-5">Figure 5</a>). The report provides specific metadata and metrics for the repository alongside descriptions of these metrics. The software linting check assesses if the repository is following best software development practices. We have configured the check to run alongside continuous integration and deployment (CI/CD) tools to automatically check code as it is changed. The Python package can be executed by any Python interpreter, but also as a command line interface (CLI). We apply the Almanack Python package to the Almanack book itself both through CI/CD for real-time development, as well as in Almanack tutorials, which you can run through this [Google Colab notebook](https://colab.research.google.com/drive/1VZhpLW7qNYelXiy2mb_piIxkqVcthb5_).

### A deep dive into the Almanack and practical use cases

The Almanack helps developers cultivate sustainable software ecosystems. It implements several sustainability metrics and checks, which promotes sustainable software development. One of these metrics measures Shannon Entropy<sup>[14]</sup>, a concept derived from [information theory](https://en.wikipedia.org/wiki/Information_theory) that quantifies unpredictability and complexity in a given system (<a href="#formula-1">Formula 1</a>).

<img id="formula-1" src='../../images/shannon-entropy-formula.png' class='page lightbox' />[Formula 1. Shannon Entropy]

Originally used to measure how much information is required to describe a state of a variable, we apply Shannon’s Entropy formula to software by analyzing code changes. This idea was originally proposed by Hassan<sup>[15]</sup> in 2009, and we directly implement this metric within the Software Gardening Almanack. In our system, entropy reveals complexity across a project's history. High entropy indicates irregular or unpredictable code modifications, which fragilize projects, making them more expensive to maintain and prone to future error.<sup>[15]</sup> In contrast, low entropy suggests more consistent and structured software development, where changes are less likely to cause unexpected failure.

To explore software entropy empirically, we collected and analyzed about 10,000 repositories referenced in PubMed articles since 2011. In our search we also collected GitHub metadata such as commit history, stars, forks, issues, primary programming language, and more. This metadata gives us insights into software collaboration and engagement, both of which are also key drivers of software sustainability. Using the Almanack, we calculated Shannon's entropy at the file level across commits, normalizing by total lines of code (loc) per repository (<a href="#formula-2">Formula 2</a>). This normalization procedure is required for us to compare projects of varying sizes.

<img id="formula-2" src='../../images/normalized-shannon-entropy-per-file-formula.png' class='page lightbox' />[Formula 2. Normalized Shannon Entropy per file]

Our analysis showed how software entropy relates to software sustainability (<a href="#fig-6">Figure 6</a>). Projects with shorter lifespans exhibited higher entropy, likely indicating rapid and unstructured development cycles lacking sustained maintenance. These projects are prone to instability, which can severely hurt long-term use. In contrast, projects with lower entropy and higher community engagement enjoyed a longer lifespan. We observed many other interesting trends, detailed through a [“Seed Bank” notebook](https://software-gardening.github.io/almanack/seed-bank/pubmed-github-repositories/visualize-pubmed-repo-sofware-entropy.html) within the Software Gardening Almanack book content. Overall, this application shows how entropy can serve as a quick and valuable indicator of software sustainability, while also, importantly, providing insights into the causes of software decay.

<img id="fig-6" src='../../images/software-entropy-relationships.png' class='page lightbox' />[Figure 6. Relationships between software entropy, time, and community engagement. In a sample of about 10,000 GitHub repositories referenced in published scientific articles indexed on PubMed, we find that low software entropy is positively associated with sustainability and community engagement through (left) open GitHub issues and (right) number of GitHub forks.]

Proactive software maintenance using Software Gardening practices will reduce entropy and lead to more long-lasting software. Left unmanaged, high entropy causes software decay. In other words, the Almanack identifies entropy hotspots, while they’re being developed, that may require targeted maintenance. Similar to an overgrown garden, these hotspots require attention through pruning, such as refactoring and restructuring, to preserve the project sustainability.

### Future harvests

<img id="fig-7" src='../../images/almanack-future.png' class='page lightbox' />[Figure 7. Our Almanack roadmap includes the development of a reusable GitHub Action, developing and testing an empirically defined software sustainability score, and integrating checks into community-driven projects to improve scientific communication and impact, such as openRxiv.]

Looking ahead, the Almanack is poised to expand impact (<a href="#fig-7">Figure 7</a>). We will continue to implement new metrics, including a sustainability score. We will also develop other technical features, such as a GitHub Action, and integration technology for embedding with scientific communication platforms like [openRxiv](https://openrxiv.org/) to automatically assess software and analysis repositories that are associated with posted preprints. These innovations will put the Almanack into the hands of those who can benefit most: researchers, developers, and educators who are shaping the future of scientific software.

### Let’s garden together

The Software Gardening Almanack is more than a toolkit; it’s a call to action. It invites software developers to rethink how they approach software, not as a static product but as a living, evolving ecosystem. By embracing the principles of gardening—nurturing growth, fostering collaboration, and planning for the future—we can create software that not only thrives in the moment, but also stands the test of time.

So, let’s garden together. Explore the Almanack, join the community, and help cultivate a better future for scientific software!

### Acknowledgements

The Software Gardening Almanack was made possible through the support of a [Better Scientific Software (BSSw) Fellowship](https://bssw.io/fellowship) awarded to Dave Bunten. The BSSw Fellowship empowers leaders to advance scientific software quality, sustainability, and community engagement.
Through this fellowship, the project received the resources and network needed to promote best practices in software development, fostering a more maintainable and collaborative ecosystem for scientific computing.

We are also deeply grateful to the following individuals and organizations whose support has been instrumental in the creation of the Software Gardening Almanack:

* Faisal Alquaddoomi  
* Vincent Rubinetti  
* Cameron Mattson  
* Erik Serrano  
* Members of the Way Lab at the University of Colorado Anschutz Medical Campus ([https://www.waysciencelab.com/](https://www.waysciencelab.com/))  
* Department of Biomedical Informatics within the School of Medicine at the University of Colorado Anschutz Medical Campus ([https://medschool.cuanschutz.edu/dbmi](https://medschool.cuanschutz.edu/dbmi))  
* Aditi Gopalan, Jineta Banerjee and The Multi-Consortia Coordinating (MC²) Center for Cancer Biology managed by Sage Bionetworks ([https://sagebionetworks.org/community/mc2-center](https://sagebionetworks.org/community/mc2-center))  
* Jonathan Starr and The Map of Open Source Science (MOSS) managed by NumFocus ([https://www.opensource.science/moss](https://www.opensource.science/moss))  
* Better Scientific Software (BSSw) ([https://bssw.io](https://bssw.io))  
* Sustainable Horizons Institute ([https://shinstitute.org](https://shinstitute.org))

### Figure credits

[Figure 1](#fig-1) Daubigny, Charles-François, French Orchard at Harvest Time (Le verger). [Retrieved from Wikimedia Commons](https://commons.wikimedia.org/wiki/File:French_Orchard_at_Harvest_Time_\(Le_verger\)_\(SM_1444\).png).

### Author bios

Dave Bunten is a Software Developer with the [Department of Biomedical Informatics at the University of Colorado Anschutz](https://medschool.cuanschutz.edu/dbmi). He has over a decade of experience in the field of software development through various roles in his career. His keen interest in software design, collaboration, and innovation has driven him to explore various areas of the field. He is particularly passionate about research data engineering, in-memory data flow, and scientific software.

Will Davidson is a Computer Science student at the University of Colorado Boulder and an incoming Developer at Capital Group. Previously, he interned at the University of Colorado Anschutz Medical Campus, where he contributed to the Software Gardening Almanack. His work focused on software entropy analysis, Git-based metrics, and developing tools to support long-term software resilience. He is passionate about open-source development and creating innovative, high-impact software that addresses complex challenges.

Gregory P. Way is an Assistant Professor in the [Department of Biomedical Informatics at the University of Colorado Anschutz](https://medschool.cuanschutz.edu/dbmi). His lab develops methods and software for analyzing large biomedical datasets, most often in the context of drug screens for rare diseases. He believes that high-performance software facilitates science and that we could not make the next discoveries in treating human diseases without software engineers. The sustainability of software is essential to maintaining scientific progress and reducing human suffering.

<!---
Publish: yes
Track: deep dive
Topics: software process improvement, software engineering, software sustainability
--->

[1-sfer-ezikiw]: https://doi.org/10.2172/1846009 "Basic Research Needs {Heroux, M. *et al.* Basic Research Needs in The Science of Scientific Software Development and Use: Investment in Software Is Investment in Science. (2023) doi:10.2172/1846009.}"
[2-sfer-ezikiw]: https://doi.org/10.48550/arXiv.2306.03255 "Evaluation of software impact {Afiaz, A. *et al.* Evaluation of software impact designed for biomedical research: Are we measuring what's meaningful? Preprint at https://doi.org/10.48550/arXiv.2306.03255 (2023).}"
[3-sfer-ezikiw]: https://doi.org/10.5281/ZENODO.4464625 "Stanford software survey {Sochat, V. The Stanford Software Survey, 2020\. Zenodo https://doi.org/10.5281/ZENODO.4464625 (2021).}"
[4-sfer-ezikiw]: https://doi.org/10.5281/ZENODO.10073232 "Research software engineers {US Research Software Engineer Association & IEEE Computer Society. Research Software Engineers: Creating a Career Path—and a Career. Preprint at https://doi.org/10.5281/ZENODO.10073232 (2023).}"
[5-sfer-ezikiw]: https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/ "Cost of Poor Software Quality {Krasner, H. Cost of Poor Software Quality in the U.S.: A 2022 Report. https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/ (2022).}"
[6-sfer-ezikiw]: https://doi.org/10.1109/MCSE.2019.2900945 "Software collapse {K. Hinsen, Dealing With Software Collapse, in Computing in Science & Engineering, vol. 21, no. 3, pp. 104-108, 1 May-June 2019, doi: 10.1109/MCSE.2019.2900945.}"
[7-sfer-ezikiw]: https://doi.org/10.5281/ZENODO.14765834 "Software Gardening Almanack {Bunten, D., Davidson, W., Alquaddoomi, F., Rubinetti, V. & Way, G. The Software Gardening Almanack. Zenodo https://doi.org/10.5281/ZENODO.14765834 (2025).}"
[8-sfer-ezikiw]: https://doi.org/10.48550/ARXIV.2210.04275 "Research software engineers {Cosden, I. A., McHenry, K. & Katz, D. S. Research Software Engineers: Career Entry Points and Training Gaps. (2022) doi:10.48550/ARXIV.2210.04275.}"
[9-sfer-ezikiw]: https://github.blog/news-insights/octoverse/octoverse-2024/ "AI leads Python to top language {GitHub Staff. Octoverse: AI leads Python to top language as the number of global developers surges. *GitHub Blog* https://github.blog/news-insights/octoverse/octoverse-2024/ (2024).}"
[10-sfer-ezikiw]: https://doi.org/10.48550/arXiv.2412.13459 "4.5 Million (Suspected) Fake Stars in GitHub {He, H. *et al.* 4.5 Million (Suspected) Fake Stars in GitHub: A Growing Spiral of Popularity Contests, Scams, and Malware. Preprint at https://doi.org/10.48550/arXiv.2412.13459 (2024).}"
[11-sfer-ezikiw]: https://doi.org/10.1093/gigascience/giz053 "Over-optimization of academic publishing metrics {Michael Fire, Carlos Guestrin, Over-optimization of academic publishing metrics: observing Goodhart's Law in action, GigaScience, Volume 8, Issue 6, June 2019, giz053, https://doi.org/10.1093/gigascience/giz053}"
[12-sfer-ezikiw]: https://bssw.io/blog_posts/long-term-software-gardening-strategies-for-cultivating-scientific-development-ecosystems "Software Gardening {Bunten, D. & Way, G. P. Long-Term Software Gardening Strategies for Cultivating Scientific Development Ecosystems. *Better Scientific Software (BSSw) Blog* https://bssw.io/blog_posts/long-term-software-gardening-strategies-for-cultivating-scientific-development-ecosystems (2023).}"
[13-sfer-ezikiw]: https://doi.org/10.1371/journal.pcbi.1005510 "Good enough practices {Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, Teal TK (2017) Good enough practices in scientific computing. PLoS Comput Biol 13(6): e1005510. https://doi.org/10.1371/journal.pcbi.1005510}"
[14-sfer-ezikiw]: https://doi.org/10.1002/j.1538-7305.1948.tb01338.x "Mathematical theory of communication {C. E. Shannon, A mathematical theory of communication, in The Bell System Technical Journal, vol. 27, no. 3, pp. 379-423, July 1948, doi: 10.1002/j.1538-7305.1948.tb01338.x.}"
[15-sfer-ezikiw]: https://doi.org/10.1109/ICSE.2009.5070510 "Predicting faults {Hassan, A. E. Predicting faults using the complexity of code changes. in *2009 IEEE 31st International Conference on Software Engineering* 78–88 (IEEE, Vancouver, BC, Canada, 2009). doi:10.1109/ICSE.2009.5070510.}"
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "Basic Research Needs"
[2]: #sfer-ezikiw-2 "Evaluation of software impact"
[3]: #sfer-ezikiw-3 "Stanford software survey"
[4]: #sfer-ezikiw-4 "Research software engineers"
[5]: #sfer-ezikiw-5 "Cost of Poor Software Quality"
[6]: #sfer-ezikiw-6 "Software collapse"
[7]: #sfer-ezikiw-7 "Software Gardening Almanack"
[8]: #sfer-ezikiw-8 "Research software engineers"
[9]: #sfer-ezikiw-9 "AI leads Python to top language"
[10]: #sfer-ezikiw-10 "4.5 Million (Suspected) Fake Stars in GitHub"
[11]: #sfer-ezikiw-11 "Over-optimization of academic publishing metrics"
[12]: #sfer-ezikiw-12 "Software Gardening"
[13]: #sfer-ezikiw-13 "Good enough practices"
[14]: #sfer-ezikiw-14 "Mathematical theory of communication"
[15]: #sfer-ezikiw-15 "Predicting faults"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[Heroux, M. *et al.* Basic Research Needs in The Science of Scientific Software Development and Use: Investment in Software Is Investment in Science. (2023) doi:10.2172/1846009.](https://doi.org/10.2172/1846009)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[Afiaz, A. *et al.* Evaluation of software impact designed for biomedical research: Are we measuring what's meaningful? Preprint at https://doi.org/10.48550/arXiv.2306.03255 (2023).](https://doi.org/10.48550/arXiv.2306.03255)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Sochat, V. The Stanford Software Survey, 2020\. Zenodo https://doi.org/10.5281/ZENODO.4464625 (2021).](https://doi.org/10.5281/ZENODO.4464625)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[US Research Software Engineer Association & IEEE Computer Society. Research Software Engineers: Creating a Career Path—and a Career. Preprint at https://doi.org/10.5281/ZENODO.10073232 (2023).](https://doi.org/10.5281/ZENODO.10073232)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[Krasner, H. Cost of Poor Software Quality in the U.S.: A 2022 Report. https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/ (2022).](https://www.it-cisq.org/the-cost-of-poor-quality-software-in-the-us-a-2022-report/)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[K. Hinsen, Dealing With Software Collapse, in Computing in Science & Engineering, vol. 21, no. 3, pp. 104-108, 1 May-June 2019, doi: 10.1109/MCSE.2019.2900945.](https://doi.org/10.1109/MCSE.2019.2900945)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Bunten, D., Davidson, W., Alquaddoomi, F., Rubinetti, V. & Way, G. The Software Gardening Almanack. Zenodo https://doi.org/10.5281/ZENODO.14765834 (2025).](https://doi.org/10.5281/ZENODO.14765834)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[Cosden, I. A., McHenry, K. & Katz, D. S. Research Software Engineers: Career Entry Points and Training Gaps. (2022) doi:10.48550/ARXIV.2210.04275.](https://doi.org/10.48550/ARXIV.2210.04275)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[GitHub Staff. Octoverse: AI leads Python to top language as the number of global developers surges. *GitHub Blog* https://github.blog/news-insights/octoverse/octoverse-2024/ (2024).](https://github.blog/news-insights/octoverse/octoverse-2024/)
* <a name="sfer-ezikiw-10"></a><sup>10</sup>[He, H. *et al.* 4.5 Million (Suspected) Fake Stars in GitHub: A Growing Spiral of Popularity Contests, Scams, and Malware. Preprint at https://doi.org/10.48550/arXiv.2412.13459 (2024).](https://doi.org/10.48550/arXiv.2412.13459)
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[Michael Fire, Carlos Guestrin, Over-optimization of academic publishing metrics: observing Goodhart's Law in action, GigaScience, Volume 8, Issue 6, June 2019, giz053, https://doi.org/10.1093/gigascience/giz053](https://doi.org/10.1093/gigascience/giz053)
* <a name="sfer-ezikiw-12"></a><sup>12</sup>[Bunten, D. & Way, G. P. Long-Term Software Gardening Strategies for Cultivating Scientific Development Ecosystems. *Better Scientific Software (BSSw) Blog* https://bssw.io/blog_posts/long-term-software-gardening-strategies-for-cultivating-scientific-development-ecosystems (2023).](https://bssw.io/blog_posts/long-term-software-gardening-strategies-for-cultivating-scientific-development-ecosystems)
* <a name="sfer-ezikiw-13"></a><sup>13</sup>[Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, Teal TK (2017) Good enough practices in scientific computing. PLoS Comput Biol 13(6): e1005510. https://doi.org/10.1371/journal.pcbi.1005510](https://doi.org/10.1371/journal.pcbi.1005510)
* <a name="sfer-ezikiw-14"></a><sup>14</sup>[C. E. Shannon, A mathematical theory of communication, in The Bell System Technical Journal, vol. 27, no. 3, pp. 379-423, July 1948, doi: 10.1002/j.1538-7305.1948.tb01338.x.](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x)
* <a name="sfer-ezikiw-15"></a><sup>15</sup>[Hassan, A. E. Predicting faults using the complexity of code changes. in *2009 IEEE 31st International Conference on Software Engineering* 78–88 (IEEE, Vancouver, BC, Canada, 2009). doi:10.1109/ICSE.2009.5070510.](https://doi.org/10.1109/ICSE.2009.5070510)
