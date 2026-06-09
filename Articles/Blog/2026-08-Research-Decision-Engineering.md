# Research Decision Engineering: Managing Cognitive Load in the Generative Era

#### Contributed by: [Dave Bunten](https://github.com/d33bs)

#### Publication date: August 2026

<!-- start of deck text -->
Generative tools are expanding what scientific software developers can accomplish — but realizing that potential depends on how intentionally we direct it. This article introduces the concept of the _research decision engineer_ to describe this evolving and opportunity-rich role, and offers practical strategies for channeling cognitive effort toward the decisions that most advance software quality and scientific impact.
<!-- end of deck text -->

The scientific software ecosystem is no stranger to change. The software gardening lens we have explored in earlier work<sup>[1],[2]</sup> asks us to think of software as a living system that requires sustained, intentional stewardship. A new season has arrived. Generative tools — software capable of producing code, tests, documentation, and architectural suggestions from natural language descriptions — are now part of many developers' daily workflows. The underlying technologies, from large language models to agent-based coding assistants, are evolving rapidly; what they share is the capacity to generate at a speed and breadth that no individual developer could match alone. This shift is not just a new tool in the toolshed — it is a change in the nature of the craft itself.

While much attention has focused on what these tools can produce, less attention has been paid to how they change the cognitive experience of development. Generative tools do not eliminate technical decisions — they redistribute them, creating space for developers to operate at a higher level of abstraction. The gardener who once shaped each plant by hand now directs a crew that works at speed, channeling that energy toward a more intentional and ambitious vision for the garden. This is the work of the **research decision engineer**.

### What is decision engineering?

Decision engineering is not a new discipline invented alongside generative tools. It describes a dimension of software development that has always existed, now given greater visibility and impact as the scope of what a single developer can initiate has grown dramatically. The **research** decision engineer does this work in a context that carries distinctive pressures: scientific correctness is non-negotiable; reproducibility is a community expectation rather than a best practice; software often serves a specific hypothesis rather than a general user population; and the "product owner" is frequently the same person writing the code. These conditions make the judgment calls of decision engineering both harder and more consequential than in many commercial settings — and they make a dedicated vocabulary for the practice more valuable. The research decision engineer frames problems precisely enough for tools or colleagues to act on them, evaluates the outputs produced, verifies correctness against real-world requirements, steers system architecture toward sustainable designs, and maintains clarity about what problem is actually worth solving. These are the skills that determine whether expanded generative capacity translates into expanded scientific value.

<img id="fig-1" src='../../images/Blog_2608_decision_engineer_overview.png' class='page lightbox' />[Figure 1. The decision engineer operates at the intersection of problem framing, output evaluation, and system steering — roles that have grown in proportion as generation tools grow in capability.]

In scientific software development specifically, decision engineering has always carried elevated influence. The software gardener who previously spent effort writing code now increasingly spends effort determining whether generated code correctly captures scientific intent, appropriately handles edge cases, and fits within a sustainable architecture. That shift is not a reduction in what developers contribute — it is an elevation of the character of that contribution, from implementation to authorship of scientific intent.

A concrete and underappreciated example of decision engineering in practice is the act of writing a precise prompt. Composing a prompt that produces useful generative output requires the same discipline as writing a good specification: you must identify the real problem, state its constraints, anticipate ambiguity, and be explicit about what success looks like. Consider the difference between asking a generative tool to "write a normalization function" versus specifying "write a per-sample normalization function for a plate-based assay where well position effects are known to confound column means — the function should accept a pandas DataFrame with sample rows and feature columns and return a corrected DataFrame of the same shape." The second prompt encodes domain knowledge, guards against a plausible but wrong implementation, and would serve equally well as a unit test description. The value of that exercise does not live only in the output it produces — the act of framing a problem rigorously enough to be acted on is itself a form of scientific thinking. Research decision engineers who treat prompting as a specification discipline develop habits of problem clarity that improve all their work, generative or otherwise.

### Neighbors in the decision space: Data science, decision science, and a growing community

Decision engineering does not arrive from nowhere. Two neighboring disciplines have been practicing versions of it for decades, and RSEs can learn considerably from both.

**Decision science** is a formal field that studies how individuals and organizations make choices under uncertainty, drawing on probability theory, psychology, economics, and operations research.<sup>[3]</sup> Decision scientists develop structured approaches for modeling uncertainty, quantifying the expected value of different choices, and communicating recommendations to stakeholders who must act on incomplete information. These practices — sensitivity analysis, decision trees, Bayesian reasoning, structured deliberation — are precisely the kind of disciplined thinking that the research decision engineer needs when evaluating generated outputs, steering architecture, or judging whether a proposed solution actually addresses the right problem.

