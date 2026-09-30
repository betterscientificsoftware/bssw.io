# Owning Your Research Infrastructure: A Website Rebuilt with an AI Agent
<!-- deck text start -->
Lorena Barba describes replacing her group's thirteen-year-old, vendor-maintained website in four days with an AI agent.
Her account is a case study in the cost of closed dependencies and in keeping verification with the human.
<!-- deck text end -->

#### Contributed by [Michael A. Heroux](https://github.com/maherou)

#### Publication date: TBD

Resource information | Details
:--- | :---
Article title | [Barba group website rebuilt with AI, and a lesson about ownership](https://lorenabarba.com/blog/barba-group-website-rebuilt-with-ai-and-a-lesson-about-ownership/)
Authors | Lorena A. Barba
Focus | Infrastructure ownership, open formats, AI-assisted development

In the blog post *[Barba group website rebuilt with AI, and a lesson about ownership](https://lorenabarba.com/blog/barba-group-website-rebuilt-with-ai-and-a-lesson-about-ownership/)*, Lorena Barba of George Washington University describes retiring her research group's website after thirteen years.
The site had been built and maintained by outside agencies, and she rebuilt it herself in four days, working with an AI agent (Anthropic's Claude).
Her central point is not about AI, but about ownership: the open parts of the old site migrated easily, and the closed parts had to be discarded.
She states it in one line: "the open part of your infrastructure ages; the closed part rots."

The post makes three points in detail:

* **The cost of closed dependencies.** A custom codebase, a vendor-held plugin license, rented fonts, and hardcoded API credentials meant that every change needed someone else's permission and money.
  Fixes and rescues over the years cost more than $12,000, and a 2024 rebuild quote was about $8,500.
* **What survived was open.** Fifteen years of posts, more than 150 publication records, and 407 comments exported to plain XML and JSON in minutes.
* **A clear division of labor with the agent.** The agent assessed the legacy code, kept three of twelve plugins, wrote the new theme and migration tools, and fixed bugs quickly.
  Barba made every decision, performed every live action, and tested every page herself.
  She warns that the result depended on her ability to read and check what was written.

The site is not scientific software, but the lessons carry over directly.
Research teams accumulate the same kinds of closed dependencies in build systems, hosting, and tools, and the cost appears years later when funding is thin.
The post also gives a concrete, bounded example of agent-assisted development that works because verification stays with a knowledgeable person.
Adoption requires no new tools, only the habit of preferring open formats and self-maintainable infrastructure, plus enough expertise to review what an agent produces.

This post should be useful to research software engineers and group leads weighing whether AI agents can help them take back control of infrastructure they currently outsource.  I have had similar positive experience in significantly revising two project websites I manage, [E4S](https://e4s.io) and the [PESO Project website](https://pesoproject.org).  In both cases, the Claude app and Claude Code were instrumental to producing a high-quality replacement with modest effort and quickly.

<!---
Publish: yes
Pinned: no
RSS update: 2026-09-30
Topics: AI for Better Development, Software Sustainability, Research Software Engineers
--->
