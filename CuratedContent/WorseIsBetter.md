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
Gabriel introduced this concept in a [1991 essay](https://www.dreamsongs.com/WIB.html) where he bemoaned the sluggish uptake of Lisp, a programming language he helped to develop.
In an attempt to explain the challenges Lisp was facing, he compared and contrasted two design philosophies.

* The philosophy of *The Right Thing*, used in the design of Lisp, which includes these characteristics...

  * Simplicity - it is more important for the [user] interface to be simple than it is for the implementation.
  * Completeness - All reasonably expected cases must be covered even if some simplicity is sacrificed.
  * Consistency - Consistency is as important as correctness even if some simplicity and/or completeness is sacrificed.
  * Correctness - Incorrectness is not at all acceptable.

* The philosophy of *Worse-is-Better*, used in the design of other inferiour products, which includes the same characteristics with a different prioritization and emphasis...

  * Consistency - Inconsistency should be avoided but not where doing so would jeopardize simplicity.
  * Completeness - As many reasonably expected cases as possible should be covered without loss of simplicity.
  * Correctness -  Incorrectness is not acceptable. But, it is slightly better to be simple than correct.
  * Simplicity - Both the [user] interface and the implementation must be simple but implementation trumps interface.

Ironically, Gabriel introduced the notion of Worse-is-Better to try to make a case for why it is a bad idea.
He even argued that Unix and C are examples of products developed using the Worse-is-Better approach and that they represent the ultimate in computer viruses.
They have worked their way into literally *everything*.

Although his primary aim was to suggest Worse-is-Better is an inferior approach, he may have unwittingly given rise to and even lent credibility to Worse-is-Better as a bonafide software engineering methodology.
In 2010, Stanford even offered a [CS course](https://cs.stanford.edu/people/eroberts/cs201/projects/2010-11/WorseIsBetter/index.php/Main_Page.html) where Worse-is-Better was considered along with other approaches.

In reading *The Rise of Worse is Better*, one is reminded of another important software engineering tenet; [never make perfect the enemy of good [enough]](https://fairygodboss.com/career-topics/perfect-is-the-enemy-of-good).

<!---
Publish: yes
Pinned: no
Topics: Software engineering, Software process improvement
RSS update: 2023-05-15
--->