**Data scientists** who work alongside RSEs often operate in this space instinctively. Their workflows are built around cycles of hypothesis, evaluation, and refinement: a model is proposed, its outputs are interrogated against domain knowledge, its failure modes are characterized, and a judgment is made about whether it is fit for purpose. This is decision engineering applied to analytical pipelines. Data scientists have also developed a particular fluency with communicating uncertainty — a skill that maps directly onto the research decision engineer's challenge of conveying the limits of generated or automated work to scientific stakeholders who may interpret confident-looking output as reliable truth.

The connection runs the other direction as well. RSEs who think explicitly about decision engineering can offer data scientists something concrete in return: structured practices for the moments where analysis work stalls not for technical reasons but for judgment ones. A data science pipeline that has grown too complex to reason about is not primarily a software problem — it is a value stream problem, solvable by mapping the steps that actually deliver scientific value and eliminating the rest. A project where acceptance criteria keep shifting is not primarily a communication problem — it is a product leadership problem, addressable by anchoring the work to a specific scientific question and making that anchor visible. Decision engineering gives these familiar frustrations a vocabulary and a set of tools.

Research software engineering sits at the intersection of these fields, and the rise of generative tools makes that intersection more visible and more consequential. The capacity to generate plausible-looking analytical code at speed means that the bottleneck in a research data pipeline is increasingly not the writing of code but the judgment about whether that code correctly expresses a scientific question — and whether that question was the right one to ask. That judgment is the shared work of the data scientist, the decision scientist, and the research decision engineer, and it benefits from all three perspectives.

Beyond these two established fields, the generative era is also expanding the community of practitioners who need decision engineering skills at all. Domain scientists who are not professional developers — biologists, physicists, social scientists — can now initiate and shape more software than ever before, using generative tools to close the gap between their scientific intuition and a working implementation. For these practitioners, decision engineering is not a professional specialization to aspire to but an immediate practical need: the ability to frame a problem precisely, evaluate whether generated output captures domain intent, and know when to bring in deeper engineering expertise. The generative era does not just change how RSEs work — it invites a broader community into the craft, and creates new opportunities for collaboration across the boundary between domain expertise and software practice. Research decision engineers who understand this can position themselves as the enabling partners that broader community most needs.

<img id="fig-2" src='../../images/Blog_2608_decision_neighbors.png' class='page lightbox' />[Figure 2. Research decision engineering sits at the convergence of research software engineering, data science, and decision science. Each field contributes complementary tools for evaluating choices, managing uncertainty, and aligning work with scientific goals.]

### Cognitive load: A biological reality

To understand why this shift matters, we must first take seriously the biological constraints of human cognition. Cognitive load theory,<sup>[4]</sup> originating from educational psychology, describes the demands placed on working memory — the limited mental workspace where active thinking happens. Working memory can hold only a small number of distinct chunks of information at once,<sup>[5]</sup> and when that capacity is exceeded, performance degrades: errors increase, decisions become shallower, and the ability to detect subtle problems diminishes.

Cognitive load is traditionally divided into three types. **Intrinsic load** is the inherent complexity of the task itself — understanding a novel algorithm or a domain-specific data model. **Extraneous load** is overhead imposed by poor design of the work environment — unclear prompts, noisy output, ambiguous acceptance criteria. **Germane load** is the productive cognitive effort that builds lasting understanding and skill — the insight you carry forward after a hard problem. In a scientific software context, intrinsic load might be the genuine difficulty of implementing a numerical solver correctly; extraneous load might be the effort of reading through a hundred lines of plausible but irrelevant generated scaffolding to find the five lines that actually matter; and germane load is the understanding of *why* the solver requires a particular boundary condition — understanding that no generated code can substitute for and that makes all future related work faster.

Used well, generative tools can reduce extraneous load substantially — handling boilerplate, scaffolding test structures, surfacing relevant prior implementations — freeing germane capacity for the decisions that actually benefit most from human judgment. This is the opportunity at the center of the generative era: not simply doing the same work faster, but doing qualitatively different and more meaningful work.

The counterpart to this opportunity is **decision fatigue**: the documented phenomenon where the quality of decisions degrades as the cumulative number of choices grows across a day or a task.<sup>[6]</sup> Generative tools that are not used with intention can increase extraneous load — producing output that covers territory not requested, carries hidden assumptions, or requires significant effort to evaluate. The craft of decision engineering is learning which decisions to delegate and which to hold, so that the germane capacity freed by generative tools goes toward the work that matters most.

This points to an important corollary worth naming explicitly: **germane load is how expertise is built.** The productive struggle of working through a hard problem — not just receiving a solution — is what builds the mental models that make someone a skilled decision engineer over time. For early-career developers and domain scientists new to software, there is real value in deliberately preserving some of that struggle, using generative tools to reduce friction without eliminating the learning opportunities that develop judgment. Investing in that growth now pays compounding returns: the developer who understands deeply why a design choice is correct is far better equipped to evaluate generated alternatives than one who has only ever accepted them.

