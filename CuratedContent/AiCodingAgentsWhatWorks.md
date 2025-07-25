#  AI Coding Agents: What Works and What Doesn't

<!-- deck text start --> 
AI agents are emerging as the preferred way to exploit the usage of artificial intelligence (AI) large language models (LLMs) to perform a variety of software development tasks.
Learn how the open-source OpenHands AI agent is successfully being used to automate various software engineering tasks and the current limits of AI agents.
<!-- deck text end --> 

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date: July 28, 2025

Resource information | Details
:--- | :--- 
Publication title  | AI Coding Agents: What Works and What Doesn't
Presenters | Robert Brennan (CEO of All Hands AI), Joe Peliter (Head of Product and Ops at All Hands AI),
Web links | [Video](https://www.youtube.com/watch?v=_rltvykJV4E)

The webinar "AI Coding Agents: What Works and What Doesn't" provides an overview of the usages for AI coding agents with examples from the open-source [OpenHands Software Engineering Agent](https://github.com/All-Hands-AI/OpenHands).
The OpenHands AI agent uses Large Language Models (LLMs) and related tools to implement a variety of software development-related tasks.

AI coding agents are transforming software development, shifting the focus from repetitive typing to creative problem-solving for engineers.
The presenters delved into the intricacies of these agents, highlighting what makes them effective and where their challenges lie.

**Understanding AI Coding Agents and Their Mechanics**

At its core, an AI coding agent is defined by its capacity to interact with the real world using tools like code editors, terminals, and browsers.
The OpenHands agent exemplifies this by handling some simpler software development tasks from start to finish.
These agents operate in a continuous loop: a large language model (LLM) proposes an action, that action is executed, and the resulting output is fed back to the LLM, which decides on the next action, and so forth until the given termination criteria is satisfied (or some iteration or other limit is reached).

Some of the basic tools that are used modern AI coding agents include:

* **Code Editor:** Modern agents efficiently manage code changes using diff-based or find-and-replace methods, avoiding the need to rewrite entire files.

* **Terminal:** The agent can execute a number of different terminal commands to drive builds, run tests, and perform many other actions.
Challenges here include gracefully handling long-running commands, executing commands in parallel, and managing standard input.

* **Browser:** The agent can access various websites to extract data and even interact with the webpage (e.g. clicking buttons, etc.).
Instead of parsing raw HTML, agents find it more efficient to convert HTML to markdown or an accessibility tree.
Their interaction strategies range from having the agent write JavaScript to selecting nodes based on screenshots.

A critical aspect of AI agent operation is **sandboxing**.
Because LLMs are used to select what commands to run and because LLMs can often behave in unpredictable ways, it is important to restrict what data an AI agent can read and what actions they can perform.
One way to accomplish this is to run an AI agent in an isolated "sandbox" container that has limited access to data from the host machine.
The user who runs the AI agent (OpenHands) can select the exact set of directories from the host system to expose to the AI agent and its tool.
Running agents within a (Docker) sandbox is vital for security, preventing unintended actions on the user's machine.
However, securely managing API key access and sensitive operations remains an ongoing area of development.

**Best Practices for Leveraging Coding Agents**

To get the most out of AI coding agents, the presenters suggested several best practices:

* **Start Small:** Begin with clearly defined and manageable tasks.

* **Provide Clear Instructions:** Be specific in your prompts to the AI agent, not only about what needs to be done but also how.

* **Treat Them Like New Engineers:** Current LLMs often need more hits and context than a regular software engineering.

* **Be Prepared to Restart:** Don't hesitate to discard code and begin anew if the agent veers off track.
LLM-driven agents can get stuck in a rut and not be able to work themselves of bad situation.

* **Always Review Code:** This is paramount, as agents can hallucinate, duplicate code, or misinterpret instructions.
Adopt a "trust but verify" approach, ensuring a human remains responsible for every change.

**Practical Applications and Future Outlook**

AI coding agents are proving valuable across various software development scenarios.
Some of the more successful tasks that AI coding agents like OpenHands can often perform fairly well include:

* Resolving merge conflicts
* Addressing pull request feedback
* Fixing minor bugs
* Making small infrastructure changes (e.g., Terraform, Helm)
* Performing database migrations
* Fixing and expanding test coverage
* Building small new applications from scratch

At the end of the presentation, the presenters fielded a number of questions that provided a great deal of more useful information.
Some of the more interesting questions and answers include:

* **Q:** How to keep agents within organizational context (e.g., avoiding GPL licenses)?

  * **A:** Code review is the primary safeguard.
  OpenHands' "micro agents" can be customized to guide the agent (e.g., "never use GPL dependencies"), but CI/CD checks are still essential.

* **Q:** Do all AI coding agents use runtime sandboxing?

  * **A:** It's mixed.
  First-generation agents often run directly on the user's machine with frequent prompts for permission to run each command.
  Newer agents like OpenHands aim for more autonomous operation within sandboxes.

* **Q:** How does OpenHands perform on benchmarks like Commit0?

  * **A:** SWE-Bench is the current "golden benchmark."
  OpenHands is near the top for open-source models.
  However, SWE-Bench is becoming gamed, so they are diversifying benchmarks (e.g., MultiSWE-Bench, Commit0) to ensure real-world improvement.

* **Q:** How does OpenHands handle cross-session memory and learnings?

  * **A:** Memory is stored as code in a Git repository under user control, primarily through "micro agents" at repository, organization, or user levels.
  This allows for explicit control and sharing of context.

* **Q:** Are there plans for OpenHands in VS Code or IntelliJ?

  * **A:** A CLI was recently shipped.
  The plan is to integrate this CLI into VS Code to allow local development and context sharing from the IDE.

* **Q:** Are there plans for OpenHands to automatically review PRs?

  * **A:** It's possible today by prompting the agent.
  They are looking to make it a more first-class feature, potentially with a read-only mode for reviews.

* **Q:** What about better Windows development support (WSL)?

  * **A:** They are working on it, but it's challenging.
  OpenHands Cloud is an alternative.
  Contributions for Windows support are welcome.

* **Q:** Which LLM models work best with OpenHands?

  * **A:** Claude 4 is a great default (though expensive and closed-source).
  [Devstral](https://mistral.ai/news/devstral) is a good open-source alternative, about two-thirds as good as Claude 4, suitable for smaller/easier tasks.

* **Q:** Is there a noticeable difference between coding-specific models (e.g., Codex, Devstral) and general-purpose models (e.g., GPT-3, Claude 4) for coding tasks?

  * **A:** Generalist models like Claude 4, with strong reasoning and coding capabilities, often outperform coding-specific models in terms of quality.
  Coding-specific models are usually smaller and cheaper, offering efficiency benefits for certain tasks.

The webinar wrapped up by teasing future sessions and promising continued insights into the development and usage of AI coding agents.

<!---
Publish: yes
RSS update: 2025-07-28
Topics: documentation, development tools, refactoring, testing, peer code review
Pinned: no
--->
