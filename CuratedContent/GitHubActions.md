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
which are typically found in the [actions marketplace](https://github.com/marketplace?type=actions).

The top-level concept is called a *workflow*. Yaml files in `.github/workflows` define
[*workflows*](https://docs.github.com/en/actions/learn-github-actions/introduction-to-github-actions#understanding-the-workflow-file);
a set of *jobs* to be performed with whatever synchrony is desired. In turn, jobs
often use [*actions* from the marketplace](https://github.com/marketplace?type=actions)
to perform work in response to various [*trigger*](https://docs.github.com/en/actions/reference/events-that-trigger-workflows)
events in the repository. GitHub directly provides the compute resources needed to 
run the workflows.

Typically, the Yaml *scripts* you develop to define workflows involve a combination
of [GitHub-defined yaml structure and keywords](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions),
[*actions* from the marketplace](https://github.com/marketplace?type=actions),
which may require minor customizations, and minimal amounts of python or shell code.

Although GitHub's [REST API](https://docs.github.com/en/rest/reference) has long
provided the functionality needed for projects to script up almost any workflow they
may wish, *Actions* represent an easy to use and more convenient abstraction.
However, one price to pay for this convenience is that any tasks automated with GitHub
Actions will likely work only on GitHub and nowhere else. In fact, it is often difficult
to even test [GitHub Action workflows locally](https://github.com/nektos/act).
Depending on the kind of activity to be automated, it may be best for a project to 
minimize its use dependence on GitHub actions and codify the majority of work as a
shell or python script the action calls.

<!---
Publish: review 
RSS update: 2021-03-31
Categories: Development, Productivity
Topics: testing
--->