When cognitive load is well-managed — intrinsic load matched to skill, extraneous load minimized — the conditions for **flow** become available: the state of absorbed, effortful engagement that produces both the best work and the deepest satisfaction.<sup>[7]</sup> Research decision engineers who structure their generative workflows thoughtfully — protecting focused time for the decisions that require it, delegating the rest — create more frequent opportunities for flow than the unassisted developer context has historically allowed. The generative era, used well, is not just more productive; it can be more rewarding as an experience of work.

### The self as a team

Managing cognitive load well requires knowing not just *how* to think, but *what role* you are in when you think. The same decision looks different depending on whether you are operating as the person delivering scientific output, the person building shared infrastructure, or the person holding specialized domain knowledge. The Team Topologies framework<sup>[8]</sup> offers a precise vocabulary for these distinctions, even for individual contributors. Skelton and Pais describe four fundamental team types: **stream-aligned teams** that deliver continuous value along a product or capability, **enabling teams** that help others improve their practices, **complicated subsystem teams** that manage domains requiring deep expertise, and **platform teams** that provide reliable internal services. These team types interact through defined modes: collaboration, X-as-a-Service, and facilitation.

For a single developer working with generative tools, these distinctions do not disappear — they internalize. The developer simultaneously occupies stream-aligned work (delivering software that directly serves a scientific goal, such as a working analysis pipeline), enabling work (building the reusable utilities, templates, and documented practices that let collaborators — or future-self — work more effectively), and complicated subsystem work (holding the domain expertise that the generative tool cannot reliably supply, such as knowing which numerical methods are appropriate for a specific class of differential equation). Generative tools, in this framing, behave something like a platform service — providing broad, generalized capability on demand — while the human developer holds the roles that give that capability scientific direction.

<img id="fig-3" src='../../images/Blog_2608_self_as_team_topologies.png' class='page lightbox' />[Figure 3. Adapted Team Topologies roles internalized by a single developer working with generative tools. The human developer holds domain expertise, strategy, and evaluation; the generative tool functions as a platform service providing broad generative capability.]

This framing surfaces a generative insight: **with clear role awareness, a single developer can work with the reach and coherence of a well-organized team.** The generative platform handles high-volume, lower-judgment work; the human developer holds the stream-aligned and domain-expertise roles that give that output direction and meaning. Effective decision engineering means making this collaboration explicit — knowing which seat you are in at any given moment, and using the platform's tireless capacity to amplify the decisions only you can make.

### Value streams and the art of triage

Knowing which role you are in tells you *who* is responsible for a decision. The next question is *which* decisions actually deserve attention at all. Not everything that presents itself as a decision is one worth making carefully — and in the generative era, the volume of things that could be decided grows with every tool invocation. Decision engineering requires clarity about which decisions belong in the critical path. The concept of a **value stream** — the sequence of steps that delivers something meaningful to an end user or scientific goal — provides a useful guide.<sup>[9]</sup> Not every decision is equally load-bearing. Some choices, if made poorly, directly impede the delivery of correct, reproducible science. Others are secondary optimizations that can be deferred or delegated entirely.

The Eisenhower matrix<sup>[10]</sup> offers a practical triage heuristic for this. In a scientific software context, a decision that is both urgent and important might be: a collaborator has discovered that the analysis pipeline produces different results depending on sample processing order, and a manuscript submission deadline is imminent — this demands immediate, focused human investigation. A decision that is important but not urgent is the choice of data storage format for a growing experimental dataset, where the wrong choice will compound maintenance costs for years; this deserves protected time and deliberate evaluation, not a reactive answer grabbed between meetings. A decision that is neither urgent nor important — how to name an internal helper function — is a candidate for delegation to convention or a generative tool with a style constraint. Decisions that feel urgent but are not actually important — a teammate's stylistic preference about import ordering during code review — should be resolved quickly with a default and not allowed to consume decision-making energy.

<img id="fig-4" src='../../images/Blog_2608_eisenhower_decision_matrix.png' class='page lightbox' />[Figure 4. Applying the Eisenhower matrix to software decisions in scientific software development. The upper-left quadrant (urgent + important) demands direct human judgment; the lower-right (neither urgent nor important) is the natural domain for convention and delegation.]

Generative tools can play a useful role in this triage, not by making judgments, but by helping to surface and structure them. A well-framed conversation with a generative assistant — describing the current state of a project, the open decisions on the table, and the scientific goal at hand — can help externalize the decision landscape, reducing the working memory cost of holding everything simultaneously. The Eisenhower framing gives that conversation structure and prevents the most common failure mode: treating every open question as equally urgent.

### The generative stack: Matching tools to tasks

Every step in a scientific software value stream has different cognitive requirements — and in the generative era, those requirements map onto meaningfully different tool profiles. Not all generative capability is equivalent. A model well-suited to reasoning through a novel architecture is not necessarily well-suited to implementing a narrowly scoped function, and using it for both wastes its strengths while adding unnecessary evaluation burden. Matching the right generative tool to the right task is itself a decision engineering act — one that shapes the cognitive load of the entire workflow.

