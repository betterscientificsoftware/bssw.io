# UX Methods Across the Research Software Lifecycle

#### Contributed by Md Hasan Shahriar Simanto and Rajshree Deshmukh

#### Publication date: November 6, 2026

Research software teams often hesitate to invest in user experience work. Some think it is too early to talk to users; others think the project is too far along for design changes to matter. Both instincts get in the way of the same thing: understanding whether the software actually works for the people using it.

But UX isn't a "one-and-done" step – it's a toolkit that applies at every turn. In practice, every stage of a project has a few usability questions worth answering. The infographic below outlines key UX techniques and their relevance across the project lifecycle:

<img src='../../images/UX-methods-research-software-lifecycle.png' class='page lightbox'/>

*The full-size infographic and detailed guide on above methods are available in the open-access [Zenodo resource](https://doi.org/10.5281/zenodo.22287846).*

### Planning: What should we build, and for whom?

Early on in the planning phase, the question is what to build and for whom. Here, methods like stakeholder interviews, semi-structured interviews and contextual inquiry are invaluable. These techniques help uncover the scientific goals and, more importantly, the hidden frustrations and workarounds that formal requirements documents often miss.

### Design and Development: Is it functional & feasible?

As the design takes shape and you move into development, the focus shifts to feasibility and if the approach will actually work for users. Sketching, prototyping and cognitive walkthroughs allow teams to test designs and interactions early, spotting confusing elements or unclear guidance before significant engineering resources are spent.

### Release & Validation: Can people actually use it?

Once something is built and you are in the release and validation phase, the question becomes if people can use it effectively. Methods like heuristic evaluation and targeted usability tests (even a single think-aloud session) help uncover friction points in the actual product. This real-world feedback is far more powerful than internal team assumptions.

### Maintenance & Sustainability: Does it need to change?

Finally during maintenance, the question is whether the software still works as users and their workflows evolve. At this stage, teams can combine broad signals with deeper evidence: behavioral analytics, support ticket analysis, and user surveys help us understand what people are actually doing in the software over time.

In reality, Software development is rarely linear. Unforeseen constraints like funding changes, new scientific questions, or shifting requirements mean usability hurdles surface constantly. UX processes should therefore not be treated as activities that belong only at one stage.

Enhancing user experience also requires more than formal methods. Building trust and engagement relies heavily on user outreach, strong onboarding, and relationship building. Embedding continuous feedback checkpoints at every stage is essential for creating intuitive and frictionless software.

AI-assisted development can shorten the time needed to implement software, but faster implementation does not reduce the need to understand users. If anything, the ability to build more quickly makes it even more important to know what is worth building in the first place.

<br>

<details markdown="1">
<summary><h2 style="display:inline;">Details on UX Methods in the chart</h2></summary>


<h3>Journey Mapping</h3>
<ul>
  <li>Visualize steps of how users accomplish goals to identify pain points &amp; gaps.</li>
  <li>Early in development, it can help teams articulate assumptions about how users may accomplish a goal and identify questions that need validation.</li>
  <li>In later stages, it can help diagnose friction in workflows that have been in production for years.</li>
  <li>A map built without user input can be a useful starting point when time is tight, but it reflects the team's assumptions rather than users' reality, so it still needs to be validated with real users before it can be treated as a finding.</li>
</ul>
 
<h3>Semi-structured Interviews</h3>
<ul>
  <li>Gather in-depth contextual insights from a user group via a flexible interview format.</li>
  <li>While effective for gathering requirements early on, these methods remain valuable across all project phases to uncover UX friction and pinpoint targeted solutions, such as addressing workflow gaps or missing functionality.</li>
  <li>This method scales well depending on the time and resource constraints. Five to eight conversations with a reasonably similar group of users is typically enough to surface the most common and recurring themes.</li>
</ul>
 
<h3>Stakeholder Interviews</h3>
<ul>
  <li>Structured discussions with project owners, funders, and contributors to define goals and keep design decisions aligned.</li>
  <li>Most useful at the start of a project and at the start of each funding cycle, when scope and priorities are being set.</li>
  <li>Stakeholders describe what they want built, but that's not always what users actually need. So it's best paired with research that involves real users.</li>
</ul>
 
<h3>Competitive Analysis</h3>
<ul>
  <li>A review of existing tools and workflows that solve part of the same problem, to identify common approaches, gaps, and opportunities.</li>
  <li>In research software this is less about market position than about avoiding reinvention, and about inheriting conventions expert users already know from tools they use.</li>
  <li>Most valuable during planning and design, and worth revisiting when a new tool gains traction in the domain.</li>
</ul>
 
<h3>User Personas &amp; Archetypes</h3>
<ul>
  <li>Short profiles of the target user base capturing goals, expertise, and pain points, giving the development team a shared reference instead of an abstract "user."</li>
  <li>For research software, archetypes based on role or expertise, such as a domain scientist, a method developer, and an operator, tend to be more useful than demographic personas.</li>
  <li>Personas are only as useful as the research behind them. Assumption-based personas can align a team temporarily, but they should be validated and updated as user understanding improves.</li>
</ul>
 
<h3>Conceptual Sketches</h3>
<ul>
  <li>Low-fidelity sketches, wireframes, or AI-generated prototypes used to convey a vision and get buy-in from funders and stakeholders.</li>
  <li>Particularly useful during planning, when there is nothing built yet to point at.</li>
  <li>Label them as concepts, not commitments, so they don't get mistaken for the final design.</li>
</ul>
 
<h3>User Scenarios</h3>
<ul>
  <li>Short narratives describing a specific person trying to accomplish a specific goal in a realistic context, used to understand constraints and usage variations.</li>
  <li>Useful in planning to clarify what the software needs to support, and in design to test whether a proposed approach holds up.</li>
  <li>Good scenarios can be reused later as tasks in usability testing, so it pays off to write them thoughtfully.</li>
</ul>
 
<h3>Usability Testing</h3>
<ul>
  <li>Task-based "think-aloud" sessions where someone works through a realistic task using a mockup, prototype, or working software while narrating their thinking.</li>
  <li>The key is giving people representative, non-leading tasks rather than asking for their opinions. Resist the urge to help when they get stuck, since getting stuck is the data.</li>
  <li>This method scales down more than most teams expect. Even one session on one properly designed, unbiased task, run on an early prototype, often surfaces more problems than anticipated.</li>
</ul>
 
<h3>Sketching and Prototyping</h3>
<ul>
  <li>Creating a rough, low-effort version of an idea, from a hand-drawn sketch to a clickable prototype, and putting it in front of users, funders, or stakeholders before investing real engineering effort.</li>
  <li>Keeping it rough is important. Polished mockups tend to get polite agreement, since they look finished and people assume the decisions are already made.</li>
  <li>Mostly a design-stage activity, but it applies any time a substantial new feature/design comes up, even during maintenance.</li>
</ul>
 
<h3>Heuristic Evaluation</h3>
<ul>
  <li>A review of an interface against established usability principles, typically using a structured template.</li>
  <li>Can be conducted by one person in an afternoon. Two or three reviewers working independently will catch noticeably more.</li>
  <li>Finds the problems experts can see, so it complements testing with real users rather than replacing it. Useful at any stage once there's something designed to review, whether that's an early prototype or a mature interface.</li>
</ul>
 
<h3>Support Issue Analysis</h3>
<ul>
  <li>A review of support tickets, issue trackers, and mailing list threads to identify where users repeatedly encounter friction.</li>
  <li>No recruitment needed. The data already exists, so this is often the fastest place to start on an established project.</li>
  <li>Tickets over-represent users persistent enough to file one. People who hit a wall during a process and quietly gave up won't appear in this analysis.</li>
</ul>
 
<h3>Contextual Inquiry</h3>
<ul>
  <li>Observing people working in their own environment rather than asking them to describe it.</li>
  <li>Reveals workarounds, informal scripts, and constraints that users don't think to mention.</li>
  <li>Most associated with early research, but equally useful during maintenance when other signals suggest something is wrong and you need to see what's actually happening.</li>
  <li>Even a single session, sitting with one user through real work, often reveals something you'd never have thought to ask about. It takes more coordination than an interview, but it is worth the effort.</li>
</ul>
 
<h3>Information Architecture</h3>
<ul>
  <li>Organizing and labeling content and functionality so people can find what they need. In research software this includes command structure, documentation layout, and naming of parameters, modules, and outputs, not just menus.</li>
  <li>Most often addressed during design, but organizational and naming problems frequently surface again during maintenance as functionality grows.</li>
</ul>
 
<h3>Card Sorting &amp; Tree Testing</h3>
<ul>
  <li>Card sorting asks users to group and label items, helping you generate a structure for your menus or content. Tree testing asks users to find something in a structure you already have, helping you validate it.</li>
  <li>Useful from design onward, and into maintenance whenever support issues suggest people can't find a feature that already exists.</li>
</ul>
 
<h3>A-B Testing</h3>
<ul>
  <li>Comparing two versions of a design with real users to see which one better supports a task or outcome.</li>
  <li>Requires more number of users to get meaningful difference with confidence, which makes it more relevant to systems with larger user base.</li>
  <li>A smaller sample can still be worth running if paired with qualitative context rather than relying on the numbers alone.</li>
  <li>Most applicable to select optimal design from variations, or just after release during the validation phase.</li>
</ul>
 
<h3>Diary Studies</h3>
<ul>
  <li>Participants log their experience with the software over days or weeks, so you can see how use changes over time instead of catching one snapshot.</li>
  <li>Good for catching problems that only show up on the tenth use, not the first, and for understanding how adoption actually plays out.</li>
  <li>This method asks more of participants than most methods, so keep prompts short and infrequent if you want people to actually finish it.</li>
</ul>
 
<h3>Participatory Design Sessions</h3>
<ul>
  <li>Working sessions where prospective users respond to prototypes and help refine them directly.</li>
  <li>Works well with domain experts who have strong opinions, which is common in research software.</li>
  <li>Needs careful facilitation so the loudest voice in the room doesn't dictate the design.</li>
</ul>
 
<h3>Cognitive Walkthrough</h3>
<ul>
  <li>A structured evaluation of learnability. Evaluators step through a task from a new user's perspective to identify where the user might become stuck or confused.</li>
  <li>Usually conducted by UX practitioners, product-team members, or domain experts rather than representative users, though it can also be run with real users thinking out loud, called a participatory or user-led walkthrough.</li>
  <li>A useful first pass before launch or for diagnosing problems in an existing workflow. Because expert-only findings depend on the evaluators' judgment, follow up with usability testing when possible.</li>
</ul>
 
<h3>Eye Tracking</h3>
<ul>
  <li>Recording where users look to see what draws attention and what gets missed.</li>
  <li>Best for information-dense interfaces like dashboards, where visual attention is the actual question.</li>
  <li>Needs specialized equipment and expertise most research software teams won't have. Worth the investment when you specifically need to know where attention goes, not just where users struggle.</li>
</ul>
 
<h3>Content Auditing</h3>
<ul>
  <li>Reviewing documentation and in-software text, guides, references, labels, error messages, for gaps, inconsistencies, and outdated information.</li>
  <li>Research software docs drift fast, since features change faster than the text describing them.</li>
  <li>Most useful around release and after major version changes.</li>
</ul>
 
<h3>User Behavioral Analytics</h3>
<ul>
  <li>Instrumentation that shows what users actually do: which features get used, where people abandon a workflow, what never gets touched.</li>
  <li>Shows what happens, not why. Pairing it up with a qualitative method can help to validate usability issues.</li>
  <li>Applies after release. Settle privacy and consent questions before you start collecting data.</li>
</ul>
 
<h3>Chat Log Analysis</h3>
<ul>
  <li>Reviewing conversations between users and an embedded AI assistant to spot recurring questions and points of confusion.</li>
  <li>Increasingly relevant as AI assistants get built into research tools, since logs capture what people actually ask, unprompted.</li>
  <li>Watch for sensitive or unpublished research content in logs, and be clear with users about how conversations are retained.</li>
</ul>
 
<h3>User Surveys</h3>
<ul>
  <li>Broad-reach questionnaires to capture patterns and usage feedback across a large user base for reporting and planning.</li>
  <li>Surveys look easy but they aren't. Poorly worded questions produce data that's confident and wrong, and surveys tell you what people report rather than what they actually do.</li>
  <li>Work best when informed by earlier qualitative work, which helps ensure you're measuring meaningful questions rather than guessing. Done well, they scale insight in a way no other method here can.</li>
</ul>

</details>

## Additional Public Resources

Three of the methods above already have free, community-built resources:

- **Usability testing:** a Carpentries Incubator lesson on rapid usability testing, covering everything from participant recruitment through data analysis: [https://carpentries-incubator.github.io/rapid-usability-tutorial/index.html](https://carpentries-incubator.github.io/rapid-usability-tutorial/index.html)
- **Semi-structured interviews:** a presentation on practical techniques for gathering rich data from users, hosted on Zenodo: [https://zenodo.org/records/17362664](https://zenodo.org/records/17362664)
- **Heuristic evaluation:** A template for assessing your software against design heuristics, suitable for both CLI and GUI tools, developed by contributions from the STRUDEL, PESO, and CASS projects: https://github.com/cass-community/heuristics-for-scisoft
- For a broader starting point, the STRUDEL project's "Ten Principles for Creating Usable Software for Science" explains what makes scientific software different and how to approach its usability: [https://escholarship.org/content/qt0w5547jv/qt0w5547jv_noSplash_fb5d052988314657a264f28acb6ffc95.pdf](https://escholarship.org/content/qt0w5547jv/qt0w5547jv_noSplash_fb5d052988314657a264f28acb6ffc95.pdf)


## About the Authors

**Md Hasan Shahriar Simanto**

Senior UX Researcher at MathWorks, where he conducts user research for MATLAB, a scientific computing platform used by engineers and scientists. Since 2018, his work has focused on human-centered research and usability across scientific software, cloud infrastructure, cybersecurity, and enterprise systems, with current work centered on the usability of AI-assisted technical workflows. He is an active member of the US-RSE UX Working Group. Reach him at hsimanto@mathworks.com

**Rajshree Deshmukh**

User Experience Designer at Lawrence Berkeley National Laboratory's Scientific Data Division, where she designs intuitive software products and contributes to projects including NERSC, ESnet, PrOMMiS and the Orphaned Wells project. She has over ten years of industry experience at Reuters, IBM, and Nutanix, and holds a Master's in Information Design from the National Institute of Design, India. Reach her at rajshreed@lbl.gov
<!---
Publish: Yes
Track: Deep Dive
Topics: user experience design, software process improvement
--->

