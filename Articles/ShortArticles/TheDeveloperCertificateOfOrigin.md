# The Developer Certificate of Origin

<!--deck text start-->
Every project that accepts contributions from outside developers should have a legal mechanism in place that allows those contributions to become part of the main code base that allows for further development and distribution and avoids future legal problems.
The Developer Certificate of Origin with signoffs embedded into Git commits messages is becoming the preferred way to handle this issue and is being adopted by important open source projects.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date: ???, 2021

When a person writes a piece of software, by default, they own that software unless some other legal entity -- such as their employer -- owns their work by default.
And even if that person provides that source code with the implied intent to make it part of some existing software project or otherwise give it away (i.e. place it in the public domain), that by itself is not enough to allow the receiving project to modify and distribute the contribution along with the rest of the project.
Instead, individuals (or owning organizations) have to explicitly state that they are providing the software (or a modification to an existing piece of software) to a project in accordance to some specific software license associated with the project<sup>[sl]</sup>.
It is the process by which a person provides an (updated) contribution to an existing project that has an existing software license that is the focus of this article.

Until fairly recently, Contributor License Agreements (CLAs)<sup>[ca],[cla]</sup> have been the industry standard way to accept such contributions.
CLAs can be signed by individual contributors or by organizations (to cover all of its members).
While CLAs have a number of advantages for a project from a legal standpoint (such as allowing for later re-licensing), they are unpopular with some developers and developer communities and are seen by many as an impediment to accepting contributions<sup>[gitlab-dco],[gitlab-dco-benefits]</sup>.

To address the problems with CLAs and other similar appraoches, the Linux Foundation introduced the Developer Certificate of Origin (DCO) in 2004<sup>[cla-vs-dco]</sup>.
The DCO is a lightweight approach where developers "sign" every Git commit with a `Signed-off-by` line in the commit message:

```
This is the commit message

Signed-off-by: First M. Last <first.last@someurl.org>
```

which implies that the developer is asserting the terms of the DCO<sup>[dco]</sup> which, as of Version 1.1, states:

> By making a contribution to this project, I certify that:
> 
> (a) The contribution was created in whole or in part by me and I
>     have the right to submit it under the open source license
>     indicated in the file; or
> 
> (b) The contribution is based upon previous work that, to the best
>     of my knowledge, is covered under an appropriate open source
>     license and I have the right under that license to submit that
>     work with modifications, whether created in whole or in part
>     by me, under the same open source license (unless I am
>     permitted to submit under a different license), as indicated
>     in the file; or
> 
> (c) The contribution was provided directly to me by some other
>     person who certified (a), (b) or (c) and I have not modified
>     it.
> 
> (d) I understand and agree that this project and the contribution
>     are public and that a record of the contribution (including all
>     personal information I submit with it, including my sign-off) is
>     maintained indefinitely and may be redistributed consistent with
>     this project or the open source license(s) involved.

This `Signed-of-by` line can be added to the Git commit log automatically using the standard `-s` option with `git commit -s` (using information already registered with Git locally).

Some major projects are using the DCO with Git commit sign-offs for handling contributions including the Linux Kernel<sup>[linux-kernel-github]</sup> and more recently the source code for the GitLab itself <sup>[gitlab-dco],[gitlab-dco-just]</sup>.
In addition, the Linux Foundation's CII Best Practices Badge Program<sup>[ciibp]</sup> contains the Silver-level item:

* The project SHOULD have a legal mechanism where all developers of non-trivial amounts of project software assert that they are legally authorized to make these contributions.
The most common and easily-implemented approach for doing this is by using a Developer Certificate of Origin (DCO)<sup>[dco]</sup>, where users add "signed-off-by" in their commits and the project links to the DCO website.
However, this MAY be implemented as a Contributor License Agreement (CLA), or other legal mechanism. {Met URL} <sup>[ciibp-dco]</sup>

