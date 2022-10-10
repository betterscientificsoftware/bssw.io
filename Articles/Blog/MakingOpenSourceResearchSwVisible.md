# Making Open Source Research Software Visible: A Path to Better Sustainability?

#### Contributed by [Neil Chue Hong](https://github.com/npch "Neil Chue Hong GitHub Profile")

#### Publication date: September 12, 2019

Why do open source research software projects appear to have a low rate of success? Is it because we lack appropriate models for sustaining research software development or is it because the community isn’t seeing the results? 

In "traditional" open source software projects, development is often sustained by creating a community of contributors from different organisations that collectively provide effort towards the ongoing maintenance and feature development of the software. For open source research software, although there are examples of the same model being used, it appears to have a smaller chance of success. In this blog post, I’ll examine my hypothesis that this is due to the differing competing drivers for contributing to software, particularly in academic settings, and also suggest some models that might improve the contributions.

### Understanding the economics

First, let’s do a quick crash course on economics, in particular how goods are categorised. Goods are anything that satisfy human wants and provide utility. Rather than just seeing this as one axis (public vs private), goods can be split into rivalrous/non-rivalrous (does the consumption of a good by one consumer prevent or reduce the ability of other customers from being able to consume it) and excludable/non-excludable (is it possible to prevent consumers who haven’t paid for the good from consuming it).

To see what this means in practice, consider the following table:

&nbsp; | Excludable | Non-excludable
:--- | :--- | :---
Rivalrous  | Private goods (Food, clothing, cars, parking spaces) | Common pool resources (Fish-stocks, timber, coal)
Non-rivalrous | Club goods (Cinemas, private parks, satellite television) | Public goods (Free-to-air television, air, national defense)


### Where does open source software fit?

At first glance, you might think that open source software is an example of a public good. It’s clearly non-excludable, as the terms of an open source licence means it isn’t possible to prevent consumers who haven’t paid for the good from consuming it. But is it rivalrous or non-rivalrous? Does the consumption of open source software by one consumer prevent or reduce the ability of other customers from being able to consume it?

