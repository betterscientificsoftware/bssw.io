# GitHub Actions for Repo Event Automation

<!--deck text start-->
From reminding reviewers of languishing PRs to packaging up release assets,
you can use GitHub Actions to automate all sorts of activities, not just CI,
in response to various events in your GitHub repos.
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: March 31, 2021

Resource information | Details 
:--- | :--- 
Web Page | [Getting Started with GitHub Actions](https://itnext.io/getting-started-with-github-actions-fe94167dbc6d)
Authors | Daniel Weibel
Publication | June, 2020, 16 min. read
Web Page | [Getting the Gist of Actions](https://gist.github.com/br3ndonland/f9c753eb27381f97336aa21b8d932be6)
Authors | [Brendon Smith](https://gist.github.com/br3ndonland)
Publication | August, 2020

GitHub introduced [*Actions*](https://github.com/features/actions) in 2018.

> You can discover, create, and share actions to perform any job you'd like,
> including CI/CD, and combine actions in a completely customized workflow.

They are often described in the context of [CI/CD](https://en.wikipedia.org/wiki/CI/CD)
workflows. However, that is not all they are good for. GitHub Actions are
designed to support automation of all kinds of tasks associated with a software project
and its repository(s).  

The naming is a bit confusing because *Actions* is used both in the name of the service,
*GitHub Actions*, and in the name of a key building block used in that service, *Actions*,
typically taken from the [marketplace](https://github.com/marketplace?type=actions).
However, the overarching abstraction is a
[*workflow*](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#understanding-the-workflow-file)
defined by Yaml files in the `.github/workflows` of a GitHub repository. A workflow is
[*triggered*](https://docs.github.com/en/actions/reference/events-that-trigger-workflows)
by various events in a repository and *uses* [*actions*](https://github.com/marketplace?type=actions)
in preparation for executing one or more *jobs*, with whatever synchrony is needed.

Typically, the Yaml *scripts* defining workflows involve a combination of
[GitHub-defined yaml structure and keywords](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions),
[*actions* from the marketplace](https://github.com/marketplace?type=actions),
which may need minor customizations, and minimal amounts of python or shell code.
In this respect, GitHub Actions are similar to [GitLab's CI/CD](https://docs.gitlab.com/ee/ci/).

Although GitHub's [REST API](https://docs.github.com/en/rest/reference) has long
provided the functionality needed for projects to script up almost any workflow they
may wish, [*Actions*](https://docs.github.com/en/actions/reference) represent an easier
to use and more convenient abstraction. However, one price to pay for this convenience
is that anything automated with GitHub Actions will likely work only on GitHub and
nowhere else. In fact, it is often difficult even to test
[GitHub Action workflows locally](https://github.com/nektos/act). Depending on the kind
of activity to be automated, it may be best for a project to minimize dependence on
GitHub Actions and implement the majority of work as a single job shell or python script.

<!---
Publish: review 
RSS update: 2021-03-31
Categories: Development, Productivity
Topics: testing
--->

