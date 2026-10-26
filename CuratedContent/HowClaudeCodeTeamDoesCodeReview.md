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

As AI coding agents and models improve, they can generate increasing amounts of (mostly) working code to implement new features, fix bugs, and make other changes.
However, gaps in the specifications given to agents and mistakes made by models can introduce bugs, security vulnerabilities, flawed designs and architectures, and other problems.
Reviewing AI-generated code is therefore essential to prevent defects and technical debt from accumulating in the codebase.
As a result, writing clear specifications and reviewing code become key bottlenecks in AI-assisted software development.
Who better to consult on these challenges than the frontier AI labs using their own AI coding agents tools to develop software?

In *How the Claude Code Team Does Code Review*, Anthropic software engineers describe a review process spanning local verification, automated bug and security reviews, continuous integration, and approvals based on each change's risk.
AI agents review more of the code, allowing developers to focus their limited attention on critical code and issues that agents struggle to assess.
Human developers remain responsible for deciding what to build, defining specifications, making architectural decisions, evaluating evidence, and owning the outcomes of the changes they direct.

The authors emphasize measuring review effort along with the usage of feature flags, reverts, and staged releases to contain and reverse problems that escape the initial review and merge process.
They also describe improving AI reviewers with examples from past failures, filtering false positives, limiting repeated review cycles, and preparing for rapid rollbacks/reverts.
Some review failures that led to reverts also become test cases in the AI reviewers' evaluation suite.
These practices support an incremental approach to deciding which checks to automate and which changes need one or more human reviewers.

In following this updated process, the authors report that, from June to September 2026, the number of pull requests merged into the Claude Code codebase more than doubled while the proportion requiring a revert fell by more than 40%.

For scientific software teams, this case study suggests a way to assess review workflows as AI coding becomes more common.
Teams could begin with one repository and examine whether automated review catches defects while reducing reviewer effort.
Domain experts could pay particular attention to numerical algorithms, scientific assumptions, and changes that affect reproducibility, using project-specific validation criteria to guide adoption.

<!---
Publish: yes
Pinned: no
Topics: peer code review, AI for better development, continuous integration testing, software process improvement
RSS update: 2026-10-29
--->
