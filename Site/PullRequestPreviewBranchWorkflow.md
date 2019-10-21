# A Proposed Pull Request Workflow using a Preview Branch

The primary goal of this workflow is to allow the usage of a single BSSw
GitHub branch and Pull Request (PR) to be created and edited by multiple
actors where all reviews, edits, and all other modifications are made in that
one branch/PR before the PR is merged to the `master` branch and deployed on
the `bssw.io` site and to allow for previews on `preview.bssw.io` without
needing to merge to `master` first.  This is in contrast to current workflow
where the draft content is merged to `master` very early and subsequent edits
are done un-reviewed on `master`.


## Actors in the workflow

* **Author:** Creates a branch with the first draft of the proposed content on
  a branch (i.e. `content-A` in their fork of the BSSw repo) and then creates
  a PR of that branch against BSSw `master`.  (This could be actual content
  author or the editorial board member that collects the initial draft of the
  contribution from from Google Form placed there by the original author.)

* **EB Member:** BSSw editorial board member that shepherds the new PR through
  the editorial process (and may make small changes at the permission or
  request of the original author).

* **Technical Editor:** Professional technical writer that reviews and edits
  the document.

* **Sand Box:** A staff member at the company Sand Box that makes small
  changes to the proposed content so that it is displayed properly on the
  BSSw.io site.


## Overview of the workflow

An overview of the workflow using a `preview` branch is shown in the below
figure.

???Preview branch git workflow diagram???

This is a simplification of the "throw-away integration test branch" [???]
where the `preview` branch takes the place of the 'next' branch.

In this setup, the `production bssw.io` site is generated from the `master`
branch while the `preview.bssw.io` site is generated from the `preview`
branch.

Some simple rules for the workflow:

* To preview the content, merge the `content-X` branch to the `preview` branch
  and observe it on the `preview.bssw.io` site.

* All edits and reviews to the proposed content are performed on the
  `content-X` branch and the associated PR before merging to the `master`
  branch.

* When the proposed content is 100% ready to publish, the `content-X` branch
  is "graduated" (i.e. is merged to the `master` branch by merging to
  associated PR).

* The `preview` branch always contains `master` so every merge to `master`
  must be followed up by a merge of `master` to `preview`.

* The `preview` branch is **never** merged to the `master` branch.  (The
  `preview` branch is disposable and can be rebuilt from scratch at any time.)


## Proposed Implementation

The merge of the `content-X` branch is performed by GitHub by merging the
associated PR.  Pushing new commits to the `content-X` branch are performed as
usual.  Because the PR has been created, every GitHub user with push access to
the BSSw GitHub repo can push commits to the authors '<author-id>/content-x'
branch.  Therefore, the only operations that are not already coverted are the
merges to the `preview` branch from each PR branch and `master`.

The remaining operations of the proposed workflow can be performed manually on
the shell command-line, or using GitHub PRs on the web interface, or could be
automated with GitHub Actions or Travis CI jobs.  It would be highly desirable
to automate these merges to the `preview` branch as the workflow would have
near-zero manual overhead as compared to the current workflow (where the
`content-X` branch is merged to `master` very early and subsequent edits are
done un-reviewed on `master`).

The commands to merge an updated `content-X` branch to `preview` are:

```
[(<branch>)]$ git checkout preview
[ (preview)]$ git pulll       # from origin/preview
[ (preview)]$ git remote add <author-id> git@github.com:<author-id>/betterscientificsoftware.io.git
[ (preview)]$ git fetch <author-id>
[ (preview)]$ git merge <author-id>/content-x
[ (preview)]$ git push       # to origin/preview
```

The commands to update the `preview` branch after the `content-X` branch and
PR has been "graduated" (i.e. merged to `master`) are:

```
[(<branch>)]$ git checkout preview
[ (preview)]$ git pulll      # from origin/preview
[ (preview)]$ git merge origin/master
[ (preview)]$ git push       # to origin/preview
```

One can also perform these merges on the GitHub web API itself by creating
dummy GitHub PRs to merge from the different branches to the `preview` branch
but it would be somewhat tedious to do.  Therefore we would like to look at
automating these merges.

The automation of the merge of `master` to `preview` can easily be implemented
as a cron job on any machine with access to GitHub (using the unix account of
any BSSw EB member).  The more challenging operation to automate is the
merging of topic branches `content-X` to `preview`.  That is possible to
implement with either a GitHub Action or a Travis CI job.  The challenges to
overcome with using GitHub Actions or Travis CI jobs there are:

1) How to identify if the PR branch should be merged `preview` or not?  (Not
all branches on open PRs should be merged to the `preview` branch.)

2) How to do authentication to allow the push to the updated `preview` branch?

For the first challenge, one could define and apply a new GitHub Issue label
called `preview-content`.  If a PR has the label `preview-content` set, then
the GitHub Action (or Travis CI) job could check to see if that label is set,
and if so, merge the branch to `preview`.  Here, the job would need to be able
to query the labels on the associated PR and see if the `preview-content`
label was set.

As for the second challenge, it is not clear how to address the authentication
issue needed to push to the `preview` branch.  That will take some research to
figure out (but we know that there are ways to do this).
