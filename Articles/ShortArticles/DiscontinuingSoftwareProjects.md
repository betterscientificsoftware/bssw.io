# Discontinuing a Research Software Project

Software projects can come to an end for a variety of reasons. A newer offering
can wind up making an older project obsolete. The market or need for the capability
dwindles or completely disappears. A sponsoring organization can wind up making
a strategic decision to discontinue a software project. Funding can run out.

Here we focus on the case of funding running out for an otherwise healthy,
productive and useful software project.

Many *research* software projects have built-in sunset dates when the sponsoring
organization's funding award runs out. For SciDAC projects for example, a common
duration is 3-5 years. If projects are unable to gain sufficient traction within
the community to secure continued (production) funding, such projects wither and
die. Over time, project assets and artifacts and even the people involved can
become inaccessible due to resources falling out of date (bitrot). Any future
researchers are then unable to discover the project even existed let alone benefit
from any of the knowledge gained. The only living record is likely to be
publications. However, in scientific computing projects, publications tend to focus
on the science enabled by the software meaning that without care, little if any
published knowledge about the software itself remains available.

Utilization of project hosting services such as SourceForge (then) and GitHub (now)
definitely helps software projects avoid some issues when discontinuing by enabling
the project to maintain a continued presence even after funding is lost. The more
services (issue tracking, email lists, web site hosting, etc.) the project utilizes
from the hosting service, the easier it is for the project to go into hibernation
mode.

However, there are a few things project leaders and sponsoring organizations can do to
discontinue a software project in such a way that key assets remain aviailable
for the community.

* Ensure on-line access points have a continued maint. plan
  * as well as the systems where the below resources are hosted
  * mailing lists
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
  has been discontinued.
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
