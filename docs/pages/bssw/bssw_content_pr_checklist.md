---
title: Content PR Checklist
sidebar: bssw_sidebar
permalink: bssw_content_pr_checklist.html
---
The following markdown should be copied and pasted into a content PR's initial comment.

---
```
Be sure to select `main` as the `base` branch above as the target for this PR.

Provide a general summary of your changes in the title above.

Fill in the below **Description** section with minimal text describing the changes/new contributions in this PR and replace `<...>` as appropriate.

Any checklist items that do not apply can be striken out by adding `~~` to the beginning and end of the checklist item as `* ~~[] <checklist-item>~~`.
Also, remove the strikeout markers `~~` for the [wikize_refs.py] checklist items if using formal citations for bssw.io contributions.

# Description

EB Member: @`<eb-member-id>`

Resolves #`<issue-id>`

`<Other minimal information about the PR.>`


## PR checklist for files displayed on bssw.io site

* [ ] ***[Author]*** `@mention` the BSSw.io editorial board member `@<eb-member-id>` in **Description** above assigned to shepherd your PR.
* [ ] ***[Author]*** Add the `<issue-id>` in the **Description** above for the associated GitHub Issue.
* ~~[ ] ***[Author]*** Ensure `wikize_refs.py -i <base>.md` is run and commit (if using [wikize_refs.py])~~.
* [ ] ***[Author]*** Inspect the content in the `*.md` file(s) as rendered in GitHub for this PR.
* [ ] ***[EB Mem]*** Assign this PR to the EB member `<eb-member-id>`.
* [ ] ***[EB Mem]*** Assign this PR to the author of the PR `<pr-author-id>`.
* [ ] ***[EB Mem]*** Add one or more Reviewers.
* [ ] ***[EB Mem]*** Add label `content: <content-type>` for the type of contribution.
* [ ] ***[EB Mem]*** Add to Project `Content Development` (see [Content Development]).
* [ ] ***[EB Mem]*** Add [meta-data] to the `*.md` file(s) (set `Publish: yes`).
* [ ] ***[EB Mem]*** Add label `preview` (so PR branch will be merged to 'preview' branch and watch for possible merge failures).
* [ ] ***[EB Mem]*** Rebuild [preview] site and confirm new content is there, renders correctly and is returned in searches.
* [ ] ***[Author]*** Make any final changes to the PR based on feedback.
* ~~[ ] ***[Author]*** Ensure `wikize_refs.py -i <base>.md` is run and commit (if using [wikize_refs.py]).~~
* [ ] ***[EB Mem]*** Rebuild [preview] site and re-confirm content looks correct.
* [ ] ***[EB Mem]*** Ensure at least one reviewer signs off on the final changes.
* [ ] ***[EB Mem]*** Move the PR to "Ready to Publish" in [Content Development].
* [ ] ***[EB Mem]*** Leave comment and @mention `@betterscientificsoftware/bssw-maint` (**BSSw Maint**) asking to carry out final publication steps.
* [ ] ***[BSSw Maint]*** Verify that all needed files are present in the PR (article, images, updates to Site/Homepage.md carousel and/or Site/Announcements/Announcements.md as appropriate).
* [ ] ***[BSSw Maint]*** Merge PR. (Should automatically move to "Done" in [Content Development].)
* [ ] ***[BSSw Maint]*** Verify new contribution shows up on [bssw.io] as expected.

NOTE:
* Checklist items prefixed with ***[Author]*** are expected to be performed by the author of the PR or can be performed by the author.
* Checklist items prefixed with ***[EB Mem]*** must be performed by a [BSSw.io Editorial Board (EB) Member](https://betterscientificsoftware.github.io/bssw.io/bssw_members.html).
* Checklist items prefixed with ***[BSSw Maint]*** must be performed by someone in the `@betterscientificsoftware/bssw-maint` team (hint: type `@`, `b`, `s`, `s`, `w`, `-`, `m`  to auto-complete to `@betterscientificsoftware/bssw-maint`).

<!-- Standard links below, leave these this section! -->

[preview]: https://preview.bssw.io
[bssw.io]: https://bssw.io
[Content Development]: https://github.com/betterscientificsoftware/bssw.io/projects/3
[BSSw Internal]: https://github.com/betterscientificsoftware/bssw.io/projects/2
[meta-data]: https://betterscientificsoftware.github.io/bssw.io/bssw_styling_common.html#metadata-section
[wikize_refs.py]: https://github.com/betterscientificsoftware/bssw.io/blob/master/utils/README.md#wikize_refspy
```
---

{% include links.html %}
