From ChatGPT...

Yes, there are several steps that can be taken to preserve the software engineering know-how from a research software project when its funding is cut. Here are some recommendations:

1. Document the project: Create comprehensive documentation that captures the project's objectives, methodologies, and key findings. Include installation instructions, configuration details, and usage examples. Document any design decisions, algorithms, and implementation details that may be valuable to others.

2. Open-source the code: If the project's codebase is not already open source, consider releasing it under an open-source license. Platforms like GitHub, GitLab, and Bitbucket provide infrastructure for hosting and managing open-source projects. By making the code open source, you allow others to access, use, and contribute to the software.

3. Establish a community presence: Create a dedicated website, forum, or mailing list where users and developers can interact and discuss the project. Encourage community participation, answer questions, and provide support to users. This helps build a community around the project and fosters knowledge sharing.

4. Create a public repository: Set up a public code repository (e.g., GitHub) to store the project's code, documentation, and related resources. This repository can serve as a central hub for the project's artifacts, allowing others to easily discover and access them.

5. Engage with relevant communities: Reach out to relevant communities, such as software engineering or research groups, and present your project at conferences, workshops, or meetups. Share your insights, experiences, and lessons learned. Networking with other researchers and developers can help disseminate knowledge about the project and ensure its longevity.

6. Seek collaborations and partnerships: Explore opportunities to collaborate with other institutions, organizations, or researchers who may be interested in continuing the project or incorporating its findings into their own work. Collaborative efforts can help sustain the project's impact and facilitate ongoing development.

7. Apply for grants and funding: Although the project's original funding may have been cut, consider seeking alternative sources of funding. Look for grants, scholarships, or fellowships that support open-source software development, research initiatives, or knowledge sharing in your field. Funding can help sustain the project and enable further contributions.

8. Foster a culture of knowledge sharing: Encourage project members to share their expertise through blog posts, tutorials, or technical articles. Publish research papers, technical reports, or whitepapers that discuss the project's methodologies, challenges, and outcomes. By actively sharing knowledge, you increase the chances of the community benefiting from the project's know-how.

9. Collaborate with universities and research institutions: Establish relationships with academic institutions or research organizations that have an interest in the project's domain. Collaborate on joint projects, provide access to the project's resources, or mentor students who can contribute to the project. Academic partnerships can help preserve the project's knowledge and promote ongoing research.

10. Continuously update and maintain the project: Assign dedicated maintainers to oversee the project's evolution, address issues, and incorporate community contributions. Keep the project up to date with the latest software libraries, frameworks, and best practices. Regularly review and update the documentation to ensure it remains accurate and relevant.

By following these steps, you can increase the chances of preserving and sharing the software engineering know-how from a research software project, even when its funding is cut.

# Discontinuing a Research Software Project

Software projects come to an end for a variety of reasons.
A newer project can render an older project obsolete.

Research software projects in particular can come to an end in abrupt ways that ultimately impact the community's ability to ever reap any benefit from, learn lessons from or otherwise have available for posterity's sake any of the system architecture and software engineering know how that went into them.

The market or need for a capability can dwindle or completely disappear.
A sponsoring organization can wind up making a strategic decision to discontinue a software project.
Funding can run out.

Many *research* software projects have built-in sunset dates when the sponsoring
organization's funding ends. For SciDAC projects for example, a common
duration is 3-5 years. If a project is unable to gain traction within the
community and funding from other sponsors in that time frame, the project will most
likely have to be discontinued.

Over time, on-line project assets and artifacts and even contact information of
the people involved can fall out of date and/or become inaccessible. Future
researchers are then unable to discover the project even existed let alone benefit
from any knowledge gained. The only living record is likely to be publications.
However, in scientific computing projects, publications tend to focus
on the science enabled by the software so that little if any published knowledge
about the software itself remains available.

Utilization of software project hosting providers such as SourceForge, GitHub, GitLab,
etc.  definitely helps software projects avoid some issues when discontinuing by enabling
the project to maintain a continued presence even after funding is lost. The more
services (issue tracking, email lists, web site hosting, etc.) the project utilizes
from hosting providers, the easier it is for informabout about the project to remain
available even after all work has ended.
For example, GitHub features the ability to put a repository in an *archived* state.
But, even that has its limits (security updates for example take effort).

There are things project stakeholders and sponsoring organizations can do to *gracefully* 
discontinue a software project in such a way that key assets remain aviailable for
the benefit of the community.

What to do about existing users? What to do about future users?
license to transfer or support continued development by others.

One of the first things to decide is whether future project *communications* will go on
some form of life-support or be discontinued entirely. Having life-support communications
is obviously preferred but it comes at some non-zero cost and so may not be practical in
all cases. For life-support, it is important to identify *how* (e.g. email, twitter, slack)
any inquiries will be handled and by *whom* (e.g. email address, twitter handle, slack
username). This information should be posted prominently in all of the on-line spaces where
the project has a continued presence. Even if communications will be discontinued entirely,
it may make sense to provide way for inquirers to *register* their interest by some kind of
a sign-up process that collects such contact information.
GitHub reactions can do this.


Some of he choices a project makes up front can impact these questions

Problems with email and email lists, etc.

Collecting such inquiries

 may be useful in substantiating the level of interest to future
stakeholders
The ability to collect contacts
Will interested parties be directed to make contact by email, twitter, slack, etc. or just
be directed to a web page?

of

 One of the nice things about email
is that

Which modality(s) of communication with former project stakeholders will
be maintained 

* Identify the modality(s) of contact that will be maintained for any inquiries
  occurring *after* project discontinuation (e.g. email, twitter, GitHub discussions, etc.).

* Identify at least one person (preferrably 2 or 3 persons) who will serve as point
  of contact for any inquiries occuring after the project is discontinued. If this
  role needs to be transferred

* Some stakeholders should set semi-annual reminders on their calenders just to
  check and confirm the project's on-line presence is still working.
* Ensure on-line access points have a continued maintinence plan
  * as well as the systems where the below resources are hosted
  * mailing lists, discussion boards, ...
  * issue trackers
  * web site(s)
  * custom domain names
    * Custom domain names cost money and have expiration dates. In many cases, these
      custom domain names are just re-directions to a sponsoring organization's 
      own hosting resources. If so, change the re-direction for the custom domain name
      as soon as possible to an announcement page (e.g. break the redirection) indicating
      the project is discontinued. This way, while the custome domain name remains active,
      this will give time for project hosted through the sponsoring organization's own
      resources to become well known.
* Set up appropriate auto-responders on email list(s)
* Ensure various on-line access points prominently indicate that the project
  has been discontinued (or is in hibernation mode).

or is seeking funding


* security updates for hosting modalities
* For projects that involve persistent data formats, provide users with documentation
  about how to convert their data to another format.
* For projects for which decent alternative software products exist, maybe 
* Gather together whatever resources the project may have produced that help to
  explain/describe the software (slide decks from presentations, etc.)
  * This could be a simple listing of key files in the repository interested
    consumers should be aware of if they need to go look
* On GitHub, projects can be *archived* (converted to read-only)
* What can be done to ensure that if the project gets re-started, it can be easily
  picked back up and restarted by possibly new developers?
* Sponsoring organizations should be willing to allocate a small amount of remaining
  funds for teams to expend effort preparing the project for discontinuation. A good
  motive is helping to ensure the sponsor's investments to that point are not lost
  entirely.
