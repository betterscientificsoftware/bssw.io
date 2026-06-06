# Documentation Is the Interface

#### Contributed by [Vicente Bolea](https://github.com/vicentebolea), [Jaswant Panchumarti](https://github.com/jspanchu), [Berk Geveci](https://www.kitware.com/berk-geveci/), [Will Schroeder](https://www.kitware.com/will-schroeder/), and [Patrick O'Leary](https://www.kitware.com/patrick-oleary/)

#### Publication date: June 6, 2026

<!-- begin deck -->
Scientific software documentation now has a second audience: AI systems that use it to explain software behavior, generate code, and help users reach complex APIs.
As users interact with software through AI, documentation becomes part of the software's interface.
<!-- end deck -->

## Opening problem

*Scientific software is powerful, but it still depends on documentation to make that power usable.*

Documentation has always been part of what makes scientific software usable.
VTK may offer a rich set of algorithms, data structures, and rendering components, but users still need help understanding how those pieces work together in practice.
Documentation has traditionally supplied that missing layer by explaining concepts, walking through workflows, and connecting APIs to real applications.<sup>[1]</sup>

That role remains.
The difference now is that documentation has a second audience.

## What changed

*Documentation no longer serves only human readers; it also serves AI systems that use it to explain software and generate code.*

What is new is not documentation itself, but who and what is consuming it.
AI systems now work from the same API pages, guides, tutorials, and examples that human users rely on.
They use that material to answer questions, explain software behavior, and help generate code.
Once that happens, documentation stops being just explanatory material.
It starts becoming part of the way the software is accessed and used.

## How AI uses documentation

*AI systems consume documentation in several ways, including model adaptation, retrieval, structured tool access, and code generation.*

AI can use documentation in several ways.
We usually cannot tell from public information whether a general-purpose model such as ChatGPT was trained on a specific documentation set like VTK, even though OpenAI says its models draw on a mix of public, licensed, synthetic, and human-generated data.<sup>[2]</sup>
But developers can still build smaller domain models from curated documentation, tutorials, examples, and API descriptions.

They can also bring documentation into the loop at runtime.
Retrieval can supply relevant passages and examples when a user asks a question, while tool interfaces such as MCP can expose structured software knowledge more directly.<sup>[3],[4],[5]</sup>
In code generation, those pieces often work together: a model produces the response, retrieval supplies context, and tools expose structure.<sup>[6]</sup>
For VTK, that only works well when the documentation makes roles, relationships, inputs, outputs, and common usage patterns explicit.

## Why that matters

*AI systems do not read documentation the way people do, so documentation now needs to make its structure and relationships explicit.*

AI systems do not use documentation the way people do.
A person can read a page from beginning to end, follow an explanation across links, and supply missing context from prior experience.
AI systems typically operate within a constructed context composed of retrieved passages, examples, and structured metadata.
Retrieval and ranking systems select that material, and the model then matches patterns between the prompt and the supplied context to predict a response.
It does not absorb the documentation as a continuous argument.
It works over selected fragments and inferred relationships.
That means documentation now has to do more than read well.
It also has to state concepts, relationships, and common usage patterns clearly enough for software systems to use them.

In VTK, that difference shows up quickly.
If the documentation clearly says what a class does, what kind of object it is, what it takes as input, what it produces, and where it fits in the visualization pipeline, AI-assisted tools have a much better chance of producing something useful.
If that information is scattered, left implicit, or described inconsistently, the answer may still sound convincing while getting important details wrong.

## What to do differently

*Keep the website for people, but add a structured documentation layer that machines can use directly.*

Traditional documentation websites are still the right place for people to learn.
That is where users browse, follow links, compare examples, and slowly build a mental model of how a system works.
For VTK, that kind of exploration still matters.
People need explanations, examples, tutorials, and enough context to understand not just an API call, but how the larger visualization pipeline fits together.

AI systems need some of that same information, but they do better when it is exposed more directly.
Instead of leaving everything buried in prose, projects can add a structured layer that software can parse and use more reliably.
In practice, that might mean JSON or JSONL records that spell out class roles, parameters, relationships, example usage, and pipeline behavior.
The website is still where people learn.
The structured layer helps machines work with the same knowledge without having to infer quite so much from scattered pages.