Here, the key thing is that this isn’t just about the good itself (the code), but about the cost of production of the software. Software lives somewhere between the concept of a durable good (such as a car, or a brick) and a consumable (such as food) but in general, without maintenance, software has a limited lifespan. This means that the key cost is not how much it costs to create a new copy of a piece of software but how much it costs to maintain it. I’m definitely not the first to think of this: Titus Brown provides insight on how it applies to research in his [blog post](http://ivory.idyll.org/blog/2018-oss-framework-cpr.html), which references the work that Nadia Eghbal has [done](https://nadia.xyz/tragedy-of-the-commons) in this [area](https://www.fordfoundation.org/about/library/reports-and-studies/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure/); Dan Katz [takes this further](https://danielskatzblog.wordpress.com/2018/09/26/fundamentals-of-software-sustainability/) to consider how this relates to [software collapse](http://blog.khinsen.net/posts/2017/01/13/sustainable-software-and-reproducible-research-dealing-with-software-collapse/). This all points to open source software being a common pool resource.

Using a common pool resource argument enables companies to more effectively justify committing effort. If open source software is like a forest where anyone is allowed to cut trees for timber or firewood, then if no one helps plant new trees, eventually the forest will disappear. It is in the interests of organisations using open source to contribute back so they can continue using that software. For this to work, organisations need to have two things. Firstly, a long-term interest in the software - possibly why some of the most successful types of open source software are platforms that other organisations build plugins for, services, and tools with niche functionality. Secondly, trust that other consumers will contribute appropriately, forged by communication and often governed via foundations.

### Why doesn’t this argument work in academia?

The challenge is that there are additional drivers for research software in academia. The curse of novelty is one which is well identified, where it is easier to get funding for producing new things than for maintaining or reusing existing work. Likewise, there is a challenge because the main driver for the use of the software is not the software itself, but the research output it enables. However both of these can be seen elsewhere, and I do not believe these are the main challenges.

Instead, I assert that the biggest challenge is that it is harder to make the “forest” argument, because there is a larger disconnect between the people benefitting from the software and the people controlling the budgets. The Nobel Prize winning economist, Elinor Ostrom, noted in [her work on common pool resources](https://www.cambridge.org/gb/academic/subjects/politics-international-relations/political-theory/governing-commons-evolution-institutions-collective-action-1?format=PB&isbn=9781107569782) that in cases of failure: “no one communicates, everyone acts independently, no attention is paid to the effects of one’s actions, and the costs of trying to change the structure of the situation are high” -- there has been a breakdown in context and communication. Paying money for software is commonplace in universities: for things like email, research services like Web of Science, and large academic software packages like Matlab, Qualtrics and SPSS. What is not commonplace is paying for open source software, because the use of such software is split across many more people, for many different reasons and it makes it much harder for the true impact of the software to be understood. 

There are new models of funding open source research software that might make this easier. Fiscal sponsors (e.g., [NumFOCUS](https://numfocus.org), [Code for Science and Society](https://codeforscience.org), [Commons Conservancy](https://commonsconservancy.org)) provide the administrative and legal functions on which to help construct a cohesive community. There are more ways of being able to pay for expert support ([RSE groups](https://society-rse.org/community/rse-groups/), [QuanSight](https://www.quansight.com)) or tipping developers ([GitHub Sponsors](https://github.com/sponsors)). One approach that literally acknowledges the consumable nature of software is that of [TideLift](https://tidelift.com), which provides subscriptions to organisations, and allows project maintainers to sign up to get some of the income. However all of these approaches help only only help when the key challenge of creating the cultural change within academic organisations to value a sustained and collaborative commitment to open source software have been overcome.

### Recommendations for improving the visibility of software

I believe that one of the key solutions to the issue is connecting academic organisations more directly to the software they rely on, by making it more visible. In the same way that we can’t really understand the impact of deforestation without seeing the pictures or visiting the devastated land, we need to create a shared context to understand the value of the open source software we use.

I propose a number of recommendations to make this value and impact more visible, and put it at the heart of what universities do:

1. As universities set up research software engineering (RSE) groups, broker an agreement with RSE group leaders to set aside a set percentage of their time to contribute to open source software that is important to the organisation. For this to work, the way they use that time must be prioritised by the projects they are working on, based on what they are best placed to contribute to, not by their university (who only get to choose which software projects they are contributing to).
2. Universities should seek to associate their brand with open source software more. Universities contribute significant amounts of effort already to leading open source projects, and yet it is often unrecognised.
3. Universities should promote working on open source projects as part of Undergraduate and Masters programmes, similar to doing internships, so it is seen as valuable career development for both students and faculty.
4. University libraries should consider subscription style donations to some of the most significant open source research software projects that they rely on, as determined by annual surveys.

The challenge with maintaining research software is that there is more software produced than we need to maintain, but there is more software that needs to be maintained than we are currently doing. By making software more visible, it becomes easier to make the argument that we can’t keep taking from open source software projects without giving back.

### Acknowledgments

The original idea behind this blog post was the result of a conversation with [Allison Randal](https://allisonrandal.com). Additional feedback was given by [Daniel S Katz](https://danielskatz.org). It was first presented as a white paper at the [2019 Collegeville Workshop on Sustainable Scientific Software (CW3S19)](https://collegeville.github.io/CW3S19/) before being revised and extended for this blog post, which is crossposted on the [SSI](https://www.software.ac.uk/), [BSSw](https://bssw.io), and [URSSI](http://urssi.us) sites.

### Author bio

[Neil Chue Hong](https://www.software.ac.uk/about/staff/person/neil-chue-hong) is Director of the Software Sustainability Institute ([SSI](https://www.software.ac.uk)) and a Senior Research Fellow at [EPCC](https://www.epcc.ed.ac.uk), University of Edinburgh.


<!---
Publish: yes
RSS update: 2019-09-12
Categories: Collaboration
Topics: Funding sources and programs, strategies for more effective teams
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
