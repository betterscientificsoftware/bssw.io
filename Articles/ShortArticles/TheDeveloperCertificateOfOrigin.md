# The Developer Certificate of Origin

<!--deck text start-->
Every project that accepts contributions from outside developers should have a legal mechanism in place that allows those contributions to become part of the main code base for further development and/or distribution, and avoids any possible future legal issues that could arise. 
The Developer Certificate of Origin with signoffs embedded into Git commits messages is becoming the preferred way to approach these circumstances, and is being adopted by important open source projects.
<!--deck text end-->

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)

#### Publication date: January 26, 2022

When a person writes a piece of software, they own the copyrights in that software by default, unless it is a "work for hire". In that case, their employer owns it, or those rights are conveyed to some other legal entity by a written agreement.
Even if that person provides that source code with the implied intent to make it part of some existing software project or otherwise give it away (i.e. place it in the public domain), legal experts may differ as to whether that by itself is enough to allow the receiving project to modify and distribute the contribution along with the rest of the project.
For some experts, contributions are implicitly offered under the same licensing terms as the code base to which the contribution is being made.
Others prefer to have the owner of the copyright in new contributions explicitly state that they are providing the software (or a modification to an existing piece of software) to a project in accordance with some specific software license<sup>[0]</sup> associated with the project.
It is the process by which a person provides an (updated) contribution to an existing project that has an existing software license that serves as the focus of this article.

Until fairly recently, Contributor License Agreements (CLAs)<sup>[1],[2]</sup> have been the industry standard way to accept such contributions.
CLAs can be signed by individual contributors or by organizations (to cover all of its members).
While CLAs have a number of advantages for a project from a legal standpoint (such as facilitating later re-licensing), they are unpopular with some developers and developer communities, and are seen by many as an impediment to accepting contributions<sup>[3],[5]</sup>.

To address the problems with CLAs and other similar appraoches, the Linux Foundation introduced the Developer Certificate of Origin (DCO) in 2004<sup>[6]</sup>.
The DCO is a lightweight approach where developers "sign" every Git commit with a `Signed-off-by` line in the commit message:

```
This is the commit message

Signed-off-by: First M. Last <first.last@someurl.org>
```

This "sign-off" implies that the developer is asserting the terms of the DCO<sup>[7]</sup> which, as of Version 1.1, states:

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

Some major projects are using the DCO with Git commit sign-offs for handling contributions, including the Linux Kernel<sup>[8]</sup> and, more recently, the source code for GitLab itself <sup>[3],[4]</sup>.
In addition, the Linux Foundation's CII Best Practices Badge Program<sup>[9]</sup> contains the Silver-level item:

* The project SHOULD have a legal mechanism where all developers of non-trivial amounts of project software assert that they are legally authorized to make these contributions.
The most common and easily-implemented approach for doing this is by using a Developer Certificate of Origin (DCO)<sup>[7]</sup>, where users add "signed-off-by" in their commits and the project links to the DCO website.
However, this MAY be implemented as a Contributor License Agreement (CLA), or other legal mechanism.<sup>[10]</sup>

A few issues must be considered when adopting the DCO for accepting contributions.
First, since anyone can use any committer name and email address they want with a Git commit (e.g. using `git commit --amend --author "<any-author>"` and therefore impersonate someone else), greater assurance that the person signing off on the DCO is actually the author of the commit can be added by requiring commits to be GPG signed using the `-S` option with `git commit -s -S`<sup>[11]</sup>.
(However, requiring GPG signing of all commits adds a lot of extra overhead and complexity, which may be too much for many developers and, therefore, more limited usages of GPG signing are possible to provide some elevated assurances <sup>[12]</sup>.
It is unclear if any major project requires GPG signing of all commits to assert the DCO.)

Second, for the DCO to be effective, every commit that contains a nontrivial contribution needs to contain the `Signed-off-by` line.
Tools are available to assert that all commits in a GitHub Pull Request (PR) contain the `Signed-off-by` line<sup>[13]</sup>.
(Note that tools to automate the signing of CLAs for GitHub PRs also exist if one wants to automate CLA signoffs as well<sup>[14]</sup>.)

In summary, using a Developer Certificate of Origin (DCO) is a lightweight legal approach to provide cover in accepting contributions. However, it does come at the cost of requiring every nontrivial commit from a Pull Request for a proposed contribution to be signed-off by an outside contributor (and the process to go back and fix unsigned commits can be quite cumbersome for some people with poor Git knowledge and skills, or depending on how those commits and branches were constructed).
Therefore, for some developer communities, the upstream technical overhead and mechanics of applying the DCO may be more of an impediment to accepting outside contributions than the barriers to getting outside contributors or organizations to sign CLAs.

### Disclaimer

This is not legal advice.
Consult your own lawyer before any action that may have legal consequences.
The article is based on U.S. copyright law; other countries may differ.

[sl-sfer-ezikiw]: https://bssw.io/items/an-introduction-to-software-licensing "An Introduction to Software Licensing"

[ca-sfer-ezikiw]: https://contributoragreements.org/ "Contributor Agreements"

[cla-sfer-ezikiw]: https://en.wikipedia.org/wiki/Contributor_License_Agreement: "Contributor License Agreement"

[gitlab-dco-sfer-ezikiw]: https://about.gitlab.com/blog/2017/11/01/gitlab-switches-to-dco-license/ "GitLab: We're switching to a DCO for source code contributions"

