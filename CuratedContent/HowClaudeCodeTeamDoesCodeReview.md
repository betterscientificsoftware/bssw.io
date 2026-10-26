# How the Claude Code Team Does Code Review

<!-- deck text start -->
Anthropic's Claude Code team describes how it combines AI review, automated checks, and human judgment to handle growing volumes of code while preserving accountability.
<!-- deck text end -->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe "Roscoe A. Bartlett")

#### Publication date: October 29, 2026

Resource information | Details
:--- | :---
Article title | [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/)
Authors | Addy Osmani, Morgan Westlee Lunt, and Qing Wang
Publication | October 15, 2026, claude.dev blog
Focus | AI review, verification, human accountability

As AI coding agents and AI models improve, their ability to write (mostly) working code to implement new features, address bugs, and make other changes explodes the amount of code they can generate.
However, gaps in up-front specifications given to the agents, and mistakes made by the models, result in bugs, security vulnerabilities, bad designs and architectures, and other problems.
Therefore, review of AI-generated code is needed to find and correct these problems to avoid an explosion in the amount of bugs and technical debt being added to the codebase.
And with this, the key bottleneck in accelerating AI-assisted software development becomes up-front specification and code review.
Who better to consult on how to address these problems than the frontier AI labs developing software with themselves?

In *How the Claude Code Team Does Code Review*, Anthropic software engineers describe a review process spanning local verification, automated bug and security reviews, continuous integration, and approvals based on each change's risk.
The amount of code reviewed by AI agents increases while limited human attention is focussed on a smaller amount of critical code and issue where AI agents are currently lacking.
In particular, human developers remain responsible for deciding what to build, input specifications, architectural decisions, evaluating evidence, and the changes they direct.

The authors emphasize measuring review effort alongside the usage of feature flags, reverts, and branch graduation to contain and reverse problems that make it through the initial review and merge process.
They also describe improving AI agent reviewers with examples from past failures, filtering false positives, limiting repeated review cycles, and preparing for rapid rollback/reverts.
Some past review failures leading to reverts are also added as new eval cases to the AI review agent eval suite.
These practices support an incremental approach to deciding which checks can be automated and where human review is needed (and sometimes more than one human reviewer).

The updated review process they describe resulted in a doubling of the rate of code changes merged to the Claude Code codebase while simultaneously reducing the after-merge revert rate by more than 40% from the month of June to September, 2026.

For scientific software teams, this case study suggests a way to assess review workflows as AI coding becomes more common.
Teams could begin with one repository and examine whether automated review catches defects while reducing reviewer effort.
Domain experts could reserve particular scrutiny for numerical algorithms, scientific assumptions, and changes that affect reproducibility, using project-specific validation criteria to guide adoption.

<!---
Publish: yes
Pinned: no
Topics: peer code review, AI for better development, continuous integration testing, software process improvement
RSS update: 2026-10-29
--->