A few issues must be considered when adopting the DCO for accepting contributions.
First, since anyone can use any committer name and email address they want with a Git commit (e.g. using `git commit --amend --author "<any-author>"` and therefore impersonate someone else), greater assurance that the person signing off on the DCO is actually the author of the commit can be added by requiring commits to be GPG signed using the `-S` option with `git commit -s -S`<sup>[git-gpg]</sup>.
(However, requiring GPG signing of all commits adds a lot of extra overhead and complexity which may be too much for many developers and therefore more limited usages of GPG signing are possible to provide some elevated assurances <sup>[dco-vs-clas]</sup>.
It is unclear if any major project requires GPG signing of all commits to assert the DCO.)

Second, for DCO to be effective, every commit that contains a nontrivial contribution needs to contain the `Signed-off-by` line.
For example, tools are available to assert that all commits in a GitHub Pull Request (PR) contain the `Signed-off-by` line<sup>[github-dco]</sup>.
(Note that tools to automate the signing of CLAs for GitHub PRs also exist if one wants to automate CLA signoffs as well<sup>[github-contrib-ass]</sup>.)

In summary, using a Developer Certificate of Origin (DCO) is a lightweight legal approach to provide cover in accepting contributions but it comes at the cost of requiring every nontrivial commit from a Pull Request for a proposed contribution to be signed-off by an outside contributor (and the process to go back and fix unsigned commits can be quite cumbersome for some people with poor Git knowledge and skills or depending on how those commits and branches were constructed).
Therefore, for some developer communities, the upstream technical overhead and mechanics of applying the DCO may more of an impediment to accepting outside contributions than the barriers to getting outside contributors or organizations to sign CLAs.


[sl]: https://bssw.io/items/an-introduction-to-software-licensing "An Introduction to Software Licensing"

[ca]: https://contributoragreements.org/ "Contributor Agreements"

[cla]: https://en.wikipedia.org/wiki/Contributor_License_Agreement: "Contributor License Agreement"

[gitlab-dco]: https://about.gitlab.com/blog/2017/11/01/gitlab-switches-to-dco-license/ "GitLab: We're switching to a DCO for source code contributions"

[gitlab-dco-just]: https://docs.google.com/document/d/1zpjDzL7yhGBZz3_7jCjWLfRQ1Jryg1mlIVmG8y6B1_Q "GitLab: MEMO CLA vs DCO + License"

[gitlab-dco-benefits]: https://sdtimes.com/certificate-of-origin/power-open-source-gitlabs-move-developer-certificate-origin-benefits-developer-community/: "The power of open source: Why GitLab’s move to a Developer Certificate of Origin benefits the developer community"

[cla-vs-dco]: https://opensource.com/article/18/3/cla-vs-dco-whats-difference "CLA vs. DCO: What's the difference?"

[dco]: https://developercertificate.org/ "Developer Certificate of Origin"

[linux-kernel-github]: https://github.com/torvalds/linux/commits/master "Linux Kernel Git Repository"

[ciibp]: https://bestpractices.coreinfrastructure.org/en/criteria "CII Best Practices"

[ciibp-dco]: https://bestpractices.coreinfrastructure.org/en/criteria?details=true&rationale=true#1.dco "CII Best Practices [dco]"

[git-gpg]: https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work "Git Tools - Signing Your Work"

[dco-vs-clas]: https://jponge.medium.com/developer-certificate-of-origin-versus-contributor-license-agreements-339f36567dd7 "Developer Certificate of Origin versus Contributor License Agreements"

[github-dco]: https://github.com/apps/dco "Github DCO App"

[github-contrib-ass]: https://github.com/contributor-assistant/github-action/blob/master/README.md "Handling CLAs and DCOs via GitHub Action"

<!---
Publish: yes
Pinned: no
Topics: Projects and organizations, Strategies for more effective teams, Licensing, Revision control
RSS update: ???
--->
