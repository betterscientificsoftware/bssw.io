# Building an Online Learning Toolkit for Git, GitHub, and High-Performance Computing

#### Contributed by [Jasmine Buckley-Williams](https://github.com/jbuckleywilliams)


Technology is evolving rapidly, and students entering computer science, data science, and
engineering fields are expected to understand far more than just programming fundamentals.
Today's learners must also understand version control, collaborative software development,
parallel programming, and performance optimization. To help bridge that gap, I developed an
interactive online learning toolkit focused on Git, GitHub, and High-Performance Computing
(HPC).

This project was designed as both a technical resource and an educational platform that
introduces beginners to industry-relevant computing concepts through tutorials, exercises, and
hands-on examples. The goal was to create a structured environment where learners can
explore foundational programming workflows while gradually progressing into advanced topics
such as MPI, OpenMP, optimization strategies, and performance analysis.

## Why I Created the Toolkit

One challenge many students face when learning technical concepts is the disconnect between
theory and practical application. Topics like Git branching, parallel computing, profiling tools, or
compiler optimization flags can feel overwhelming when presented only through documentation
or lectures.

This toolkit was created to simplify those learning barriers by organizing content into
beginner-friendly sections with:
- Guided tutorials
- Step-by-step coding examples
- Interactive exercises
- Glossary definitions
- Real-world HPC workflows
- GitHub collaboration examples
- Performance optimization concepts

The website combines software engineering practices with computational science concepts so
learners can understand not only how systems work, but also how professional development
workflows are structured in research and industry environments.

## Website Structure and Learning Content

The toolkit website is divided into several learning modules that progressively build technical
knowledge.

### Git & GitHub Fundamentals

The Git and GitHub section introduces learners to version control and collaborative
development workflows. Topics include:
- Git vs. GitHub
- Creating repositories
- Cloning repositories
- Branching and merging
- Pull requests
- Merge conflict resolution
- GitHub Pages
- GitHub Actions automation

Students practice essential commands such as:
```
git init
git add .
git commit -m "Initial commit"
git push origin main
```

The tutorials also explain collaborative workflows commonly used in software engineering
teams, including feature branching and pull request reviews.

### High-Performance Computing (HPC)

The HPC portion of the website introduces learners to computational science concepts used in
research laboratories, data centers, and supercomputing environments.

Topics include:
- Parallel computing fundamentals
- MPI programming
- OpenMP threading
- Hybrid MPI + OpenMP models
- Scalability
- Performance tuning
- Profiling and optimization
- Memory hierarchy and cache efficiency

Students learn how distributed systems divide workloads across processors and how
performance bottlenecks impact scalability.

Example OpenMP code used in the tutorials:
```
#pragma omp parallel for reduction(+:sum)
for (int i = 0; i < N; i++) {
sum += A[i];
}
```

The website also explains key HPC concepts such as:
- Strong scaling
- Weak scaling
- Amdahl's Law
- Roofline analysis
- Arithmetic intensity
- Vectorization
- NUMA optimization

## Hands-On Practice Material

One of the core goals of the toolkit is experiential learning. Instead of only reading concepts,
learners complete structured exercises that simulate real-world workflows.

Exercises include:
- Git collaboration practice
- MPI “Hello World” programs
- OpenMP threading exercises
- Hybrid parallel programming challenges
- Performance tuning experiments
- Profiling and debugging activities
- HPC simulation mini-projects

These activities reinforce problem-solving skills while exposing students to tools commonly used
in scientific computing and enterprise software development.

## Building the Website

The website itself was developed using:
- HTML5
- CSS3
- Visual Code Studio
- Git version control

The site structure was intentionally designed to remain lightweight and easy for beginners to
understand. Each tutorial exists on its own HTML page to help students learn how multi-page
websites are organized and linked together.

The project also demonstrates practical web development concepts including:
- Navigation menus
- Dropdown navigation
- Responsive layouts
- External stylesheets
- Semantic HTML structure
- Code formatting with <pre> and <code> blocks

By building the site manually rather than relying entirely on templates, I was able to better
understand how front-end systems are organized and deployed.

## Challenges During Development

One major challenge during development involved Git repository management and
synchronization between local and remote repositories. While working on the site, I
encountered:
- Merge conflicts
- Non-fast-forward push errors
- Deleted file recovery
- Workflow restoration
- GitHub Pages deployment issues

These challenges ultimately became learning opportunities and helped strengthen my
understanding of Git troubleshooting, repository recovery, and collaborative version control
practices.

Another challenge was organizing advanced HPC concepts in a way that remained accessible
to beginners while still being technically accurate. This required balancing simplified
explanations with real-world examples and mathematical models.

### Educational Goals and Future Expansion

The long-term goal of this toolkit is to provide students with an accessible introduction to both
software engineering workflows and computational science techniques.

Future additions may include:
- Interactive coding sandboxes
- Parallel debugging tutorials
- GPU programming with CUDA
- MLflow and reproducible machine learning pipelines
- Data visualization dashboards
- Containerization with Docker and Singularity
- SLURM job scheduling walkthroughs
- Research reproducibility workflows

The toolkit is intended to continue evolving as both an educational resource and a
demonstration of applied technical skills.

## Conclusion

Building this online learning toolkit has been both a technical and educational experience. It
combines concepts from web development, software engineering, parallel computing, and
performance optimization into a single learning platform designed to support beginners and
intermediate learners alike.

More importantly, the project demonstrates how modern computing increasingly depends on
interdisciplinary knowledge, blending collaboration tools like GitHub with scalable computational
techniques used in high-performance systems.

As technology continues advancing, understanding both collaborative development and
computational performance will remain essential skills for future engineers, analysts, and
researchers.

## Author bios
[Jasmine Buckley-Williams](https://github.com/jbuckleywilliams) is a [2025 BSSw Fellow](https://bssw.io/blog_posts/introducing-the-2025-bssw-fellows) and a Public Utilities Regulatory Analyst with a Master's Big Data Analytics. She has a background in data manipulation and management in utilities enforcement. Her work bridges the gap between technical excellence and practical accessibility, ensuring that HPC best practices are not only understood but also effectively applied in real-world scientific computing environments.


<!---
Publish:
Track: bssw fellowship
Topics:
OpenGraph image:
--->