The distinction that matters most in practice is between tasks that require broad reasoning across context and tasks that require focused, constrained generation within a well-defined scope. High-level reasoning tasks — writing a specification, proposing an architecture, breaking work into a coherent set of implementable issues — benefit from models with strong general reasoning and wide context, even at the cost of slower generation and more output to evaluate carefully. Implementation tasks — writing the code for a well-specified issue, generating a test suite for a defined interface, applying a fix described in a review comment — are better served by models optimized for code generation, which tend to be faster, more predictable, and less likely to wander outside the scope they were given (<a href="#fig-5">Figure 5</a>).

<img id="fig-5" src='../../images/Blog_2608_model_task_stack.png' class='page lightbox' />[Figure 5. A tiered generative workflow matching model capability to task type. Frontier reasoning models handle specification and architecture; specialized code generation models handle implementation, testing, and fixes; human review closes the loop at each stage.]

A practical generative workflow for scientific software might look like this:

1. **Specification and architecture** — the research decision engineer provides the scientific question, domain constraints, and relevant codebase context to a frontier reasoning model, which returns a draft specification and proposed architecture. The human evaluates this for scientific correctness, sustainability, and alignment with the actual research goal — not implementation detail. This is the step that most demands domain expertise; the tool provides structure, but the scientist-engineer determines whether the structure fits the science.
2. **Issue breakdown** — the frontier model decomposes the approved architecture into discrete, well-scoped implementable issues, each with acceptance criteria precise enough that a code-generation model can act on them without ambiguity. The research decision engineer reviews the decomposition for gaps, overlapping scope, and any issues that touch scientifically sensitive logic and will need closer human attention downstream.
3. **Implementation** — a code-generation model takes one issue at a time and produces the implementation. The narrow scope is intentional: it concentrates evaluation effort onto a well-defined unit rather than a sprawling generated codebase, making the human review step tractable.
4. **Tests and fixes** — the code-generation model writes tests against the implemented interface and applies fixes surfaced by those tests or static analysis. The research decision engineer's role here is to confirm that the test coverage reflects scientific intent — that what is being tested is scientific correctness, not just syntactic plausibility.
5. **Human review** — the research decision engineer reviews the assembled work against the original specification and scientific requirements, with the decision trail (prompts, issue descriptions, architectural choices) available alongside the code. This is not a rubber stamp; it is the moment where the full scientific context is brought to bear on the generated whole.

This tiered approach is a practical expression of the value stream and triage principles above: frontier model capability is expensive in both compute and human evaluation time, so it is reserved for the steps where broad reasoning and scientific context matter most. Specialized code generation handles the high-volume, well-constrained implementation work where its predictability is an asset. Human attention is preserved for the review moments that require scientific judgment — not distributed thinly across every generated line.

The specific tools available at each tier will evolve — models that are frontier today become commoditized, and new capability profiles will emerge. The workflow above is not a permanent prescription but an illustration of the underlying principle: **match generative capability to task requirement**. Before generating, ask whether this step calls for broad scientific reasoning across context or focused, constrained code production within a well-defined scope. Building that habit — pausing to ask which tool this moment actually calls for, rather than reaching for the same one by default — is itself a durable decision engineering skill, and like all such skills, it sharpens with deliberate practice.

### The gardener's finite day: Resource awareness as decision advantage

Generative tools have no inherent sense of cost. Left without constraint, they will explore a solution space indefinitely — producing elaborate architecture for a problem that needed a simple function, generating comprehensive test coverage for code that will be replaced next week, or refining an implementation long past the point where the refinement serves the science. This is not a flaw; it is simply what these tools are. They optimize for plausibility and completeness within the scope they are given. They do not know that the grant ends in three months, that the compute budget is nearly exhausted, or that the collaborator waiting on this result is presenting at a conference on Friday.

Humans know these things. And that knowledge — of time, money, team capacity, opportunity cost, and the real-world consequences of delay — is what makes human judgment about *value* irreplaceable in the generative workflow. Resource awareness is not a constraint that limits the research decision engineer; it is a form of intelligence that the tools entirely lack. The gardener who knows the season is short tends the garden differently than one who believes summer is infinite. That awareness shapes every decision: what to plant, what to prune, what to leave for next year.

In scientific software, resource constraints take concrete forms that require direct human judgment. A technically elegant solution that takes six months to build may be less valuable than a good-enough solution that ships before the grant renewal deadline. A generative tool will not make that tradeoff — it has no access to the funding calendar or the political reality of the collaboration. A comprehensive refactor of a legacy module may be architecturally correct but wrong given that the module will be deprecated when the next phase of the project begins. A perfect implementation of the wrong feature is still the wrong feature. These are not technical judgments; they are value judgments, grounded in an understanding of what the work is actually for and what it costs to do it.

