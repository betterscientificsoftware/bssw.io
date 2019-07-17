# When NOT to Write Automated Tests?

**Hero Image:**

- <img src='https://github.com/betterscientificsoftware/images/raw/master/testing-hero-image.png'/>[Image Source: https://www.testingspot.net]

#### Contributed by [Roscoe A. Barltett](https://bartlettroscoe.github.io)

#### Publication date: July 29, 2019

<br>

### Introduction

The importance of writing and maintaining strong automated tests for software is well established in the modern software engineering community (and in fact, tests will be written before the code when using test-driven development, TDD).
But does it always pay off to write automated tests for some piece of code?
Are there situations where one is better off not writing automated tests?
Will you be considered to be a bad developer and chastised by your peers, users, stakeholders, or your manager if every line of code that you write is not under strong automated testing?

I have been wrestling with this question since 2007 when I first read the book [*Working Effectively with Legacy Code*](https://bssw.io/items/working-effectively-with-legacy-code/)<sup>[1]</sup> and [many other books on software engineering](https://bartlettroscoe.github.io/reading-list/) and radically changed my thinking about automated testing.
In the 10+ years of my professional career prior to 2007, I wrote a lot of computational science and engineering (CSE) and applied math software with very little strong automated testing.
I used the validation-centric approach<sup>[2]</sup> to test the software that I was writing (i.e., only test/validate the software in the downstream customer code and then perhaps only manually).
As a result, I had personally written O(100k) lines of code that were being used by other people and was in the position to have to maintain.
When I realized that almost all of this software was considered "Legacy Code" according to *Working Effectively with Legacy Code* (i.e., "code without tests == legacy code"), I felt ashamed and horrified at the mass of useful but buggy and difficult-to-maintain software that I had created and now would have to deal with for years to come.
(Just recently a nasty bug came up in software I wrote around 2006 without strong automated testing that caused a good deal of harm and was an embarrassment.)

After reading the book *Working Effectively with Legacy Code*, I resolved to turn over a new leaf and become a born-again Agile software engineer who would use TDD to write all new code and religiously apply the [Legacy Code Change Algorithm](https://bssw.io/items/working-effectively-with-legacy-code/) to modify all legacy code (i.e., code without tests).
Over the years since my conversion to an Agile software engineer, I often rigorously wrote automated tests for nearly every piece of software I touched.
There where times  under schedule pressure that I slipped and reverted back to my old ways and failed to write sufficient automated tests and came to regret it.
However, there were also times where my overzealous drive to religiously test everything (which usually came after the guilt of a recent slip of not testing enough) caused me to waste time writing automated tests that were not worth the effort.
(One example is for some code in Trilinos that did not end up getting a lot of usage and is now actually deprecated to be removed.)
And now after having had followed this road from 2007 until now (having written and maintained thousands of automated tests over that time period), I have come to realize that while in the majority of cases writing automated tests is necessary or overwhelmingly beneficial, alternatively there are cases when it is actually better (all things considered) not to write automated tests for some pieces of software!
(Or to hold off in writing automated tests for now.)

### Criteria for when writing automated tests may not pay off

I have come to realize that often writing automated tests for a piece of software does not pay offwhen the following five things are ALL true about that software:

* The damage done by a defect is minor.
* The majority of defects will be obvious.
* Fixing the majority of defects will be easy.
* Manually testing the software after a change is easy.
* Writing automated tests is hard or the tests will be hard to maintain.

If all five of the above criteria are satisfied, it is often better not to write automated tests for a piece of software.
The time spent writing, maintaining, and running the automated tests does not have enough benefit to outweigh the cost.

For example, some bash scripts used locally that load some modules and then configure, build, and run tests for some software may not be worth writing an automated test suite for because:

* The damage done by not having everything complete correctly will be minor because you can just run it again.
* A failure will be obvious because the software will not even build and no tests will be run.
* The scripts do pretty basic stuff and will be easy to fix if they fail.
* It would be difficult to mock up the various commands run by the script.

Therefore, it is often not worth the investment to write automated tests for locally run scripts of this type.

### An example of where automated tests should have been added

A critical point worth remembering is that if some scripts are being used to automate some important process like deploying the software to users, where not performing the task correctly would cause non-trivial harm, then one should write some automated tests to protect the critical functionality of the scripts.
Or, if other people are running the scripts and it will not be obvious to them that a failure has occurred or they will not know how to fix it quickly, then one should likely write some automated tests for such scripts.

For example, there was a bash test-driver script in a CSE project where the script (run as a cron job) failed to detect that the code's tests were failing and instead sent out emails that everything was passing.
As a result, the code was broken for weeks with no one noticing.
A release of the software went out (to hundreds of internal users), and it was the users who noticed the new defects.
This wasted user's time, may have resulted in incorrect results, and damaged the reputation of the project releasing the software.
The lesson is that many *scripts* may actually need to be considered *software* in their own right and need to have strong automated testing just like any piece of nontrivial software.
(Just become some piece of software is written in bash or python does not mean it can be dismissed as "scripts" and avoid any automated testing.
And just because it is harder to write automated tests in some languages like bash than others like Java is not an excuse for not writing automated tests.  You can write automated tests in any Turing-complete language.)

### Notes

If the first four criteria above are satisfied but it is not too hard to write automated tests, then often one should write them anyway because it will make the code easier extend and to maintain going forward.

Adjectives like "minor", "obvious", "easy", and "hard" are all subjective and do not have precise definitions.
For example, while one person might consider these five criteria as "minor", "obvious", "easy", "easy" and "hard", another person may consider them "significant", "non-obvious", "not easy", "painful", and/or "tractable".
For example, if one does not know the sensing, separation, and fake collaborators strategies for unit testing described in *Working Effectively with Legacy Code*, then one might think that adding automated tests for a piece of software is "hard" while another more knowledgeable and/or experienced developer might consider adding tests for that piece of software to be quite tractable.

### Summary

While it often pays off to write a high-quality automated test suite for a piece of software (i.e., reduce initial development costs and improve long-term maintenance), there are situations where it does not pay off.
Here were listed five criteria that if satisfied, then it is often better not to write automated tests and instead do manual testing when any changes are made to the code.

## Disclaimer

Please don't use this blog article as an excuse for not writing automated tests for some piece of software by trying to convince yourself that the damage done by defects will be "minor", any failures will be "obvious", or the defects will be "easy" for anyone to fix.
You might think that but your users, stakeholders, and other developers (who will need to maintain this software) may not feel the same way.
So please use discretion when applying this criteria to some piece of software when deciding whether or not to write automated tests (and how much testing is reasonable).

<br>

### Author bio

[Roscoe A. Bartlett](https://bartlettroscoe.github.io) is a computational scientist and engineer in the [Center for Computing Reserach](https://cfwebprod.sandia.gov/cfdocs/CompResearch/templates/insert/research.cfm) at [Sandia National Laboratories](https://sandia.gov).
Roscoe is a long-time contributor to the [Trilinos Project](https://trilinos.org) and is currently working on various subprojects in the [Exascale Computing Project](https://www.exascaleproject.org/) including [IDEAS-ECP](https://ideas-productivity.org/ideas-ecp/).

[1]: https://bssw.io/items/working-effectively-with-legacy-code/ "Feathers, Micheal C. Working Effectively with Legacy Code.  Prentice Hall, 2004, ISBN: 0131177052 {}"
[2]: https://doi.org/10.1109/eScience.2012.6404448 "Overview of the TriBITS lifecycle model: A Lean/Agile software lifecycle model for research-based computational science and engineering software {}"

<!---
Image copyright source info…
  One public domain...
      * http://www.testingspot.net/tst-cloud.png
--->

<!---
Publish: preview
Categories: Planning, Reliability
Topics: design, testing
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