That shift also changes how it makes sense to build documentation.
Rather than writing pages first and trying to pull structure out of them later, it may be better to make structure part of the system from the beginning.
Some of that structure can come straight from the software through introspection: class names, inheritance, method signatures, and docstrings.
An ontology can add another layer by defining the categories and relationships that make those facts useful.<sup>[7],[8]</sup>
Human experts then handle the smaller, higher-value part of the work: validating the model, curating the mappings, and fixing where automation falls short.
The result is not two separate documentation systems.
It is a documentation system that serves people through the website and AI through a structured knowledge layer.

The practical takeaway is pretty simple.
Most projects do not need a massive overhaul of AI documentation.
However, a few habits suddenly matter even more than they used to.
**Clear structure matters.**
**Consistent terminology matters.**
**Self-contained pages matter.**
**Good examples matter.**
**Machine-readable metadata matters.**
Those were already signs of good documentation.
Now they also shape how well AI can work with the software.

## Final takeaway

*As users work through AI and AI works through documentation, documentation becomes part of the software's interface.*

More and more people will come to software through AI rather than through source code, manuals, or search results alone.
When that happens, the AI still needs some way to figure out what the software does, how its pieces fit together, and what patterns of use actually make sense.
In many cases, that path runs straight through the documentation.

That is the bigger shift.
Documentation is no longer just supporting material.
It is becoming part of how software is actually used.

**As users interact with software through AI, and the AI itself relies on documentation to understand APIs, relationships, and usage patterns, the documentation becomes a new computational interface to the software itself.**

## Author bios

