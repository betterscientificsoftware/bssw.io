---
title: Preview Branch Workflow
sidebar: bssw_sidebar
permalink: bssw_pr_preview_branch.html
---

## BSSW.io Pull Request Workflow using a Preview Branch

This workflow allows the usage of a single bssw.io GitHub branch and Pull
Request (PR) to be created and edited by multiple actors where all reviews,
edits, and all other modifications are made in that one branch/PR before the
PR is merged to the `main` branch and deployed on the `bssw.io` site.  In
addition, it allows previews on https://preview.bssw.io without needing to
merge to `main` first.

**Contents:**

* [Actors in the workflow](#actors)
* [Overview of the workflow](#overview)
* [Current Implementation](#current_impl)
* [Removing content from `preview` branch, preview site, or main bssw.io site](#unpublish)

<a name="actors"/>

### Actors in the workflow

* **Author:** Creates a branch with the first draft of the proposed content on
  a branch (i.e. branch `content-A` in their fork of the `bssw.io` repo) and
  then creates a PR of that branch against the `bssw.io` repo `main` branch.

* **EB Member:** BSSw editorial board member that shepherds the new PR through
  the editorial process (and may make small changes at the permission or
  request of the original author).

* **Technical Editor:** Professional technical writer that reviews and edits
  the document.

* **Website Contractor:** A staff member at the website company that makes
  small changes to the proposed content so that it is displayed properly on
  the https://bssw.io site.

<a name="overview"/>

### Overview of the workflow

An overview of the workflow using a `preview` branch is shown in the below
figure.

![BSSw Pull Request Preview Branch Workflow](https://github.com/betterscientificsoftware/images/blob/main/PullRequestPrerviewWorkflow.png)

This is a simplification of the [throw-away integration test
branch](https://docs.google.com/document/d/1uVQYI2cmNx09fDkHDA136yqDTqayhxqfvjFiuUue7wo#heading=h.2r0g9kvx5b2a)
where the `preview` branch takes the place of the `next` branch.

In this setup, the production https://bssw.io site is generated from the
`main` branch while the https://preview.bssw.io site is generated from the
`preview` branch.

The updated content is only viewed on the https://preview.bssw.io site if
`Publish: publish` or `Publish: yes` is set in the meta-data in the `*.md`
file and is only viewed on the https://bssw.io site if `Publish: yes` is set
(see the [`publish: [yes|no|preview]` meta-data
option](https://betterscientificsoftware.github.io/bssw.io/bssw_content_publishing.html#pre-publishing-checks)).

Some simple rules for the workflow:

* To preview the content, merge the `content-X` branch to the `preview`
  branch.  (Currently, one must then manually rebuild the
  https://preview.bssw.io site, and observe it on the https://preview.bssw.io
  site)

* All edits and reviews to the proposed content are made in commits on the
  `content-X` branch and the associated PR before merging to the `main`
  branch.

* When the proposed content is 100% ready to publish, the `content-X` branch
  is "graduated" (i.e. is merged to the `main` branch by merging to
  associated PR).

* The `preview` branch always contains `main` so every merge to `main`
  must be followed up by a merge of `main` to `preview`.

* The `preview` branch is **never** merged to the `main` branch.  (The
  `preview` branch is disposable and can be rebuilt from scratch at any time.)


<a name="current_impl"/>

### Current Implementation

The merge of the `content-X` branch to `main` is performed by GitHub by
merging the associated PR.  Pushing new commits to the `content-X` branch are
performed as usual.  Because the PR has been created, every GitHub user with
push access to the `bssw.io` GitHub repo can push commits to the author's
`<author-id>/content-x` branch.  Therefore, the only operations that are not
already handled by GitHub are the merges to the `preview` branch from each PR
branch and `main`.

The remaining operations of the workflow are performed automatically using
GitHub actions.

The commands to merge an updated `content-X` branch to `preview` are:

```
[(<branch>)]$ git checkout preview
[ (preview)]$ git pull       # from origin/preview
[ (preview)]$ git remote add <author-id> git@github.com:<author-id>/betterscientificsoftware.io.git
[ (preview)]$ git fetch <author-id>
[ (preview)]$ git merge <author-id>/content-x
[ (preview)]$ git push       # to origin/preview
```

These commands are performed automatically by the Github Actions [`merge-pr-to-preview.yml`](https://github.com/betterscientificsoftware/bssw.io/blob/main/.github/workflows/merge-pr-to-preview.yml) workflow when the `preview` label is set on the PR for the branch `content-x` and whenever new commits are pushed to the PR branch when that label is set.  (If the `preview` label is not set, then the PR branch is not automatically merged to the `preview` branch.)

The commands to update the `preview` branch after a `content-X` branch and PR
has been "graduated" (i.e. merged to `main`), or any updates to the `main`
branch are made, are:

```
[(<branch>)]$ git checkout preview
[ (preview)]$ git pull      # from origin/preview
[ (preview)]$ git merge origin/main
[ (preview)]$ git push       # to origin/preview
```

These commands are performed automatically by the GitHub Actions [merge-main-to-preview.yml](https://github.com/betterscientificsoftware/bssw.io/blob/main/.github/workflows/merge-main-to-preview.yml) workflow whenever new commits are pushed to the `main` branch (either by merging a PR to `main` or direct pushes to `main`).

<a name="unpublish"/>

### Removing content from `preview` branch, preview site, or main bssw.io site

To remove changes from the `content-X` branch for a PR that has not been
merged to `main` and stop the display of that content on the
https://preview.bssw.io site, one can do one of the following:

* Revert and push the changes to the `preview` branch or remove new `*.md`
  files and push to the `preview` branch.

* Set `Publish: no` in the meta-data for the `*.md` file in a commit directly
  on the `preview` branch (but the `*.md` file will remain on the `preview`
  branch).

NOTE: In the future, removing content from PRs that were closed without
merging to the `main` branch could be handled automatically (e.g. by
rebuilding the `preview` branch from scratch each time new commits are pushed
to a PR branch for open PRs or to `main`).

To unpublish a contribution already published to `main` and displayed on the
main https://bssw.io site, one can do one of the following:

* Create a new branch and PR that removes the `*.md` file and merge that PR to
  `main`.

* Create a new branch and PR that simply changes from `Publish: yes` to
  `Publish: no` in the meta-data at the bottom of the `*.md` file and merge
  that PR to `main`.

NOTE: One can also push new commits that remove the `*.md` file or change to
`Publish: no` directly to `main` but the advantage of using PRs to do so is
that the decision to unpublish is a little more visible.  (But the fact that
new commits unpublish the `*.md` document keeps a record of this and the
justification for doing so can be made in the commit message.)


{% include links.html %}
