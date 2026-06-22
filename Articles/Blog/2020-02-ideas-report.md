# Spreading Ideas about Better Scientific Software

**Hero Image:**

 - <img src='../../images/Blog_0225_Computational.jpg' />

#### Contributed by [David E. Bernholdt](https://github.com/bernhold "David Bernholdt GitHub Profile")

#### Publication date: February 28, 2020

A recently released report describes how the IDEAS-ECP project, a part of the U.S. Exascale Computing Project ([ECP](https://exascaleproject.org)), approaches its work of fostering and advancing software productivity and sustainability for extreme-scale computational science. 

Scientific computing on HPC systems is not easy. Add the challenges of the increasing diversity and rapid pace of change in computer architectures that the community is currently facing, and it gets a good deal harder. And then when we, as a community, have managed to deal with that and get some good computational science done, the expectations just seem to ratchet up. The simulations need to include more physics (coupling), with higher fidelity, on larger systems, also increasingly incorporating data analytics. And because of these increased simulation challenges, we need to use the latest *bleeding*-edge hardware to reach the next level of scientific goals. This is the situation faced by many in the community, but it is particularly true within ECP.

The [IDEAS Productivity project](https://ideas-productivity.org/), of which I am a member, began in 2014 sponsored by a partnership between the Offices of Advanced Scientific Computing Research and Biological and Environmental Research within the U.S. Department of Energy Office of Science. The project expanded in 2017 with support from the ECP to help software developers address the challenges inherent in the exascale effort. The IDEAS-ECP team recently released a [report](https://doi.org/10.2172/1606662) that catalogs many of their contributions to date and describes their approach to helping ECP (and other) code teams improve software productivity and sustainability. While I encourage you to read the report, I'll summarize the IDEAS approach briefly here.

## Curating methodologies to improve software practices of individuals and teams

Understanding best practices in software development is fundamental to being able to help improve them.  We develop, customize, curate, and disseminate these best practices. While the software development industry has many best practices to offer, scientific software development differs in important ways, so such practices often have to be tailored to the needs of the high-performance computational science community. To aid this process, we are gathering and distilling the collective understanding of scientific software development teams. 

## Incrementally and iteratively upgrading software practices

One of the differences in scientific software development is that, by and large, research projects are funded to generate scientific results — often, for the sponsors, the software is just a byproduct. Consequently, scientific software teams spend most of their coding effort developing new capabilities to enable new science. Thus, efforts to improve software development processes in this community need to be incremental, easily integrated alongside the team's primary feature development efforts, and showing benefits fairly quickly. Recognizing this situation, we have developed a simple, lightweight process for [Productivity and Sustainability Improvement Planning](https://bssw.io/psip) (PSIP), which can help teams set goals for software process improvements, implement them, and evaluate and track their success. The PSIP process has become a primary tool for our direct engagements with code teams.  And the approach is equally applicable outside of the ECP context.

## Establishing software communities

To support the needs of exascale applications, the ECP ecosystem also includes a wide range of tools, libraries, programming models, and performance portablity frameworks that are being developed and enhanced for exascale. Based on experience in the original "IDEAS-Classic" project, we are helping ECP Software Technology teams design a collection of Software Development Kits (SDKs). Organized "horizontally" (i.e., slices of qualitatively similar functionality), SDKs promote software communities that can develop and implement common policies to ensure that the software components within an SDK provide the compatibility, testing, and wide deployment necessary to support the needs of the ECP applications, as described in a recent [blog post](https://bssw.io/blog_posts/building-community-through-software-policies).

## Engaging in community outreach

In the IDEAS project, we've always recognized that we cannot change the world on our own. And that's why, from its inception, IDEAS has made community outreach a prominent feature of our approach. Our goal is to create a "virtuous cycle" in which widespread awareness of the importance of software quality and related issues within the HPC computational science and engineering community, including the Exascale Computing Project, in turn promotes sharing, discussion, and refinement of practices and resources for producing better scientific software for the benefit of the ECP as well as the broader community.  Our contributions to the community take many forms. We work with people from like-minded organizations to create opportunities for technical discussions focused on the experience of software development, including minisymposia, thematic poster groups, and birds-of-a-feather sessions. We've been delivering tutorials on Better Scientific Software at major conferences and other venues for some years now. Since 2016, we've organized the [Best Practices for HPC Software Developers](https://bssw.io/items/best-practices-for-hpc-software-developers-webinar-series) webinar series. Recognizing that there's a lot of information on software practices "out there" already but that it can be hard to know what's useful for scientific software, we launched this web site (https://bssw.io). And we've also established the [Better Scientific Software Fellowship Program](https://bssw.io/fellowship) to help grow the community of leaders in scientific software productivity and sustainability.

## We are not alone

The IDEAS-ECP project participates in, and helps grow, a larger community of practice around the idea of high-quality. Many of these groups have been described in a recent [paper](https://bssw.io/items/exploring-community-organizations-and-their-role-in-emerging-software-ecosystems) and also featured in the BSSw blog, such as the [US-RSE Association](https://bssw.io/blog_posts/us-research-software-engineer-us-rse-association), [MolSSI](https://bssw.io/blog_posts/software-sustainability-in-the-molecular-sciences), and [URSSI](https://bssw.io/blog_posts/urssi-conceptualizing-a-us-research-software-sustainability-institute). We feel that this activity is important for a number of reasons. First and foremost, as with our own efforts to organize technical events around software development, the more people and organizations who are talking about scientific software development, the better it is for awareness within the larger community. Second, the members of this community have different audiences and different stakeholders and come at issues from a variety of approaches. Together, we are building a rich, diverse, and vibrant community.

## Author bio

David E. Bernholdt is the Outreach Lead for the IDEAS-ECP project. He is a Distinguished R&D Staff Member and Group Leader at Oak Ridge National Laboratory (ORNL). He has leadership roles in multiple projects in the DOE Exascale Computing Project (ECP) and the Scientific Discovery through Advanced Computing (SciDAC) program. He also leads the Programming Environment and Tools area of the Oak Ridge Leadership Computing Facility (OLCF). His research interests center on making it easier and more productive to create and use computational science and engineering software on the largest high-performance computer systems.

<!---
Publish: yes
Track: community
RSS update: 2020-02-28
Categories: Planning, Collaboration
Topics: Software Engineering, Projects and Organizations
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
