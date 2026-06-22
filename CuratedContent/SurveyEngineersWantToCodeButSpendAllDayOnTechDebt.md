# Survey: Engineers Want to Code, but Spend All Day on Tech Debt

<!--deck text start-->

Chainguard’s *2026 Engineering Reality Report* shows that engineers find building new features energizing, but that day-to-day work is dominated by maintenance, technical debt, and tool friction.

<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe "Roscoe A. Bartlett")
#### Publication date: January 25, 2026

Resource information | Details
:--- | :---
Article Title | [Survey: Engineers Want To Code, But Spend All Day on Tech Debt](https://thenewstack.io/survey-engineers-want-to-code-but-spend-all-day-on-tech-debt/)
Authors | Darryl K. Taft (The New Stack)
Focus | Tech debt impacts

Resource information | Details
:--- | :---
Article Title | [2026 Engineering Reality Report](https://www.chainguard.dev/2026-engineering-reality-report)
Authors | Chainguard
Focus | Developer experience survey

Software teams struggle to create new capabilities while keeping complex systems reliable, secure, and reproducible.
Chainguard’s *2026 Engineering Reality Report* puts numbers behind that tension, based on 1,200 survey responses (600 software engineers and 600 senior technology leaders) collected in August 2025.
The report’s headline is stark: while 93% of engineers say writing code and building new features is rewarding, they report spending only about 16% of their week on that kind of work.
Instead, 72% of engineers report struggling to find time to create new features because they spend 84% of their time on maintenance, upgrades, patching, vulnerability remediation, and other “toil.”

The report underscores how [technical debt](https://bssw.io/items/technical-debt-in-practice-how-to-find-it-and-fix-it) and fragmented toolchains amplify the problem.
Two-thirds of respondents say they frequently encounter technical debt that impacts their ability to deliver effectively.
Tool sprawl is another recurring theme as engineers report using many tools each week, and most say that switching between tools harms productivity (including a large fraction reporting a significant loss of focus).

The New Stack’s companion summary article, *Survey: Engineers Want To Code, But Spend All Day on Tech Debt*, provides a useful narrative overview and additional context around burnout and retention concerns.
For leaders of research software projects, this framing matters because sustained delivery requires not just talented people, but also an environment that protects time for high-value work.

Some of the more interesting quotes from this article include:

> Chainguard survey reveals that developers spend 84% of their time on maintenance and tech debt
>
> Engineers spend just 16% of their week writing code and building new features, despite 93% saying that’s the most rewarding part of their jobs.
>
> ... tedious tasks (38% cited this as a barrier), ongoing code maintenance like patches and vulnerability management (another 38%), and the technical debt that two-thirds of engineers say they bump into all the time.
>
> Two-thirds of the leaders say they’re concerned about keeping their engineering talent from walking out the door.
>
> About 65% of organizations have automated most common engineering tasks, from writing code to handling admin work. And it’s working: among engineers who heavily use automation, 94% say they spend most of their time on energizing work. That compares to just 67% for those who don’t automate much of their daily tasks.
>
> Even more surprising, one in five respondents said AI is not allowed at all where they work. Kirkland said he found that “a little bit shocking.” These engineers are likely in government agencies and regulated industries.
>
> The survey also flagged the rise of “shadow AI” — engineers using unapproved tools on their own to try to get work done faster.
>
> Kirkland thinks the next big shift will be AI agents that can handle problems autonomously, working in the background while engineers sleep.

Both articles point to practical levers that translate well to the scientific software ecosystem:

* Treat “maintenance work” as planned, funded project work (dependency upgrades, [security patching](https://bssw.io/items/guide-to-securing-scientific-software), [CI](https://bssw.io/items/what-is-continuous-integration-testing) reliability, [documentation](https://bssw.io/items/diataxis-a-systematic-approach-to-technical-documentation-authoring)) rather than ad hoc interruptions.
* Reduce [context switching](https://bssw.io/items/a-look-at-detrimental-effects-of-context-switching-with-devops) by simplifying and integrating toolchains where possible, and by standardizing workflows that new team members can adopt quickly.
* Use [automation](https://bssw.io/items/github-actions-for-automation) and (carefully governed) [AI](https://bssw.io/items/ai-coding-agents-what-works-and-what-doesn-t) to reclaim time from repetitive tasks; the report associates higher automation with engineers spending more time on work that energizes them.
* Make technical debt visible and actionable: define what “debt” means for the project, track it, and routinely budget time to pay it down.

The main takeaway from this survey and its analysis is that engineering organizations (including those building research software) should intentionally design their processes and tooling to minimize and manage technical debt so teams can spend more time on the creative, mission-driven work that motivates them.

<!---
Publish: yes
Topics: software process improvement, software engineering, Development Tools, Strategies for More Effective Teams, software sustainability
Pinned: no
RSS update: 2026-01-25
--->