[gitlab-dco-just-sfer-ezikiw]: https://docs.google.com/document/d/1zpjDzL7yhGBZz3_7jCjWLfRQ1Jryg1mlIVmG8y6B1_Q "GitLab: MEMO CLA vs DCO + License"

[gitlab-dco-benefits-sfer-ezikiw]: https://sdtimes.com/certificate-of-origin/power-open-source-gitlabs-move-developer-certificate-origin-benefits-developer-community "The power of open source: Why GitLab’s move to a Developer Certificate of Origin benefits the developer community"

[cla-vs-dco-sfer-ezikiw]: https://opensource.com/article/18/3/cla-vs-dco-whats-difference "CLA vs. DCO: What's the difference?"

[dco-sfer-ezikiw]: https://developercertificate.org/ "Developer Certificate of Origin"

[linux-kernel-github-sfer-ezikiw]: https://github.com/torvalds/linux/commits/master "Linux Kernel Git Repository"

[ciibp-sfer-ezikiw]: https://bestpractices.coreinfrastructure.org/en/criteria "CII Best Practices"

[ciibp-dco-sfer-ezikiw]: https://bestpractices.coreinfrastructure.org/en/criteria?details=true&rationale=true#1.dco "CII Best Practices [dco]"

[git-gpg-sfer-ezikiw]: https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work "Git Tools - Signing Your Work"

[dco-vs-clas-sfer-ezikiw]: https://jponge.medium.com/developer-certificate-of-origin-versus-contributor-license-agreements-339f36567dd7 "Developer Certificate of Origin versus Contributor License Agreements"

[github-dco-sfer-ezikiw]: https://github.com/apps/dco "Github DCO App"

[github-contrib-ass-sfer-ezikiw]: https://github.com/contributor-assistant/github-action/blob/master/README.md "Handling CLAs and DCOs via GitHub Action"

<!---
Publish: yes
Pinned: no
Topics: Projects and organizations, Strategies for more effective teams, Licensing, Revision control
RSS update: 2022-01-26
--->

<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[0]: #sfer-ezikiw-0 "An Introduction to Software Licensing"
[1]: #sfer-ezikiw-ee1 "Contributor Agreements"
[2]: #sfer-ezikiw-2 "Contributor License Agreement"
[3]: #sfer-ezikiw-3 "GitLab: We're switching to a DCO for source code contributions"
[4]: #sfer-ezikiw-4 "GitLab: MEMO CLA vs DCO + License"
[5]: #sfer-ezikiw-5 "The power of open source: Why GitLab’s move to a Developer Certificate of Origin benefits the developer community"
[6]: #sfer-ezikiw-6 "CLA vs. DCO: What's the difference?"
[7]: #sfer-ezikiw-7 "Developer Certificate of Origin"
[8]: #sfer-ezikiw-8 "Linux Kernel Git Repository"
[9]: #sfer-ezikiw-9 "CII Best Practices"
[10]: #sfer-ezikiw-10 "CII Best Practices [dco]"
[11]: #sfer-ezikiw-11 "Git Tools - Signing Your Work"
[12]: #sfer-ezikiw-12 "Developer Certificate of Origin versus Contributor License Agreements"
[13]: #sfer-ezikiw-13 "Github DCO App"
[14]: #sfer-ezikiw-14 "Handling CLAs and DCOs via GitHub Action"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-0"></a><sup>0</sup>[An Introduction to Software Licensing](https://bssw.io/items/an-introduction-to-software-licensing)
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[Contributor Agreements](https://contributoragreements.org/)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[Contributor License Agreement](https://en.wikipedia.org/w/index.php?title=Contributor_License_Agreement&oldid=884090001)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[GitLab: We're switching to a DCO for source code contributions](https://about.gitlab.com/blog/2017/11/01/gitlab-switches-to-dco-license/)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[GitLab: MEMO CLA vs DCO + License](https://docs.google.com/document/d/1zpjDzL7yhGBZz3_7jCjWLfRQ1Jryg1mlIVmG8y6B1_Q)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[The power of open source: Why GitLab’s move to a Developer Certificate of Origin benefits the developer community](https://sdtimes.com/certificate-of-origin/power-open-source-gitlabs-move-developer-certificate-origin-benefits-developer-community)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[CLA vs. DCO: What's the difference?](https://opensource.com/article/18/3/cla-vs-dco-whats-difference)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Developer Certificate of Origin](https://developercertificate.org/)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[Linux Kernel Git Repository](https://github.com/torvalds/linux/commits/master)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[CII Best Practices](https://bestpractices.coreinfrastructure.org/en/criteria)
* <a name="sfer-ezikiw-10"></a><sup>10</sup>[CII Best Practices [dco]](https://bestpractices.coreinfrastructure.org/en/criteria?details=true&rationale=true#1.dco)
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[Git Tools - Signing Your Work](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work)
* <a name="sfer-ezikiw-12"></a><sup>12</sup>[Developer Certificate of Origin versus Contributor License Agreements](https://jponge.medium.com/developer-certificate-of-origin-versus-contributor-license-agreements-339f36567dd7)
* <a name="sfer-ezikiw-13"></a><sup>13</sup>[Github DCO App](https://github.com/apps/dco)
* <a name="sfer-ezikiw-14"></a><sup>14</sup>[Handling CLAs and DCOs via GitHub Action](https://github.com/contributor-assistant/github-action/blob/master/README.md)
