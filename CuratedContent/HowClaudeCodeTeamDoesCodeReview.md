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

In *How the Claude Code Team Does Code Review*, Addy Osmani, Morgan Westlee Lunt, and Qing Wang describe a review process spanning local verification, automated bug and security reviews, continuous integration, and approvals based on each change's risk.
People remain responsible for architectural decisions, evaluating evidence, and the changes they direct.

The authors emphasize measuring review effort alongside reverts and incidents.
They also describe improving reviewers with examples from past failures, filtering false positives, limiting repeated review cycles, and preparing for rapid rollback.
These practices support an incremental approach to deciding which checks can be automated and where human review is needed.

For scientific software teams, this case study suggests a way to assess review workflows as AI coding becomes more common.
Teams could begin with one repository and examine whether automated review catches defects while reducing reviewer effort.
Domain experts could reserve particular scrutiny for numerical algorithms, scientific assumptions, and changes that affect reproducibility, using project-specific validation criteria to guide adoption.

<!---
Publish: yes
Pinned: no
Topics: peer code review, AI for better development, continuous integration testing, software process improvement
RSS update: 2026-10-29
--->
