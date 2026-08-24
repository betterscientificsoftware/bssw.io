# Designing AI for Human Agency, Not Just Automation

#### Contributed by [Hannah Cohoon](https://github.com/jlcohoon)

#### Publication date: August 26, 2026

<!-- begin deck -->
TLDR: To enable users' control of AI systems, we must help users avoid errors as they plan, execute, and evaluate AI actions. Some longstanding usability principles are available to guide us, as well as new AI design patterns.
<!-- end deck -->

This article is cross-posted from the [AI UX blog](https://aiux.lbl.gov/blog#h.xd8wdhojrvtc). 
<br>

Generative AI has popularized a new way of interacting with technology: users describe the output they want rather than giving a computer precise commands. In the name of productivity, we have given over some decision making power to these tools, allowing them to define approaches and make assumptions about goals. But humans remain ultimately accountable for outcomes. So how do we design interfaces for AI tools so that we give people the control they need to shape outcomes as they see fit?

Error prevention is key to helping humans maintain control of AI systems. But, as many of us have learned, it is very difficult to get AI to produce the right outcome with one prompt. Often, we revise or build on our requests until we are satisfied. In recent interviews I've conducted with researchers and technologists, I have heard how people tire of this prompt engineering. "...It takes a lot of iteration at times and it just feels like maybe I'd just rather do it myself directly rather than spend the time to iterate, review, and go back and forth," said one interviewee. This is poor user experience; exhausting trial and error is an inefficient and frustrating way to get aligned.

## Planning AI Outcomes

To avoid user frustration and keep them in control, system designers need to provide users with scaffolding to craft effective prompts. Emily Campbell, creator of The Shape of AI ([https://www.shapeof.ai/](https://www.shapeof.ai/)), refers to this scaffolding as wayfinders, tools to "help users construct their first prompt and get started." She offers eight examples of wayfinders, like nudges to alert users to actions they can take with AI and follow ups to get more information from users. When AI is used in scientific settings, system designers should combine wayfinding patterns to shepherd users through tasks like workflow construction or literature review. Agents can apply skills and interfaces can be designed to walk users through prompt generation, rather than expecting them to share necessary details on their first try.

Established usability principles also apply to AI-specific tools for preventing errors and unwanted outcomes. Designers have long advised we help users foresee the consequences of their actions, preventing allowable but unwise choices ([Molich and Nielsen, 1990](https://dl.acm.org/doi/10.1145/77481.77486)). With coding agents, this form of error prevention can be seen in the diff a user sees before accepting an agent's proposed commit. With chatbots, users may encounter error prevention when an LLM clarifies a user's intent before proceeding, perhaps asking about the tone it should use when writing. Usable systems also prevent user errors by including guardrails and checks that disallow unproductive or unacceptable actions ([Molich and Nielsen, 1990](https://dl.acm.org/doi/10.1145/77481.77486)). From Campbell's library of design patterns, we can see inline flags and parameter sliders as ways to guard against unwanted actions. These configurable tuners are "knobs on the machine that let users control" and constrain AI ([https://www.shapeof.ai/patterns/parameters](https://www.shapeof.ai/patterns/parameters)).

## Executing and Evaluating AI Actions

Applying other canonical heuristics can help humans control AI as it carries out an action. For instance, for more than 35 years, Nielsen has encouraged designers to provide users with easy ways to stop or undo an action; a system should "provide clearly marked exits," ([Molich and Nielsen, 1990](https://dl.acm.org/doi/10.1145/77481.77486), p339). For AI agents and chatbots, this usability principle explains the need for a stop button or conversation forking and emphasizes the value of version control for code. Campbell considers such stoppers to be governors, "human-in-the-loop features to maintain oversight and agency."

Control still matters even after an AI has produced an output--this is just another phase for designers to attend to. AI outputs must be easily evaluated. Nielsen advises we don't just show users AI outputs, but "show the user the best representation for judging what the AI produced." This means that if an AI agent performed analyses, we might want to plot some of those results. Or, if your LLM is giving you a summary of recent research, it should also give quotes and links to impactful and relevant papers.

Like the systems themselves, AI design principles are still evolving. But it is clear that we should not just be thinking of how to offload work--we need to think of how people can easily steer AI systems and correct course when needed.

<!-- Reference has been inlined
Molich, R., & Nielsen, J. (1990). Improving a Human-Computer Dialogue. Communications of the ACM, 33(3). https://dl.acm.org/doi/10.1145/77481.77486
-->

## Author bio

Hannah Cohoon is a User Experience Researcher at LBNL, seeking to create more rewarding and impactful careers for research software engineers and more efficient and enjoyable experiences for users. She has focused on studying and facilitating open source development, open science practices, and data intensive workflows. Hannah earned her PhD from the University of Texas at Austin. She got feedback from a human and ChatGPT when revising this post. You can reach Hannah at hcohoon@lbl.gov.

<!---
Publish: yes
Track: Experience
Pinned: no
Topics: user experience design
--->
