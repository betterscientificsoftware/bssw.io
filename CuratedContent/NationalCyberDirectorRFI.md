# US Federal Government Effort to Champion Adoption of Memory Safe Languages
<!--deck text start-->
Does C++ have a future in OS3I?
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86 "Mark C. Miller GitHub Profile")
#### Publication date: December 1, 2023

Resource information | Details 
:--- | :--- 
Resource name | Request for Information on Open-Source Software Security: Areas of Long-Term Focus and Prioritization
Website | https://www.regulations.gov/document/ONCD-2023-0002-0001
Focus | US Federal Government RFI for Advancing Memory Safe Languages in Open Source Software

The [National Cybersecurity Strategy](https://www.whitehouse.gov/wp-content/uploads/2023/03/National-Cybersecurity-Strategy-2023.pdf) from the Office of the National Cyber Director (ONCD) has established an Open-Source Software Security Initiative (OS3I) to champion the adoption of memory safe programming languages (e.g. [Rust](https://foundation.rust-lang.org), [Go](https://go.dev), [Julia](https://julialang.org)) and open-source software security.

A recent [Request for Information (RFI)](https://www.regulations.gov/document/ONCD-2023-0002-0001) aimed at furthering the work of OS3I by identifying areas most appropriate to focus government priorities, and addressing critical questions was made.
112 organizations and individual experts responded to the RFI.
These included several DOE labs and a number of major commercial technology companies.

What does this mean for the future of C++?

[Todd Gamblin](https://github.com/tgamblin), an expert on the HPC software ecosystem as well as a studious observer of trends in commercial industry had these remarks about it.

> Commercial developers are shipping major products in these languages (Rust, Go, Julia to a lesser extent).
> The linux kernel is allowing contributions in Rust (and notably NOT in C++).
> Oxide computer just shipped an embedded OS written in Rust.
> crates.io has 130,000 packages.
> It’s a vibrant ecosystem, and people *are* choosing to do new projects in it *over*, most notably, C++.
> Go is real too.
> Kubernetes, Docker, and much of the cloud ecosystem is written in Go.
 
> All that being said, the DOE HPC community just spent 7 years developing [GPU computing](https://www.exascaleproject.org) capabilities — across 3 different GPU architectures.
> That represents a *huge* investment!
> And, we did that in, mostly, C++.
> It is worth noting that it was not the same old C++.
> It was C++11, 14, 17, and on.
> We’re talking about *modern* C++.
 
> It is fair to say that the GPU ecosystem in Rust and Go is seriously lacking in comparison, and I don't think the investment in C++ was misplaced.
> The GPU ecosystem has a lot of momentum from AI and games -- that is a lot of inertia to overcome.
> Julia has some integration, being a very compute-focused language.
> However, it remains to be seen if the community will build HPC codes in it...or, if it is as viable for performance portability as C++ has been.

> Whether the successor to C++, in scientific computing, if there is one, is going to be Julia, Rust, or Go is an open question.
> The answer depends strongly on what industry does and how well they can make fast, memory-safe alternatives to the algorithms and frameworks such as [RAJA](https://raja.readthedocs.io/en/develop/) or [Kokkos](https://kokkos.github.io) DOE has built in C++.
> Notably, we have yet to see any major Rust or Go AI framework emerging.
> They are all still Python + C++.
> A lot of developers are moving to Python + Rust instead of Python + C/C++, though.
> [py-cryptography](https://cryptography.io/en/latest/) and a number of other very significant packages in the ecosystem are doing that.
 
> A final point to keep in mind is that most HPC applications are not (yet) *services*.
> They don’t need the same security guarantees that a library that sits listening for input on a port from random users need.
> That’s good and bad.
> It is good because they are unlikely to be attacked in the same ways.
> And, because supply chain security for HPC applications can set different priorities.
> It is bad because it weakens the case for encouraging anyone to move to a memory safe language merely for the sake of security.

Visiters of the [RFI](https://www.regulations.gov/document/ONCD-2023-0002-0001) page will note about 100 *comments* are available there.
In some cases, *comments* are just that...very short remarks from specific individuals.
In most cases, an industry-leading organization has posted a lengthy response to the RFI as a PDF attachment.
Among the 100+ responses, there were these from...

* LBNL: https://www.regulations.gov/comment/ONCD-2023-0002-0019
* LLNL: https://www.regulations.gov/comment/ONCD-2023-0002-0080
* Rust Foundation: https://www.regulations.gov/comment/ONCD-2023-0002-0045
* OpenSSF: https://www.regulations.gov/comment/ONCD-2023-0002-0046 
* GitLab: https://www.regulations.gov/comment/ONCD-2023-0002-0044 
* HPE: https://www.regulations.gov/comment/ONCD-2023-0002-0029  
* IBM: https://www.regulations.gov/comment/ONCD-2023-0002-0077
* AWS: https://www.regulations.gov/comment/ONCD-2023-0002-0082
* Microsoft: https://www.regulations.gov/comment/ONCD-2023-0002-0019
* Google: https://www.regulations.gov/comment/ONCD-2023-0002-0074
* Consumer Reports: https://www.regulations.gov/comment/ONCD-2023-0002-0060

As a final note, [Bjarne Stroustrup](https://github.com/BjarneStroustrup), the creator of C++, [spoke recently](https://youtu.be/I8UvQKvOSSw?si=mSyWZzAkMOm5EnFR) at Cppcon-23 about bringing Safety to C++.
There is also a [summary](https://thenewstack.io/bjarne-stroustrups-plan-for-bringing-safety-to-c/) of his 1.5 hour presentation.

<!---
Publish: yes
Topics: Requirements, Software Engineering, Discussion and Question Sites
--->
