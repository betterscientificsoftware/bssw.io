# GitHub Actions for Automation

<!--deck text start-->
From reminding reviewers of languishing PRs to packaging up release assets,
you can use GitHub Actions to automate all sorts of activities, not just CI,
in response to various events in your GitHub repositories.
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: March 31, 2021

Resource information | Details 
:--- | :--- 
Web Page | [Getting Started with GitHub Actions](https://itnext.io/getting-started-with-github-actions-fe94167dbc6d)
Authors | Daniel Weibel
Focus | Version control, Automated actions

Resource information | Details 
:--- | :--- 
Web Page | [Getting the Gist of Actions](https://gist.github.com/br3ndonland/f9c753eb27381f97336aa21b8d932be6)
Authors | [Brendon Smith](https://gist.github.com/br3ndonland)
Focus | Version control, Automated actions

GitHub introduced [*Actions*](https://github.com/features/actions) in 2018.

> You can discover, create, and share actions to perform any job you'd like,
> including CI/CD, and combine actions in a completely customized workflow.

The above web resources, *Getting Started with GitHub Actions* and *Getting the Gist of Actions*, provide a good starting point and overview of *GitHub Actions* service.

The GitHub Actions service is often described in the context of [Continuous Integration/Continuous Delivery-Deployment (CI/CD)](https://en.wikipedia.org/wiki/CI/CD)
workflows. However, GitHub Actions, can go beyond this, and is designed to support automation of all kinds of tasks associated with a software project
and its repository(s). The naming is a bit confusing because *Actions* is used both in the (1) name of the service,
*GitHub Actions*, and (2) name of a key building block used in that service, *Actions*,
typically found in the [marketplace](https://github.com/marketplace?type=actions).

To delve a bit more into GitHub Actions - 

The overarching abstraction, with GitHub Actions, is a [*workflow*](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#understanding-the-workflow-file) defined by Yaml files in the `.github/workflows` of a GitHub repository. In this respect, GitHub Actions are similar to [GitLab's CI/CD](https://docs.gitlab.com/ee/ci/). A workflow is
[*triggered*](https://docs.github.com/en/actions/reference/events-that-trigger-workflows)
by various events in a repository and *uses* [*actions*](https://github.com/marketplace?type=actions)
in preparation for executing one or more *jobs*, with whatever synchrony is needed.
Typically, the Yaml *scripts* defining workflows involve a combination of
GitHub-defined [yaml](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
keywords and syntax,
[*actions*](https://github.com/marketplace?type=actions) from the marketplace
and minimal amounts of python or shell code. In advanced cases, marketplace actions may be
customized or wholly new actions may
be implemented using either [JavaScript or Docker Containers](https://docs.github.com/en/actions/reference).

Although GitHub's [REST API](https://docs.github.com/en/rest/reference) has long
provided the functionality needed for projects to script up almost any workflow they
may wish, [*Actions*](https://docs.github.com/en/actions/reference) were introduced
with the goal of providing an easier to use and more convenient interface. Whether
that goal was achieved may be debatable.  Certainly, one price to pay for this convenience
is that anything automated with GitHub Actions will likely work only on GitHub and
nowhere else. In fact, it is often difficult even to test
[GitHub Action workflows locally](https://github.com/nektos/act). Depending on the kind
of activity to be automated, it may be best for a project to minimize dependence on
Actions by using a single-job workflow that invokes a shell or python script where
the majority of actual automation work is implemented.

<!---
Publish: preview 
RSS update: 2021-03-31
Categories: Development, Productivity
Topics: testing
--->

