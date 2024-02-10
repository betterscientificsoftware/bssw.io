# Come for Syntax, Stay for Speed, and Understand Bugs in Julia Programs

The Julia programming language is of increasing interest to scientific software developers.
Understanding the types of bugs observed in Julia programs can help developers identify, repair, or avoid them.

#### Contributed by [Akond Rahman](https://github.com/akondrahman "Akond Rahman's GitHub Profile")

#### Publication date: February 13, 2024 

In this article, I describe some of our [research findings](https://link.springer.com/article/10.1007/s10664-023-10328-5) related to bugs that occur in Julia programs.
Julia is becoming increasingly popular to implement scientific software.

Since its inception in 2012, Julia has experienced a steady increase in popularity as practitioners are migrating from scripting languages, such as Python.
Practitioners typically use Julia for large-scale scientific data analysis.
For example, Julia was used in [Celeste](https://cs.lbl.gov/news-media/news/2016/celeste-enhancements-create-new-opportunities-in-sky-surveys/), a software used in astronomy research.
Julia yielded a 1000x performance improvement for [Celeste](https://arxiv.org/abs/1611.03404), compared to the prior implementation.

But what about bugs in Julia programs? As with any other programming language, unmitigated bugs in Julia programs can hinder scientific exploration by generating erroneous results and unexpected failures. Hence, we pursued a research study where we systematically investigated a set of bugs collected from the open-source domain.

### Our approach

We studied 742 bugs via qualitative analysis. Using our qualitative analysis, we derived bug categories and bug symptoms for Julia programs. We also surveyed 52 practitioners who have contributed to open-source Julia programs for further insights. The datasets used in our paper are publicly available [online](https://figshare.com/s/35d775572bb840ebd392).  

### Major findings

<img src='../../images/julia-bugs-taxonomy.png' class='page lightbox' />[Categories of bugs identified in the study.]

In this study, we identified nine types of bugs.
Of these, three have not been reported in other types of software systems, namely, "polyglot," "pre-compilation," and "world age."
Polyglot defects relate to the incorrect use of Julia's interfaces to other programming languages.
Pre-compilation defects are due to incorrect use of Julia's pre-compilation and code caching capabilities.
World age defects are named for an analysis that Julia does to facilitate dynamic code loading and some program optimizations.

Common symptoms of bugs in Julia programs are program and build failures, incorrect calculations, and reduction in program execution speed.
Survey respondents find bugs related to data types to be the most common and most severe for Julia programs.

### What does it mean for practitioners working in the scientific software space?

Based on this study, we offer several suggestions and recommendations for toolsmiths and researchers using Julia.
First, we see ample opportunities for the development of tools to automatically detect and repair bugs in some of the categories we have identified, such as security and world age defects.
Second, developers should be encouraged to gain a better understanding of the unique characteristics of the Julia language and ecosystem and to follow Julia-related best practices in writing their code.
And finally, developers should facilitate the seamless integration of quality assurance throughout the Julia software ecosystem.

### Author bio

Akond Rahman is an assistant professor at Auburn University. His research interest is in software engineering focused on development and operations (DevOps) and secure software development. His motivation stems from the foundational challenge of integrating quality assurance into the development process without sacrificing developer productivity and software sustainability. His research is sponsored by the U.S. National Science Foundation (NSF) and the U.S. National Security Agency (NSA). He received his PhD from North Carolina State University. He won the Microsoft Open Source Challenge Award in 2016, the ACM SIGSOFT Doctoral Symposium Award at ICSE in 2018, and the ACM SIGSOFT Distinguished Paper Award at ICSE in 2019. He actively collaborates with practitioners from industry, such as GitHub and WindRiver. To learn more about his work visit <https://akondrahman.github.io/>.

<!---
Publish: yes
Topics: debugging, development tools, issue tracking, programming languages
Track: experience
--->