This is also the deeper reason the frameworks in the preceding sections matter. Value stream mapping, Eisenhower triage, and tiered model selection are all expressions of the same underlying truth: resources are finite, decisions have opportunity costs, and the human in the loop is the only participant in the workflow who knows it. The research decision engineer who carries that awareness explicitly — into prompts, into tool selection, into the decision to ship rather than continue refining — is not accepting less. They are making a judgment that the tools cannot make for them.

The practical implication is that the research decision engineer carries the resource context into every generative interaction explicitly. This means stating constraints in prompts — not just what the function should do, but that it should be implementable within a day by a single developer and maintainable by a domain scientist who is not a software professional. It means knowing when to stop generating and ship something that is good enough for the current scientific purpose, rather than continuing to refine toward an ideal that the timeline cannot support. And it means regularly asking not just "is this correct?" but "is this the most valuable thing I could be doing with the time I have?"

The tools are powerful precisely because they are unconstrained. The research decision engineer is valuable precisely because they are not.

### Product leadership: Solving real problems

Resource awareness tells us what we can afford. Product leadership tells us what is worth affording. The generative era makes that distinction both more important and more rewarding to get right. When implementation time compresses, the constraint shifts: the bottleneck is no longer writing code but knowing what code is worth writing. A research decision engineer who invests in asking the right question — and holding that question steady as generative tools rapidly explore the implementation space — can iterate toward a correct solution faster than was previously possible. Conversely, a poorly framed question executed quickly arrives at a wrong answer at speed. The leverage that generative tools provide amplifies both the value of good framing and the cost of poor framing.

Product leadership in scientific software means keeping the scientific question at the center of every evaluation. Not just "does this code run?" but "does this code correctly express the scientific method it is meant to implement?" It means shaping generated output toward abstractions that reveal domain meaning rather than paper over complexity — choosing names, interfaces, and module boundaries that would make sense to a domain scientist, not just to a compiler. It means writing acceptance criteria in the language of science: "this function should produce the same result as the established reference implementation on the benchmark dataset" rather than "this function should return a float."

There is a temporal discipline here that connects to what the software gardening series calls *nowness rooting*<sup>[1]</sup> — the practice of orienting work toward what the science actually requires today, rather than what seemed important last month or what might be needed in a speculative future. Product leadership in the generative era means regularly pausing the generation cycle to ask: is this still the right problem? The speed of the tools makes it easier to drift — to keep refining a solution that has quietly become disconnected from the actual scientific need. The decision engineer holds that thread.

### The invisible decision trail

Generative tools introduce a challenge that is new in kind, not just degree: the decisions that shape a piece of code may leave no trace in the code itself. This problem has two related but distinct faces.

The first is **generative provenance**: the prompt that produced a piece of code, the constraints specified, and the alternatives the tool explored are typically transient — they live in a conversation window that closes and disappears. Unlike a handwritten implementation where the structure tends to encode intent (naming choices, decomposition patterns, and comments reflecting the reasoning behind them), generated code can be structurally correct and stylistically clean while remaining completely silent about what produced it. A future maintainer — or a reviewer trying to assess scientific validity — has no path back to the reasoning that shaped the output.

The second is **architectural intent**: even when code is written by hand, the *why* behind a design choice often goes unrecorded. Generative tools worsen this long-standing problem because they can generate plausible implementations of multiple valid approaches without any indication of which scientific constraints ruled out the alternatives. A numerical integration method may have been chosen for a specific reason related to stiffness or boundary conditions; if that reasoning is never recorded, a future developer may "improve" the implementation in a way that breaks the scientific correctness the original author was protecting.

For scientific software, where reproducibility is a core value, both gaps are meaningful.<sup>[11]</sup> Software may be reproducible in output but opaque in process — and process transparency is often where scientific peer review begins. The research decision engineer responds by treating the decision trail as a first-class artifact alongside the code itself. This does not require elaborate documentation of every generated line. It means preserving the key framings — what problem was being solved, what scientific constraints were applied, what alternatives were considered — in forms that travel with the repository: architectural decision records, annotated commit messages, and prompt templates stored alongside the code they produce.

### Quality with real people

Preserving the decision trail addresses what future readers and reviewers need. But there is a complementary challenge that runs in the opposite direction: making sure the decisions being made in the first place reflect what the actual users of the software need, not just what a developer assumed they needed. One of the most energizing aspects of the generative era is that it creates new opportunities for richer human connection around the work. When implementation cycles shorten, the time previously absorbed by writing code can shift toward the conversations that matter most: sitting with a domain scientist to watch how they actually use a tool, testing a prototype live with the people it is meant to serve, or exploring the real shape of a problem before any assumptions have hardened into architecture. These conversations have always been valuable; now they are more accessible, because the cost of turning an idea into something testable has dropped dramatically.

This changes the character of quality assurance. Rather than validating an implementation built on a developer's engineering assumptions, the research decision engineer can build iteratively in close dialogue with real users — discovering what the problem actually is, not just what it was believed to be. Software shaped by that kind of ongoing human contact tends to be more trustworthy and more used, because it was grown toward real needs rather than constructed toward imagined ones.

