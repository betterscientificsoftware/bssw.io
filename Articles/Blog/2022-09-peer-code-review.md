# Recommendations for Peer Code Review in Research Software Development

**Hero Image:**

- <img src='../../images/computing-abstraction.jpg' />

#### Contributed by: [Nasir Eisty](https://github.com/neisty)

#### Publication date: September 13, 2022

Peer code review is a systematic examination of source code by peers of the software’s developer to identify problems the developer can then address. It is a lightweight, asynchronous method for ensuring high-quality code. As defined in the literature, peer code review is the process of analyzing code written by a teammate (i.e., a peer) to judge whether it is of sufficient quality to be integrated into the main project codebase. 
%GAIL  - this should be cited - it is a direct quote (though the boldfacefrom the original was not included) from https://www2.umbc.edu/eseiw2013/idoese/pdf/eseiw2013_IDoESE_188.pdf
Traditionally, commercial organizations and open-source projects have been adopting peer code review as a more efficient, lightweight version of the older, more formal inspection process. While peer code review is effective and prevalent in open-source and commercial software projects, it remains underutilized in research software.
%GAIL - I agree  that  itis probably underutilized  byt reserch software  is  oftne  open source,  so  saying peer code review  is prevalent in open source but underutilized in reeqrch ... seems a bit misleading

In addition to improving general software quality, the use of peer code review has other specific benefits in the research software domain. Unlike traditional commercial/IT software, research software developers are often exploring new scientific or engineering results, which may be unknown a priori. The lack of an oracle makes it difficult for developers to create adequate tests that can diagnose whether a result is a new insight from a simulation or is the consequence of a fault in the software. Even in cases where the expected output is known, the complexity of the software often makes it impossible to adequately test all important configurations of the software and input data. Conversely, in a code review, one is able to analyze the underlying algorithm and identify problematic conditions. Therefore, while peer code review is essential for any type of software, it is even more important for research software.

In this article I talk about an empirical study I conducted with Jeffrey Carver of the University of Alabama on developers' perceptions of peer code review in research software development. The study started a while ago when I was a summer intern at the National Center for Supercomputing Applications (NCSA) at the University of Illinois Urbana-Champaign. There, I was able to interview 22 research software developers. Some were in-house NCSA researchers, and some were participants in the annual Einstein Toolkit meeting. Later, we 
%GAIL  -  by "we" do you mean Jeffrey  and  I"?
conducted a community survey of research software developers to gain a general understanding of the review process. We published the results in a journal paper, 
%GAIL -  reference?
%The resulting paper presents a lot of exciting information, 
including a description of the code review process, benefits and importance of doing code review, positive/negative experiences, challenges/ and barriers, and ways of improvement. Here, I summarize the key findings of our study and provide  general recommendations to practitioners.  
%GAIL -  I would delete this sentence if you give the reference where I suggested  Please refer to the full paper for the complete discussion (see Further reading).

### Key findings
=
Overall, research software developers typically follow an informal review process. Most respondents indicated they initiate code reviews with their peers through pull-request on GitHub, BitBucket, or GitLab. Such code reviews help research software developers identify problems in the code and produce higher-quality software.

The research software developers we  surveyed had overall positive experiences regarding code review. The respondents said they found code review a good way of knowledge sharing. They improved the code quality through good feedback and problem identification. Their significant negative experiences were that the process takes too long and that misunderstandings about the criticism occurred. Having time to do the code review is the most significant barrier faced in the code review process. Another problem is a lack of people who have both domain knowledge and coding knowledge to take part in the review process.

%GAIL - is  this really recommendations? The points seem to be just what you say in the next section. FOr example, the finding might be "With no one specifically appointed to do a peer review, there was often little more than sporadicaction" instead of  saying "To make the code review process more effective, research software development teams should formalize..."
o make the code review process more effective, research software development teams should formalizethe process and use appropriate tooling. 
%GAIL -  similarly  the next sentence could  be  reworded The  developers  felt  that there  was  little  motivation in participating in a code review: having a statement in one's  vita like "made 10 suggestions  in gitHub to help improve the code" arguably lacks  the  impact  of "developed  x  code"  
Providing incentives and training could potentially increase participation in the review process. 
%GAIL -  this also seems like a recommendation rather than a  finding. And you already said that the biggest barrier  was  the time  involved, so  investing  more time doesn't seem a soltution.
sIn addition, research software developers should invest more time in code review and improve the process by providing quick feedback. 

### Recommendations

Improving the code review process can help eliminate many problems that are not addressed by testing.Here, briefly, is a set of recommendations that research software developers can incorporate into their projects to produce high-quality research software.  
%GAIL - I would agin delete this next sentence
Once again, for the full context and discussion, please see the paper.

- Make the code review process formal with structured guidelines for each step of the process. 
- Try to ensure at least one science review and one technical review.
- Include automatic tools in the code review process, and train  peer reviewers on the best practices for using the tool.
- Allocate time to do the review. 
- Encourage people to participate in the review process, providing incentives or some kind of reward to the reviewers.
- Provide a faster response to any incoming review request.
%GAIL  - is the preceding recommendation for the developer? It seems more  for the  reviewer.  Same with next. Perhaps  move these two  to the list end?
- Train reviewers on how to phrase good feedback comments. %GAIL Good  idea, perhaps "train"  is too strong for the developers/  Maybe provide brief examples to  reviewers  about how...d
- Train developers to forget their egos and accept comments from the reviewers to improve their code.
- Provide necessary support from the administrative level that encourages people to participate in the code review process.
- Make the overall code review process faster.
%GAIL -  this last one  seems too vague

### Further reading

This article is based on a paper by Eisty, N.U., Carver, J.C. Developers perception of peer code review in research software development. Emp Software Eng 27, 13 (2022). [https://doi.org/10.1007/s10664-021-10053-x](https://doi.org/10.1007/s10664-021-10053-x)

### Acknowledgments

I thank my sponsors for the NCSA summer internship, Drs. Gabrielle Allen, Roland Hass, and Daniel S. Katz. I  also thank Dr. Jeffrey Carver, my co-author of the paper, and the study participants.

### Author bio

Nasir Eisty is an assistant professor in the Computer Science Department of Boise State University, Boise, ID. He received his Ph.D. degree in computer science from the University of Alabama in May 2020. His research interests lie in the area of empirical software engineering, software quality, and research software engineering. He was a [recipient of the Better Scientific Software Fellowship](https://bssw.io/fellows/nasir-eisty) in 2020 and an Honorable Mention in 2019.

<!---
Publish: yes
Topics: peer code review
--->
