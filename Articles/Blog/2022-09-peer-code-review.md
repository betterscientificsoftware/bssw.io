# Recommendations for Peer Code Review in Research Software Development

#### Contributed by: [Nasir Eisty](https://github.com/neisty)

#### Publication date: September 14, 2022

<!-- start of deck text -->
A recent paper on peer code review in research software provides some simple, practical recommendations to make the process better.
<!-- end of deck text -->

Peer code review is a systematic examination of source code by peers of the software’s developer to identify problems the developer can then address. It is a lightweight, asynchronous method for ensuring high-quality code. As [defined in the literature](https://www.umbc.edu/eseiw2013/idoese/pdf/eseiw2013_IDoESE_188.pdf), peer code review is the process of analyzing code written by a teammate (i.e., a peer) to judge whether it is of sufficient quality to be integrated into the main project codebase.
Traditionally, commercial organizations and open-source projects have been adopting peer code review as a more efficient, lightweight version of the older, more formal inspection process. While peer code review is effective and prevalent in open-source and commercial software projects, it remains underutilized in research software.

In addition to improving general software quality, the use of peer code review has other specific benefits in the research software domain. Unlike traditional commercial/IT software, research software developers are often exploring new scientific or engineering results, which may be unknown a priori. The lack of an oracle makes it difficult for developers to create adequate tests that can diagnose whether a result is a new insight from a simulation or is the consequence of a fault in the software. Even in cases where the expected output is known, the complexity of the software often makes it impossible to adequately test all important configurations of the software and input data. Conversely, in a code review, one is able to analyze the underlying algorithm and identify problematic conditions. Therefore, while peer code review is essential for any type of software, it is even more important for research software.

In this article I talk about an empirical study I conducted with Jeffrey Carver of the University of Alabama on developers' perceptions of peer code review in research software development. The study started a while ago when I was a summer intern at the National Center for Supercomputing Applications (NCSA) at the University of Illinois Urbana-Champaign. There, I was able to interview 22 research software developers. Some were in-house NCSA researchers, and some were participants in the annual Einstein Toolkit meeting. Later,  Jeffrey and I
conducted a community survey of research software developers to gain a general understanding of the review process. We published the results in a journal paper (see [Further reading](#further-reading)).

The resulting paper presents a lot of exciting information, 
including a description of the code review process, benefits and importance of doing code review, positive/negative experiences, challenges, barriers, and ways of improvement. Here, I summarize the key findings of our study and provide  general recommendations to practitioners.
Please refer to the full paper for the complete discussion.

<br>

<img src='../../images/Blog_2209_peer_review.png' class='page'/>[Image by katemangostar on Freepik.com]

### Key findings

Overall, research software developers typically follow an informal review process. Most respondents indicated they initiate code reviews with their peers through pull-request on GitHub, BitBucket, or GitLab. Such code reviews help research software developers identify problems in the code and produce higher-quality software.

The research software developers we  surveyed had overall positive experiences regarding code review. The respondents said they found code review a good way of knowledge sharing. They improved the code quality through good feedback and problem identification. Their significant negative experiences were that the process takes too long and that misunderstandings about the criticism occurred. Having time to do the code review is the most significant barrier faced in the code review process. Another problem is a lack of people who have both domain knowledge and coding knowledge to take part in the review process.

To make the code review process more effective, research software development teams should formalize the process and use appropriate tooling.
Providing incentives and training could potentially increase participation in the review process.
In addition, research software developers should invest more time in code review and improve the process by providing quick feedback. 

### Recommendations

Improving the code review process can help eliminate many problems that are not addressed by testing. Here, briefly, is a set of recommendations that research software teams can incorporate into their projects to produce high-quality research software.  Once again, for the full context and discussion, please see the paper.

- Make the code review process formal with structured guidelines for each step of the process.
- Try to ensure at least one science review and one technical review.
- Include automatic tools in the code review process, and train  peer reviewers on the best practices for using the tool.
- Allocate time to do the review.
- Encourage people to participate in the review process, providing incentives or some kind of reward to the reviewers.
- Provide a faster response to any incoming review request.
- Educate reviewers on how to phrase good feedback comments.
- Encourage developers to forget their egos and accept comments from the reviewers to improve their code.
- Provide necessary support from the administrative level that encourages people to participate in the code review process.
- Make the overall code review process faster.

### Further reading

This article is based on a paper by Eisty, N.U., Carver, J.C. Developers perception of peer code review in research software development. Emp Software Eng 27, 13 (2022). [https://doi.org/10.1007/s10664-021-10053-x](https://doi.org/10.1007/s10664-021-10053-x)

### Acknowledgments

I thank my sponsors for the NCSA summer internship, Drs. Gabrielle Allen, Roland Hass, and Daniel S. Katz. I  also thank Dr. Jeffrey Carver, my co-author of the paper, and the study participants.

### Author bio

Nasir Eisty is an assistant professor in the Computer Science Department of Boise State University, Boise, ID. He received his Ph.D. degree in computer science from the University of Alabama in May 2020. His research interests lie in the area of empirical software engineering, software quality, and research software engineering. He was a [recipient of the Better Scientific Software Fellowship](https://bssw.io/fellows/nasir-eisty) in 2020 and an Honorable Mention in 2019.

<!---
Publish: yes
Track: experience
Topics: peer code review
--->
