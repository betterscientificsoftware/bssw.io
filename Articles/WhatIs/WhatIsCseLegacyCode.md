# What is CSE Legacy Code?
#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)

#### Publication date: May 29, 2019

<!--deck start--->
CSE legacy code can involve several years or even decades of development and resources invested in it. Maintaining such legacy code comes with several engineering challenges and its imperative to know how to balance the critical goals associated with the code.
<!--deck end--->

<!--body start--->

Successful computational engineering tools involve many person years of development. Nonetheless, software development costs alone represent only a portion of stakeholders' (developers, users, consumers and sponsors)
*total investment* in such tools. There are many ways in which stakeholders become *invested in* a computational
engineering tool. These include

* Software development costs
* User training and development costs
* Input database development costs
* Community adoption and development costs
* Perceived or measured commitment to validity of results

Eventually, investments in a computational engineering tool, both tangible and intangible, become so great that
wholesale re-write (that is throwing existing code out and re-writing from scratch), is not seen as an acceptable
strategy to move the code forward with new generations of computing technology.

The key software engineering challenge of *legacy code* involves balancing several goals

* Maintaining the original source code largely intact
* Maintaining *acceptable* performance with newer computing technologies
* Maintaining *acceptable* consistency in numerical results
* Maintaining external interfaces (both data and user)

To achieve these goals, changes to legacy code are typically *evolutionary* rather than *revolutionary* in nature.
Eventually, however, even evolutionary code changes can become cost-prohibitive. Typically, by the time legacy code faces
this demise, which could easily involve more than 30 years of development, the evolutionary approach has provided ample
time for suitable alternatives to develop and become adopted.

<!--body end--->


<!---
Publish: yes
Pinned: yes
Topics: refactoring
--->