The research decision engineer treats human collaboration not as a final gate but as a generative force in itself — a form of **cognitive apprenticeship**<sup>[1]</sup> extended to include stakeholders and end users as co-authors of the scientific intent. Domain experts carry the conceptual load of scientific correctness; the developer brings the engineering perspective; and generative tools handle the volume of implementation between those conversations. Together, this distributed effort can reach a quality of scientific software that would be difficult to achieve in any single role alone.

<img id="fig-6" src='../../images/Blog_2608_decision_engineering_lifecycle.png' class='page lightbox' />[Figure 6. The decision engineering lifecycle integrates human collaboration at multiple points, treating domain experts and end users as active contributors to the scientific intent of the software — not just validators at the end.]

### A decision engineering toolshed

The sections above draw on established bodies of knowledge — cognitive science, organizational design, product thinking, decision theory — and reframe them around the specific conditions of scientific software development in the generative era. The toolshed below (<a href="#table-1">Table 1</a>) consolidates these into concrete practices and tools, organized to help research decision engineers identify where to invest attention at each stage of their work.

<p id="table-1"><span class="caption">Table 1. A research decision engineering toolshed of practices and tools for scientific software development in the generative era.</span></p>
<table>

  <tr>
   <td><strong>Concept Name</strong>
   </td>
   <td><strong>Summary</strong>
   </td>
   <td><strong>Example Tools or Techniques</strong>
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong>Cognitive load management</strong>
   </td>
  </tr>
  <tr>
   <td>Working memory protection: Externalizing the decision landscape
   </td>
   <td>Reduce the burden of holding all open decisions in working memory simultaneously by externalizing them into structured formats before beginning generative work.
   </td>
   <td>
<ul>
<li>LLM-assisted decision journaling
<li>Kanban boards
<li>Decision logs
</ul>
   </td>
  </tr>
  <tr>
   <td>Delegation discipline: Knowing what to hand off
   </td>
   <td>Consciously distinguish decisions requiring domain judgment from those that can be handled by convention, templates, or automation, and build defaults that prevent undifferentiated delegation.
   </td>
   <td>
<ul>
<li>Eisenhower matrix triage
<li>Linters and formatters
<li>Code generation templates with domain constraints
</ul>
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong>Self-as-team role clarity</strong>
   </td>
  </tr>
  <tr>
   <td>Stream alignment: Protecting the scientific value path
   </td>
   <td>Maintain explicit awareness of the scientific question or user need at the center of the work, preventing fluent but irrelevant output from consuming the critical path.
   </td>
   <td>
<ul>
<li>Team Topologies role awareness
<li>Objectives and key results
<li>Value stream mapping
</ul>
   </td>
  </tr>
  <tr>
   <td>Complicated subsystem ownership: Holding domain expertise
   </td>
   <td>Recognize and protect the aspects of a problem that require deep domain knowledge — the parts where generative fluency is most misleading and human scientific expertise is irreplaceable.
   </td>
   <td>
<ul>
<li>Domain expert review
<li>Scientific correctness checklists
<li>Annotated architectural decision records
</ul>
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong>Model-task matching</strong>
   </td>
  </tr>
  <tr>
   <td>Tiered generation: Matching model capability to task requirement
   </td>
   <td>Reserve frontier reasoning models for specification, architecture, and issue breakdown where broad context matters; use specialized code generation models for implementation, testing, and fixes where predictability and scope control are the priority.
   </td>
   <td>
<ul>
<li>Frontier models for spec and architecture
<li>Code generation models for implementation tasks
<li>Issue-scoped prompts to constrain generation
</ul>
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong>Resource-aware decision making</strong>
   </td>
  </tr>
  <tr>
   <td>Resource grounding: Carrying constraints into generative work
   </td>
   <td>State time, budget, maintainability, and scope constraints explicitly when directing generative tools, and make "good enough given what we have" a legitimate and deliberate outcome rather than a failure of ambition.
   </td>
   <td>
<ul>
<li>Constraint-annotated prompts
<li>Time-boxed generative sessions
<li>Explicit "definition of done" tied to scientific goals not technical perfection
</ul>
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong>Product leadership</strong>
   </td>
  </tr>
  <tr>
   <td>Problem framing: Specifying before generating
   </td>
   <td>Invest in precise, scientifically grounded problem specification before engaging generative tools, reducing the risk of fluent but incorrect output.
   </td>
   <td>
<ul>
<li>User story mapping
<li>Acceptance criteria written in scientific terms
<li>LLM-assisted specification review
</ul>
   </td>
  </tr>
  <tr>
   <td>Output evaluation: Verifying correctness beyond plausibility
   </td>
   <td>Develop systematic habits for evaluating generated outputs against scientific requirements, not just syntactic or stylistic correctness.
   </td>
   <td>
