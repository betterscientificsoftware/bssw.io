# Using Local AI to Support Reproducibility and Sustainability in Scientific Software

#### Contributed by [Suzan Anwar](https://github.com/szuananwar)

#### Publication date: September 25, 2026

<!-- begin deck -->
Local large language models can help identify common reproducibility and sustainability gaps in scientific software repositories when paired with a structured rubric and careful human review.
<!-- end deck -->

In computational science, artificial intelligence is often discussed in terms of new capabilities and accelerated discovery. At the same time, the growing use of AI introduces new challenges for software reliability, sustainability, and reproducibility. Complex dependency stacks, evolving frameworks, and increasingly automated workflows can make scientific software difficult to reproduce across users, systems, and computing environments.

Rather than creating entirely new evaluation approaches, we can build on existing frameworks. Frameworks such as the [Open Source Security Foundation (OpenSSF) Best Practices Badge](https://openssf.org/projects/best-practices-badge/) and [Scorecard](https://openssf.org/projects/scorecard/) provide useful guidance for assessing software quality. Many practices promoted by OpenSSF, including dependency management, testing, and build verification, also contribute directly to software reliability and reproducibility. In scientific computing and HPC environments, failures in these areas can prevent researchers from reproducing results or deploying software successfully.

Traditional assessment frameworks often rely on manual review. To explore how AI might help support these efforts, I developed a prototype that uses a locally hosted LLM with [Ollama](https://ollama.com/) to assist with repository assessments. The goal is not to replace human evaluation, but to help identify common reproducibility and sustainability gaps early in the development process.

## Designing for the machine: The weighted rubric and OpenSSF

While developing this evaluation rubric, I compared it with existing approaches such as the OpenSSF Best Practices Badge and Scorecard. Several core criteria overlap, including documentation, testing, dependency management, and licensing.

The prototype uses the following rubric to guide repository assessments:

| Category | Targeted item or artifact | Points |
| :--- | :--- | :--- |
| Documentation | README with execution and run instructions | 15 |
| Dependencies | `requirements.txt` | 15 |
| Environment | `environment.yml` | 10 |
| HPC Environment | `spack.yaml` for system-level configurations | 10 |
| Testing | `tests/` folder or validation scripts | 15 |
| Containerization | Dockerfile or Apptainer specification | 15 |
| Experiment Tracking | MLflow logs, parameter sheets, or tracking files | 10 |
| Open Science | `LICENSE` file | 10 |
| **Total** | | **100** |

While there is significant overlap between this rubric and the OpenSSF Best Practices Badge and Scorecard, the goals are somewhat different. OpenSSF primarily focuses on software engineering and security best practices that improve software quality, maintainability, and trustworthiness. In contrast, this rubric focuses on reproducibility and sustainability concerns common in scientific computing and HPC environments.

As a result, it includes criteria such as HPC environment descriptions, containerization, and experiment tracking, which are particularly important for reproducing scientific results. Rather than competing with OpenSSF, the two approaches are complementary. OpenSSF helps assess general software quality and security practices, while this rubric focuses on additional requirements needed to support reproducible scientific research.

Documentation, dependency management, testing, and containerization receive the highest weights because they have the greatest impact on a user's ability to reproduce and reuse software. Other criteria, such as experiment tracking and HPC environment configuration, remain important but may not apply to every repository.

## The prototype in early experiments and its limits

To explore this approach, I developed a prototype reproducibility checker that combines a structured rubric with a locally hosted LLM.

In preliminary evaluations of open-source scientific repositories, the prototype frequently highlighted common reproducibility gaps, including missing environment specifications, limited testing information, and incomplete installation documentation. These preliminary observations suggest that AI-assisted assessments may help researchers identify opportunities for improvement before software is shared with collaborators or deployed on production systems.

It is critical, however, to recognize the boundary between this automated initial test and a thorough human assessment. While an LLM excels at verifying the *structural presence* of a file, confirming that a `tests/` folder or an explicit `requirements.txt` exists, it cannot verify semantic correctness or deeper scientific validity. For instance, the prototype can verify that a test suite is present, but it cannot determine whether those tests actually explore the core physical limits of an engine simulation or merely check trivial helper script functions.

During the rubric design phase, certain criteria were intentionally omitted because they are exceedingly difficult to automate without directly executing and verifying the software stack. Evaluating the underlying mathematical logic of data pipelines, analyzing scientific correctness, or judging the qualitative depth of code review comments are nuanced processes that still rely heavily on expert human peer review.

## Moving forward: Actionable recommendations for researchers

A few practices can significantly improve reproducibility and sustainability:

* Provide a minimum reproducibility package, including an explicit environment specification and example execution instructions.
* Adopt consistent repository structures so that users and automated tools can more easily locate source code, configuration files, and documentation.
* Use AI assistants cautiously. AI can help identify gaps and draft supporting materials, but researchers should always validate AI-generated recommendations before adopting them.

## Future directions

Future work will focus on refining the assessment process, improving rubric coverage across scientific domains, and gathering community feedback. The immediate priorities on the development checklist include expanding the rubric to evaluate automated continuous integration (CI) configuration files, such as GitHub Actions, and refining how the local LLM evaluates specialized metadata standards in open science. The long-term goal is to explore how local AI tools can support, not replace, human efforts to improve the reliability, sustainability, and reproducibility of scientific software.

## Prototype availability

The prototype implementation discussed in this article is available in the project's [sample workflow repository](https://github.com/szuananwar/ai-assisted-reproducibility-bssw/tree/main/examples/sample-ml-workflow).

The example demonstrates how a locally hosted LLM can be used to support reproducibility and sustainability assessments of scientific software repositories using a structured evaluation rubric. The implementation is intended as a proof of concept and a starting point for community discussion and future enhancements.

I welcome feedback, discussion, and collaboration from the scientific computing community to help refine these rubric categories and weighting schemes. If you would like to test the tool, suggest modifications to the scoring criteria, or share insights from your own workflows, please reach out by opening an issue on the project's [GitHub repository](https://github.com/szuananwar/ai-assisted-reproducibility-bssw).

## Author bio

Suzan Anwar is department chair and assistant professor of computer science at Philander Smith University. She holds a Ph.D. in Computer and Information Science from the University of Arkansas at Little Rock. Her research focuses on machine learning, cybersecurity, computer vision, and scientific software reproducibility. Dr. Anwar has served as a visiting faculty researcher at Lawrence Berkeley National Laboratory, Argonne National Laboratory, and Oak Ridge National Laboratory through the Sustainable Research Pathways. She is a 2026 Better Scientific Software (BSSw) Fellowship awardee, where her project explores local, AI-assisted tools to improve the sustainability, reliability, and reproducibility of scientific computational workflows.

<!---
Publish: yes
Track: experience
Pinned: no
Topics: reproducibility, software sustainability, ai for better development
--->
