# When is worse better?
<!--deck text start-->
Worse may be better when simplicity is prioritized over other features.
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86 "Mark C. Miller GitHub Profile")
#### Publication date: May XX, 2023

Resource information | Details
:--- | :---
Article title  | [The Rise of Worse is Better](https://www.dreamsongs.com/RiseOfWorseIsBetter.html)
Author | Richard P. Gabriel
Length | ~1,700 words, 10 min. read
Focus | Software Engineering

The [Worse-is-Better](https://www.dreamsongs.com/WorseIsBetter.html) approach to software engineering was first described by Richard P. Gabriel to help explain why the highest quality products do not always have the widest adoption and greatest success.
Gabriel presented the concept in a [1991 essay](https://www.dreamsongs.com/WIB.html) where he expressed his disappointment about the slow adoption of Lisp, a programming language he had helped to create. 
To elucidate the challenges that Lisp was encountering, he compared and contrasted two design philosophies.

* The philosophy of *The Right Thing*, used in the design of Lisp, which includes these characteristics.

  * Simplicity -  It is more important for the [user] interface to be simple than it is for the implementation.
  * Completeness - All reasonably expected cases must be covered even if some simplicity is sacrificed.
  * Consistency - Consistency is as important as correctness even if some simplicity and/or completeness is sacrificed.
  * Correctness - Incorrectness is not at all acceptable.

* The philosophy of *Worse-is-Better*, used in the design of other subpar products, shares the same characteristics with a different prioritization and emphasis.

  * Consistency - Inconsistency should be avoided but not where doing so would jeopardize simplicity.
  * Completeness - As many reasonably expected cases as possible should be covered without loss of simplicity.
  * Correctness -  Incorrectness is not acceptable. But, it is slightly better to be simple than correct.
  * Simplicity - Both the [user] interface and the implementation must be simple but implementation trumps interface.

Ironically, Gabriel introduced the notion of Worse-is-Better to try to make a case for why it is a bad idea.
He even argued that Unix and C are examples of products developed using the Worse-is-Better approach and are like computer viruses and have permeated every aspect of computing.

Although  Gabriel's primary intention was to suggest Worse-is-Better as a subpar approach, his ideas may have unintentionally lent credibility to Worse-is-Better as a bonafide software engineering methodology.
The author revisited these concerns and issues in a [new essay](https://www.dreamsongs.com/WorseIsBetter.html)  written around 2000.
Futhermore, in 2010, Stanford offered a [CS course](https://cs.stanford.edu/people/eroberts/cs201/projects/2010-11/WorseIsBetter/index.php/Main_Page.html) where Worse-is-Better was considered as one of several approaches in a computer science course.

In some respects, the article reads like the counter-argument to [never make perfect the enemy of good [enough]](https://www.rand.org/pubs/research_reports/RR2150.html), which is also sometimes paraphrased as making perfect the enemy of *possible* or the enemy of *done*.
In reflecting on the role of [perfect](https://betterprogramming.pub/why-software-should-be-good-enough-and-not-perfect-b741b07865d7) and [good](https://news.ycombinator.com/item?id=12377385) in my own life and 30+ year long career as a software engineer within the HPC/CSE community, I have come to the realization that none of us have ever really had the luxury of making perfect the enemy of anything.

We are all too over-subscribed, split across so many tasks, trying to do so much more with less, that most of our software development lives are just a frustrating series of unsatisfying compromises because of the large number of practical constraints under which we all daily operate.
Our choices are almost never between perfect and good but are almost always between good and garbage.
Our programming lives often feel like continuous triage.

All that being said, readers may want to consider how the Worse-is-Better philosophy can facilitate faster development, increased user adoption, and simplified software maintenance.
The article is also a reminder that sometimes having fewer features in software can even create a better user experience.

<!---
Publish: yes
Pinned: no
Topics: Software engineering, Software process improvement
RSS update: 2023-05-15
--->
