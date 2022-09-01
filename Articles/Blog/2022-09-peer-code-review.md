# Title: Peer Code Review in Research Software Development

**Hero Image:**

- <img src='../../images/computing-abstraction.jpg' />

#### Contributed by: [Nasir Eisty](https://github.com/neisty)

#### Publication date: September 13, 2022

Peer code review is a systematic examination of source code by peers of the software’s developer to identify problems the developer can then address. It is a lightweight, asynchronous method for ensuring high-quality code. As defined in the literature, peer code review is the process of analyzing code written by a teammate (i.e. a peer) to judge whether it is of sufficient quality to be integrated into the main project codebase. Traditionally, commercial organizations and open source projects have been adopting peer code review as a more efficient, lightweight version of the older, more formal inspection process. While peer code review is effective and prevalent in open-source and commercial software projects, it remains underutilized in research software.

In addition to improving general software quality, the use of peer code review has other specific benefits in the research software domain. Unlike traditional commercial/IT software, research software developers are often exploring new scientific or engineering results, which may be unknown a priori. The lack of an oracle makes it difficult for developers to create adequate tests that can diagnose whether a result is a new insight from a simulation or is the consequence of a fault in the software. Even in cases where the expected output is known, the complexity of the software often makes it impossible to adequately test all important configurations of the software and input data. Conversely, when a person conducts a code review, he or she is able to analyze the underlying algorithm and identify problematic conditions. Therefore, while peer code review is essential for any type of software, it is even more important for research software.

In this article, I talk about an empirical study I conducted with Jeffrey Carver of the University of Alabama on developers' perceptions of peer code review in research software development. It started a while ago when I was a summer intern at NCSA (National Center for Supercomputing Applications at UIUC). As a result, I had first-hand access to interview 22 research software developers. Some were in-house NCSA researchers, and some were participants of the annual Einstein toolkit meeting. Later, we conducted a community survey of research software developers to gain a general understanding and published the results in a journal paper. The paper presents a lot of exciting information, including the code review process, benefits/importance of doing code review, positive/negative experiences, challenges/barriers, and ways of improvement. Instead of repeating the information here, I discuss a summary and provide a general recommendation to practitioners. 

Peer code review helps research software developers to produce high-quality software. Overall, research software developers typically follow an informal review process. Most respondents indicated they initiate code reviews with their peers through pull-request on GitHub, BitBucket, or GitLab. Code reviews help research software developers identify many problems in the code. Most of the respondents identified issues related to software quality and code mistakes.

Research software developers have overall positive experiences regarding code review. They found code review as a good way of knowledge sharing. They improved the code quality through good feedback and problem identification. Their significant negative experiences are the process takes too long and misunderstanding the criticism. There is a lack of people who have both domain knowledge and coding knowledge to take part in the review process. Moreover, having time to do the code review is the most significant barrier they face in the code review process.

To improve the code review process and make it more effective, research software development teams should make it a habit by formalizing the process and using appropriate tooling. There is a need for more people to participate in the code review process, so providing proper incentives and training could potentially increase participation. In addition, research software developers should invest more time in code review and improve the process by providing quick feedback. Improving the code review process can help eliminate many problems that are not addressed by testing.

Again, I refer to the paper below in the “Further reading” section for full context, and here I provide a set of recommendations that research software developers can incorporate into their projects to produce high-quality research software.

* Make the code review process formal with a structured guideline for each step of the process.
* Try to ensure at least one science review and one technical review.
* Include automatic tools in your code review process and train your peer reviewers on the best practices to use the tool.
* Encourage people to participate in the review process and allocate some time to do the review.
* Provide incentives or some kind of reward to the reviewers to participate in the code review.
* Provide a faster response to any incoming review request.
* Train reviewers on how to phrase good feedback comments.
* Train developers to forget their egos and accept comments from the reviewers to improve their code.
* Provide necessary support from the administrative level that encourages people to participate in the code review process.
* Make the overall code review process faster.

### Further reading

This article is based on a paper - _Eisty, N.U., Carver, J.C. Developers perception of peer code review in research software development. Empir Software Eng 27, 13 (2022). [https://doi.org/10.1007/s10664-021-10053-x](https://doi.org/10.1007/s10664-021-10053-x) _

### Acknowledgment

I want to thank my sponsors for the NCSA summer internship, Drs. Gabrielle Allen, Roland Hass and Daniel S. Katz. I would also like to thank my co-author of the paper Dr. Jeffrey Carver and the study participants.

### Author bio

Nasir Eisty is an assistant professor in the Computer Science Department of Boise State University, Boise, ID. He received his Ph.D. degree in Computer Science from the University of Alabama in May 2020. His research interests lie in the area of Empirical Software Engineering, Software Quality, and Research Software Engineering. He received a 2020 BSSw (Better Scientific Software) Fellowship award from the Department of Energy (DOE).

<!---
Publish: yes
Topics: peer code review
--->