<ul>
<li>Scientific unit tests
<li>Property-based testing
<li>Peer review of generated implementations
</ul>
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong>Decision trail and reproducibility</strong>
   </td>
  </tr>
  <tr>
   <td>Decision provenance: Preserving the reasoning behind generated code
   </td>
   <td>Record the key framings, constraints, and alternatives considered during generative work so that the software's decision history remains legible and scientifically reproducible.
   </td>
   <td>
<ul>
<li>Architectural decision records
<li>Annotated prompt templates
<li>Structured commit messages
</ul>
   </td>
  </tr>
  <tr>
   <td colspan="3" ><strong>Human collaboration and co-creation</strong>
   </td>
  </tr>
  <tr>
   <td>Early collaboration: Building with users, not for them
   </td>
   <td>Engage domain experts and end users throughout development — not as validators at the end but as co-authors of scientific intent, using shortened implementation cycles to create more time for live testing and conversation.
   </td>
   <td>
<ul>
<li>Cognitive apprenticeship practices
<li>Usability walkthroughs
<li>Incremental demos with stakeholders
</ul>
   </td>
  </tr>
  <tr>
   <td>Feedback loops: Closing the loop between generation and correction
   </td>
   <td>Build short, explicit feedback cycles between generated output and domain validation to reduce the cost of correction and the accumulation of scientific debt.
   </td>
   <td>
<ul>
<li>Continuous integration with domain-specific checks
<li>Regular pair-review with scientific collaborators
<li>Living documentation of known limitations
</ul>
   </td>
  </tr>
</table>

### A flourishing new season

Software gardening has always required the gardener to understand not just the immediate plant in front of them, but the ecosystem: the soil, the season, the neighboring growth, and the long arc of time. Research decision engineering is that same understanding brought to the question of how we think and choose — at a moment when the tools available to us can help a single gardener tend a garden of previously unimaginable scale.

The research decision engineer has always been present in the scientific software developer. Every time a researcher shaped a problem statement precisely enough for a collaborator to act on it, steered an architectural choice toward long-term sustainability, or decided which scientific question was actually worth answering — that was decision engineering. What has changed is the elevation and amplification of that role. The gardener who once spent most of the day digging now has the capacity to direct growth across an entire landscape — choosing which seeds to plant, which paths to open, which growth to prune — and making choices that shape not just one pipeline but an ecosystem of scientific capability.

The generative era does not diminish what it means to be a research software developer. It raises the stakes on the most distinctly human parts of the work: judgment, framing, curiosity, and connection with the people whose science the software serves. These are not skills the tools can replace. They are the skills that make the tools matter.

Tend boldly.

### Author bios

