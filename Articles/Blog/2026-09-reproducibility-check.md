# Using Local AI to Support Reproducibility and Sustainability in Scientific Software

#### Contributed by [Suzan Anwar](https://github.com/szuananwar)

#### Publication date: September 25, 2026

<!-- begin deck -->
Local large language models can help identify common reproducibility and sustainability gaps in scientific software repositories when paired with a structured rubric and careful human review.
<!-- end deck -->

In computational science, artificial intelligence is often discussed in terms of new capabilities and accelerated discovery. At the same time, the growing use of AI introduces new challenges for software reliability, sustainability, and reproducibility. Complex dependency stacks, evolving frameworks, specialized hardware, and increasingly automated workflows can make scientific software difficult to reproduce across users, systems, and computing environments.

Rather than creating entirely new evaluation approaches, we can build on existing frameworks such as the [Open Source Security Foundation (OpenSSF) Best Practices Badge](https://openssf.org/projects/best-practices-badge/) and [Scorecard](https://openssf.org/projects/scorecard/). These frameworks provide useful guidance for assessing software quality. Many practices promoted by OpenSSF, including dependency management, testing, documentation, and build verification, also contribute directly to software reliability and reproducibility. In scientific computing and HPC environments, failures in these areas can prevent researchers from reproducing results or deploying software successfully.

To explore how AI might complement established assessment practices, I developed **ReproPilot**, a research prototype that combines transparent deterministic repository assessment, artifact-quality analysis, and optional grounded local AI using [Ollama](https://ollama.com/). The goal is not to replace human evaluation or use AI to determine a repository's reproducibility score. Instead, deterministic evidence remains authoritative, while AI is used only to help prioritize or explain verified reproducibility gaps.

## Designing for the machine: The weighted rubric and OpenSSF

While developing the evaluation rubric, I compared it with existing approaches such as the OpenSSF Best Practices Badge and Scorecard. Several core criteria overlap, including documentation, testing, dependency management, and licensing.

The current prototype uses the following indicator-based rubric to guide repository assessments:

| Category | Example evidence | Points |
| :--- | :--- | ---: |
| Documentation | `README.md`, `README.rst` | 15 |
| Dependencies | `requirements.txt`, `pyproject.toml` | 15 |
| Environment | `environment.yml`, lock files | 10 |
| HPC Software Stack | `spack.yaml`, BuildTest configuration | 10 |
| Testing | `tests/`, `pytest.ini`, `tox.ini` | 15 |
| Containers | `Dockerfile`, `Containerfile`, `apptainer.def` | 15 |
| Experiment and Provenance Tracking | `MLproject`, `dvc.yaml`, `params.yaml`, provenance metadata | 10 |
| Licensing | `LICENSE`, `LICENSE.md`, `COPYING` | 10 |
| **Total** | | **100** |

The weights are explicit methodological choices rather than universal measures of reproducibility. Different scientific communities may reasonably prioritize different evidence.

While there is significant overlap between this rubric and the OpenSSF Best Practices Badge and Scorecard, the goals differ. OpenSSF primarily focuses on software engineering and security practices that improve software quality, maintainability, and trustworthiness. ReproPilot instead focuses on repository evidence associated with **reproducibility readiness** in scientific software, including concerns specific to AI and HPC workflows.

For example, environment specifications, container recipes, experiment provenance, and HPC software-stack information can be especially important when attempting to reconstruct a scientific workflow. Rather than competing with OpenSSF, these approaches are complementary: general software-engineering practices provide an important foundation, while scientific reproducibility requires additional evidence about environments, experiments, data, models, and computing infrastructure.

## The prototype in early experiments and its limits

ReproPilot combines deterministic artifact discovery with quality-aware analysis and optional grounded local AI.

The deterministic component identifies reproducibility-related repository evidence. The quality assessor then examines whether detected artifacts contain useful information; for example, whether a README includes meaningful installation and execution instructions, whether dependency information is sufficiently explicit, whether tests contain meaningful assertions, and whether provenance or HPC portability information is documented.

The optional AI component is deliberately constrained. It receives verified findings from the deterministic assessment and may prioritize or explain those findings, but it does not independently calculate or modify repository scores.

The current prototype was evaluated on **30 open-source scientific software repositories across five domains**: high-performance computing, artificial intelligence and machine learning, computational biology, climate and Earth science, and medical AI.

The evaluation found a moderate positive relationship between artifact presence and artifact quality (`r = 0.407`, `p = 0.0255`). The constrained AI experiment produced valid outputs for 28 of 30 repositories (93.3%). However, agreement between deterministic and AI-selected priorities was relatively low, including a top-1 agreement rate of 10.7%, a mean Jaccard similarity of 0.313, and a mean F1 agreement score of 0.426.

These results reinforce an important point: AI and deterministic assessment can provide complementary signals, but AI should not replace transparent, evidence-based assessment.

It is also important to recognize the boundary between **reproducibility readiness** and successful scientific reproduction. A repository may contain strong documentation, tests, containers, and provenance records without guaranteeing that a published result can be reproduced exactly.

Automated assessment cannot, by repository inspection alone, establish scientific correctness, numerical validity, dataset availability, hardware equivalence, or successful execution of an entire workflow. Evaluating the scientific validity of mathematical models, determining whether tests adequately represent domain-specific behavior, or judging whether computational results are scientifically correct still requires expert human review and, where feasible, runtime validation.

## Moving forward: Actionable recommendations for researchers

A few practices can significantly improve reproducibility and sustainability:

* Provide a minimum reproducibility package that includes clear execution instructions, dependency and environment information, and representative examples.
* Record experiment and model provenance, including relevant parameters, software versions, data or model versions, and source-code revisions.
* Use automated tests that contain meaningful scientific or numerical assertions rather than only checking whether software executes.
* Document HPC-specific requirements such as compilers, MPI implementations, accelerator software, scheduler assumptions, and resource requirements when applicable.
* Use AI assistants cautiously. AI can help explain or prioritize verified gaps, but AI-generated recommendations should be validated before they are adopted.

## Future directions

Future work will focus on refining the assessment methodology, expanding validation across scientific domains, and gathering community feedback.

Important directions include improving applicability-aware assessment, which accounts for whether a given artifact is relevant to a repository, so that repositories are not penalized for artifacts that are irrelevant to their workflows, expanding evaluation of continuous integration (CI) and scientific-validation practices, and continuing to study artifact quality in addition to artifact presence.

The local-AI component will also be evaluated with alternative model configurations. The current fellowship prototype and benchmark use `gemma3:1b` through Ollama as a **reference model**, not as a universal requirement. Other Ollama-hosted models may be explored, but model substitutions should be treated as separate experimental configurations because generated priorities and explanations may vary.

The long-term goal is to explore how local AI tools can support, not replace, human efforts to improve the reliability, sustainability, and reproducibility of scientific software.

## Prototype availability

The ReproPilot prototype and documentation discussed in this article are available on GitHub:

[https://github.com/szuananwar/ai-assisted-reproducibility-bssw/tree/main/examples/repropilot](https://github.com/szuananwar/ai-assisted-reproducibility-bssw/tree/main/examples/repropilot)

ReproPilot is a research prototype developed within the broader 2026 Better Scientific Software Fellowship project on **AI-Assisted Reproducibility in Scientific Software**. It combines deterministic repository evidence, artifact-quality assessment, optional grounded local AI prioritization, benchmark analysis, and reproducibility reporting.

The deterministic assessment can be used independently of the local AI component. For users who wish to explore grounded AI prioritization, the project documents optional Ollama setup and uses `gemma3:1b` as the current reference model.

I welcome feedback, discussion, and collaboration from the scientific computing community to help refine the assessment categories, weighting choices, artifact-quality criteria, and broader methodology. If you would like to test the prototype, suggest modifications, report a limitation, or share insights from your own workflows, please reach out by opening an issue. You can also start a thread on the project's [GitHub Discussions page](https://github.com/szuananwar/ai-assisted-reproducibility-bssw/discussions).

## Author bio

Suzan Anwar is department chair and assistant professor of computer science at Philander Smith University. She holds a Ph.D. in Computer and Information Science from the University of Arkansas at Little Rock. Her research focuses on machine learning, cybersecurity, computer vision, and scientific software reproducibility. Dr. Anwar has served as a visiting faculty researcher at Lawrence Berkeley National Laboratory, Argonne National Laboratory, and Oak Ridge National Laboratory through the Sustainable Research Pathways. She is a 2026 Better Scientific Software (BSSw) Fellowship awardee, where her project explores local, AI-assisted tools to improve the sustainability, reliability, and reproducibility of scientific computational workflows.

<!---
Publish: yes
Track: deep dive, bssw fellowship
Pinned: no
Topics: reproducibility, software sustainability, ai for better development
--->
