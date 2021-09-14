# Things You Should Never Do, Part I

<!--deck text start-->
Starting from scratch is often a very enticing way to shed the warts of an old code base.
But the realities of trying to do this in practice, while still having to support the old code base and existing customers, often ends in disaster.
However, there is usually a better way (a path less taken), especially in the computational science and engineering community.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date: August 11 2021

Resource information | Details
:--- | :---
Blog Article Title | [Things You Should Never Do, Part I ](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/)
Authors | Joel Spolsky
Publication | April 6, 2000

The article "Things You Should Never Do, Part I" was published on Joel Spolsky's blog "Joel on Software"<sup>[1]</sup> way back in April of 2000 (which might seem like an eternity ago in the software industry).
In this article, Joel argues that the disastrous decision by Netscape to rewrite their browser from scratch from version 4.0 to 6.0 led to a delay of 3 years between releases and arguably led to the downfall of Netscape as the browser market share got gobbled up by competitors.
(And a later analysis supported this as a major contributing factor to Netscape's downfall.<sup>[2]</sup>)
Joel also recounts other disastrous examples from Borland and Microsoft of companies making the same mistake with other products and a case where Microsoft abandoned a green-field project and was saved by their old code base that they were able revive and ship (MS Word).

There are many reasons why these "green-field" projects usually do not go well which include: a) the developers writing the new code do not really understand all of the requirements that went into the legacy software and how important the "corner cases" actually are, b) the same team writing the new code has to also maintain the old code which slows down both efforts, and c) the development team is not really any more skilled than the initial team and the new code eventually turns out to be just as much of a mess as the legacy code it is replacing.

The blog "Joel on Software" was very popular at the time of the publication of this article and it had a significant impact on the software engineering community when it first came out.<sup>[2]</sup>
What is interesting is that even though this article was published over 20 years ago along with other articles about disastrous "green-field" projects, and with all of the work that has been done on refactoring<sup>[3]</sup> and specifically on refactoring of legacy software<sup>[4]</sup>, many organizations and projects are still constantly making the costly mistake of starting from scratch over and over again.
This includes many Computational Science & Engineering (CSE) projects.
Note that the goal may not be to just maintain the existing software but instead to replace it.
However, it is usually better to replace it **incrementally** one piece and one subsystem at a time.<sup>[5]</sup>
This typically reduces risk and uncertainty and improves return on investment. 
But, of course, there are cases where rewriting software from scratch may be a better choice.<sup>[2]</sup>, so a team should consider those factors as well before deciding to start from scratch or refactor the existing product (but most CSE teams seem to choose a rewrite-from-scratch when an incremental refactor/rewrite would have been a better choice). 

In conclusion, before a CSE team or an organization decides to "cut their losses" and start over from scratch with a green-field project, they may well take some time to consider the arguments that Joel made years ago in this article and which are made by numerous other experts in the software engineering community over the years<sup>[2],[3],[4],[5]</sup> and consider if an incremental refactoring/rewriting of the existing code base might be a more successful strategy.

<!---
Publish: yes
Pinned: no
Topics: Software engineering, Requirements, Release and deployment, Refactoring
RSS update: 2021-08-11
--->

<!-- BEGIN ORIGINAL LINK DEFS

[1]: https://www.joelonsoftware.com "Joel on Software (Blog)"
[2]: https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22 "Lessons from 6 software rewrite stories {Herb Caudill, February 19, 2019}"
[3]: https://en.wikipedia.org/wiki/Code_refactoring "Code refactoring {Wikipedia}"
[4]: https://bssw.io/items/working-effectively-with-legacy-code "Working Effectively with Legacy Code"
[5]: https://martinfowler.com/bliki/StranglerFigApplication.html "Strangler Fig Application {Martin Fowler, June 29, 2004}"

END ORIGINAL LINK DEFS -->

<!-- ALL CONTENT BELOW HERE IS AUTO-GENERATED FROM wikize_refs.py -->

<!--- INTERMEDIATE LINK DEFS POINT TO ANCHORS IN TABLE --->
[1]: #ref1 "Joel on Software (Blog)"
[2]: #ref2 "Lessons from 6 software rewrite stories"
[3]: #ref3 "Code refactoring"
[4]: #ref4 "Working Effectively with Legacy Code"
[5]: #ref5 "Strangler Fig Application"

<!--- TABLE OF REFS RENDERED AS MARKDOWN --->
References | &nbsp;
:--- | :---
<a name="ref1"></a>1 | [Joel on Software (Blog)](https://www.joelonsoftware.com)
<a name="ref2"></a>2 | [Lessons from 6 software rewrite stories<br>Herb Caudill, February 19, 2019](https://medium.com/@herbcaudill/lessons-from-6-software-rewrite-stories-635e4c8f7c22)
<a name="ref3"></a>3 | [Code refactoring<br>Wikipedia](https://en.wikipedia.org/wiki/Code_refactoring)
<a name="ref4"></a>4 | [Working Effectively with Legacy Code](https://bssw.io/items/working-effectively-with-legacy-code)
<a name="ref5"></a>5 | [Strangler Fig Application<br>Martin Fowler, June 29, 2004](https://martinfowler.com/bliki/StranglerFigApplication.html)