Dave Bunten is a Research Software Engineer with the [Department of Biomedical Informatics at the University of Colorado Anschutz](https://medschool.cuanschutz.edu/dbmi). He has over a decade of experience in the field of software development through various roles in his career. His keen interest in software design, collaboration, and innovation has driven him to explore various areas of the field. He is particularly passionate about research data engineering, in-memory data flow, and scientific software.

<!---
Publish: yes
Track: deep dive
Topics: software process improvement, software engineering, software sustainability, development tools, software team practices
--->

[1-sfer-ezikiw]: https://bssw.io/blog_posts/long-term-software-gardening-strategies-for-cultivating-scientific-development-ecosystems "Software Gardening {Bunten, D. & Way, G. P. Long-Term Software Gardening Strategies for Cultivating Scientific Development Ecosystems. Better Scientific Software (BSSw) Blog (2023).}"

[2-sfer-ezikiw]: https://bssw.io/blog_posts/growing-resilient-scientific-software-ecosystems-introducing-the-software-gardening-almanack "Software Gardening Almanack {Bunten, D., Davidson, W. & Way, G. Growing Resilient Scientific Software Ecosystems: Introducing the Software Gardening Almanack. Better Scientific Software (BSSw) Blog (2025).}"

[3-sfer-ezikiw]: https://us.sagepub.com/en-us/nam/rational-choice-in-an-uncertain-world/book234280 "Decision Science {Hastie, R. & Dawes, R. M. Rational Choice in an Uncertain World: The Psychology of Judgment and Decision Making (2nd ed.). SAGE Publications (2010). ISBN 978-1-4129-7269-4.}"

[4-sfer-ezikiw]: https://doi.org/10.1207/s15516709cog1202_4 "Cognitive load during problem solving {Sweller, J. Cognitive load during problem solving: Effects on learning. Cognitive Science 12, 257–285 (1988). doi:10.1207/s15516709cog1202_4.}"

[5-sfer-ezikiw]: https://doi.org/10.1037/h0043158 "The magical number seven {Miller, G. A. The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review 63, 81–97 (1956). doi:10.1037/h0043158.}"

[6-sfer-ezikiw]: https://doi.org/10.1073/pnas.1018033108 "Extraneous factors in judicial decisions {Danziger, S., Levav, J. & Avnaim-Pesso, L. Extraneous factors in judicial decisions. Proceedings of the National Academy of Sciences 108, 6889–6892 (2011). doi:10.1073/pnas.1018033108.}"

[7-sfer-ezikiw]: https://www.harpercollins.com/products/flow-mihaly-csikszentmihalyi "Flow {Csikszentmihalyi, M. Flow: The Psychology of Optimal Experience. Harper & Row (1990). ISBN 978-0-06-133920-2.}"

[8-sfer-ezikiw]: https://teamtopologies.com/book "Team Topologies {Skelton, M. & Pais, M. Team Topologies: Organizing Business and Technology Teams for Fast Flow. IT Revolution Press (2019).}"

[9-sfer-ezikiw]: https://www.lean.org/store/book/learning-to-see/ "Value stream mapping {Rother, M. & Shook, J. Learning to See: Value Stream Mapping to Add Value and Eliminate Muda. Lean Enterprise Institute (1998). ISBN 978-0-9667843-0-6.}"

[10-sfer-ezikiw]: https://www.eisenhower.me/eisenhower-matrix/ "Eisenhower matrix {The Eisenhower Matrix: Introduction and 3-Minute Video Tutorial. Eisenhower.me.}"

[11-sfer-ezikiw]: https://doi.org/10.1098/rsta.2020.0210 "Reproducibility and transparency {Gundersen, O. E. The fundamental principles of reproducibility. Philosophical Transactions of the Royal Society A 379, 20200210 (2021). doi:10.1098/rsta.2020.0210.}"

<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "Software Gardening"
[2]: #sfer-ezikiw-2 "Software Gardening Almanack"
[3]: #sfer-ezikiw-3 "Decision Science"
[4]: #sfer-ezikiw-4 "Cognitive load during problem solving"
[5]: #sfer-ezikiw-5 "The magical number seven"
[6]: #sfer-ezikiw-6 "Extraneous factors in judicial decisions"
[7]: #sfer-ezikiw-7 "Flow (Csikszentmihalyi)"
[8]: #sfer-ezikiw-8 "Team Topologies"
[9]: #sfer-ezikiw-9 "Value stream mapping"
[10]: #sfer-ezikiw-10 "Eisenhower matrix"
[11]: #sfer-ezikiw-11 "Reproducibility and transparency"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[Bunten, D. & Way, G. P. Long-Term Software Gardening Strategies for Cultivating Scientific Development Ecosystems. Better Scientific Software (BSSw) Blog (2023).](https://bssw.io/blog_posts/long-term-software-gardening-strategies-for-cultivating-scientific-development-ecosystems)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[Bunten, D., Davidson, W. & Way, G. Growing Resilient Scientific Software Ecosystems: Introducing the Software Gardening Almanack. Better Scientific Software (BSSw) Blog (2025).](https://bssw.io/blog_posts/growing-resilient-scientific-software-ecosystems-introducing-the-software-gardening-almanack)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Hastie, R. & Dawes, R. M. Rational Choice in an Uncertain World: The Psychology of Judgment and Decision Making (2nd ed.). SAGE Publications (2010). ISBN 978-1-4129-7269-4.](https://us.sagepub.com/en-us/nam/rational-choice-in-an-uncertain-world/book234280)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[Sweller, J. Cognitive load during problem solving: Effects on learning. Cognitive Science 12, 257–285 (1988). doi:10.1207/s15516709cog1202_4.](https://doi.org/10.1207/s15516709cog1202_4)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[Miller, G. A. The magical number seven, plus or minus two: Some limits on our capacity for processing information. Psychological Review 63, 81–97 (1956). doi:10.1037/h0043158.](https://doi.org/10.1037/h0043158)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[Danziger, S., Levav, J. & Avnaim-Pesso, L. Extraneous factors in judicial decisions. Proceedings of the National Academy of Sciences 108, 6889–6892 (2011). doi:10.1073/pnas.1018033108.](https://doi.org/10.1073/pnas.1018033108)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Csikszentmihalyi, M. Flow: The Psychology of Optimal Experience. Harper & Row (1990). ISBN 978-0-06-133920-2.](https://www.harpercollins.com/products/flow-mihaly-csikszentmihalyi)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[Skelton, M. & Pais, M. Team Topologies: Organizing Business and Technology Teams for Fast Flow. IT Revolution Press (2019).](https://teamtopologies.com/book)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[Rother, M. & Shook, J. Learning to See: Value Stream Mapping to Add Value and Eliminate Muda. Lean Enterprise Institute (1998). ISBN 978-0-9667843-0-6.](https://www.lean.org/store/book/learning-to-see/)
* <a name="sfer-ezikiw-10"></a><sup>10</sup>[The Eisenhower Matrix: Introduction and 3-Minute Video Tutorial. Eisenhower.me.](https://www.eisenhower.me/eisenhower-matrix/)
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[Gundersen, O. E. The fundamental principles of reproducibility. Philosophical Transactions of the Royal Society A 379, 20200210 (2021). doi:10.1098/rsta.2020.0210.](https://doi.org/10.1098/rsta.2020.0210)