[Will Schroeder](https://www.kitware.com/will-schroeder/), Ph.D., is a co-founder of Kitware and served as its CEO for 19 years.
His role is to identify technology and business opportunities and obtain the necessary support for Kitware to meet these opportunities.
Will also provides technical leadership in large open source projects such as the National Library of Medicine Insight Toolkit (ITK) project, the NA-MIC NIH National Center for Biomedical Computing, and the Visualization Toolkit (VTK), where he is a lead developer and the first author of the VTK textbook.

[Jaswant Panchumarti](https://github.com/jspanchu) is a graduate student at RPI and a Senior R&D Engineer at Kitware.
He is leading the VTK WebAssembly effort at Kitware.
His research topic addresses detecting shocks in hypersonic flows with neural networks.

[Berk Geveci](https://www.kitware.com/berk-geveci/) leads the scientific visualization and informatics teams at Kitware Inc.
He is one of the leading developers of the ParaView visualization application and the Visualization Toolkit (VTK).
His research interests include large scale parallel computing, computational dynamics, finite elements, and visualization algorithms.
Dr. Geveci regularly publishes and teaches courses at conferences including IEEE Visualization and Supercomputing conferences.

[Vicente Bolea](https://github.com/vicentebolea) is a senior R&D engineer at Kitware Inc.
He is a core developer in VTK and its ecosystem, ParaView, Viskores, and ADIOS2, and is a regular contributor in other projects within the DAV and Tools integration initiative.
He has a strong interest in open source solutions, system programming, software sustainability, and high-performance computing.

[Patrick O'Leary](https://www.kitware.com/patrick-oleary/) is the Assistant Director of Scientific Computing for Kitware, Inc.
Dr. O'Leary's research interests include high performance computing (HPC), numerical analysis, finite elements, and visualization.

<!---
Publish: no
Track: Deep Dive
Pinned: no
Topics: documentation, software engineering, development tools
--->

<!--- References --->

[vtk-docs-sfer-ezikiw]: https://vtk.org/ "VTK Documentation {Kitware and the VTK Community. VTK Documentation. Accessed April 20, 2026.}"
[openai-model-development-sfer-ezikiw]: https://help.openai.com/en/articles/7842364-how-chatgpt-and-our-foundation-models-are-developed "How ChatGPT and Our Foundation Models Are Developed {OpenAI. How ChatGPT and Our Foundation Models Are Developed. Help Center. Accessed April 20, 2026.}"
[rag-sfer-ezikiw]: https://dl.acm.org/doi/10.5555/3495724.3496517 "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks {Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kuttler, Mike Lewis, Wen-tau Yih, Tim Rocktaschel, Sebastian Riedel, and Douwe Kiela. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. In Advances in Neural Information Processing Systems 33 (NeurIPS, 2020), 9459-9474, 2020.}"
[anthropic-mcp-sfer-ezikiw]: https://www.anthropic.com/news/model-context-protocol "Introducing the Model Context Protocol {Anthropic. Introducing the Model Context Protocol. Anthropic, November 25, 2024.}"
[mcp-spec-sfer-ezikiw]: https://modelcontextprotocol.io/specification/2025-11-25 "Model Context Protocol Specification {Model Context Protocol. Specification. Accessed April 20, 2026.}"
[program-synthesis-sfer-ezikiw]: https://arxiv.org/abs/2108.07732 "Program Synthesis with Large Language Models {Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. Program Synthesis with Large Language Models. arXiv, 2021.}"
[ontology-spec-sfer-ezikiw]: https://tomgruber.org/writing/ontolingua-kaj-1993.pdf "A Translation Approach to Portable Ontology Specifications {Thomas R. Gruber. A Translation Approach to Portable Ontology Specifications. Knowledge Acquisition 5, no. 2 (1993): 199-220.}"
[knowledge-graphs-sfer-ezikiw]: https://doi.org/10.1145/3447772 "Knowledge Graphs {Aidan Hogan, Eva Blomqvist, Michael Cochez, Claudia D'Amato, Gerard de Melo, Claudio Gutierrez, Sabrina Kirrane, Jose Emilio Labra Gayo, Roberto Navigli, Sebastian Neumaier, Axel-Cyrille Ngonga Ngomo, Axel Polleres, Sabbir M. Rashid, Anisa Rula, Lukas Schmelzeisen, Juan Sequeda, Steffen Staab, and Antoine Zimmermann. Knowledge Graphs. ACM Computing Surveys 54, no. 4 (2021): 1-37.}"
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "VTK Documentation"
[2]: #sfer-ezikiw-2 "How ChatGPT and Our Foundation Models Are Developed"
[3]: #sfer-ezikiw-3 "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
[4]: #sfer-ezikiw-4 "Introducing the Model Context Protocol"
[5]: #sfer-ezikiw-5 "Model Context Protocol Specification"
[6]: #sfer-ezikiw-6 "Program Synthesis with Large Language Models"
[7]: #sfer-ezikiw-7 "A Translation Approach to Portable Ontology Specifications"
[8]: #sfer-ezikiw-8 "Knowledge Graphs"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[VTK Documentation<br>Kitware and the VTK Community. VTK Documentation. Accessed April 20, 2026.](https://vtk.org/)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[How ChatGPT and Our Foundation Models Are Developed<br>OpenAI. How ChatGPT and Our Foundation Models Are Developed. Help Center. Accessed April 20, 2026.](https://help.openai.com/en/articles/7842364-how-chatgpt-and-our-foundation-models-are-developed)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks<br>Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Kuttler, Mike Lewis, Wen-tau Yih, Tim Rocktaschel, Sebastian Riedel, and Douwe Kiela. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. In Advances in Neural Information Processing Systems 33 (NeurIPS, 2020), 9459-9474, 2020.](https://dl.acm.org/doi/10.5555/3495724.3496517)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[Introducing the Model Context Protocol<br>Anthropic. Introducing the Model Context Protocol. Anthropic, November 25, 2024.](https://www.anthropic.com/news/model-context-protocol)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[Model Context Protocol Specification<br>Model Context Protocol. Specification. Accessed April 20, 2026.](https://modelcontextprotocol.io/specification/2025-11-25)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[Program Synthesis with Large Language Models<br>Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, and Charles Sutton. Program Synthesis with Large Language Models. arXiv, 2021.](https://arxiv.org/abs/2108.07732)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[A Translation Approach to Portable Ontology Specifications<br>Thomas R. Gruber. A Translation Approach to Portable Ontology Specifications. Knowledge Acquisition 5, no. 2 (1993): 199-220.](https://tomgruber.org/writing/ontolingua-kaj-1993.pdf)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[Knowledge Graphs<br>Aidan Hogan, Eva Blomqvist, Michael Cochez, Claudia D'Amato, Gerard de Melo, Claudio Gutierrez, Sabrina Kirrane, Jose Emilio Labra Gayo, Roberto Navigli, Sebastian Neumaier, Axel-Cyrille Ngonga Ngomo, Axel Polleres, Sabbir M. Rashid, Anisa Rula, Lukas Schmelzeisen, Juan Sequeda, Steffen Staab, and Antoine Zimmermann. Knowledge Graphs. ACM Computing Surveys 54, no. 4 (2021): 1-37.](https://doi.org/10.1145/3447772)
