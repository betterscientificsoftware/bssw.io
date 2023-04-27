BSSw Workflows

This file is intended to provide a roadmap to the various workflows.  Further comments should be found within each file.

Format:
* Filename (name)
    - trigger(s)
    - jobname
        - description

# Workflows in use

* merge-master-to-preview.yml (Sync master to preview)
    - trigger: push to master branch
    - job: sync-preview
        - Merges from master into preview branch.
* merge-pr-to-preview.yml (Sync pull request to preview)
    - trigger: pull request [opened, synchronized, labeled] (only if has 'preview' label)
    - job: sync-pull-request
        - Merges PR into preview branch
* no-prs-on-preview.yml (Reject pull requests on preview branch)
    - trigger: pull request [opened, reopened] on preview branch
    - job: reject-pr
        - Attempts to open a PR against the preview branch are immediately closed and an explanatory comment is added to the PR.
* issue-to-project.yml (Auto Assign to Project(s))
    - trigger: issue [opened, labeled], pull-request [opened, labeled]
    - job: assign_to_board
        - Assigns issues and PRs to either Content Development board or BSSw Internal board based on labels ("content: *" or "scope: site-internal")
* notify-external-contrib.yml (Notify external contributions)
    - https://github.com/betterscientificsoftware/bssw.io/blob/master/.github/workflows/notify-external-contrib.yml#L6-L12
    - job: notify-external-contributions
        - Label and send email to bssw-editorial-list for externally opened issues, prs and discussions

# Gaps
* PR is closed without merge.  We should back out the whole PR from preview?  Or kill and recreate preview?
* Recreate preview branch.  Trigger manually
    - Delete preview
    - Create preview from master
    - Foreach open PR
        - Merge PR to preview
* Have not investigated possibilities for conflicts and how they should be handled.
* Quality checks on content
    - verify links
    - check spelling
    - markdown lint (are we too different for this to be useful?)
    - BSSw required elements
    - verify BSSw metadata (long ago, Will Mclendon wrote a script for this)
    - BSSw style
    - Can we use the same script(s) the backend uses to ingest articles to test for exceptions?
 * Generate list of articles published via CHANGELOG-like mechanisms
    - Log of what is published when for reporting purposes
    - Pick out new things for the monthly digest.
 * Article title collisions cause problems in the backend.  It would be nice to be able to detect them and warn.
    - Any articles with the same title, regardless of path and (I think) regardless of their publication state cause problems.

# Potentially useful actions
* ljharb/require-allow-edits
    - I think it would probably be nicer to *suggest* rather than require
* mschilde/auto-label-merge-conflicts
    - On push, check all outstanding PRs for merge conflicts.  Add label and comment.
* outsideris/potential-conflicts-checker-action
    - On PR update, compare against all outstanding PRs for possible conflicts and add comments
* dawidd6/action-delete-branch
    - Delete a branch, i.e. to recreate preview
* peterjgrainger/action-create-branch
    - Create a branch, i.e. to recreate preview
* yellowmegaman/prtrigger
    - Make an empty commit to a PR to trigger synchronization actions
    - Doesn't seem to work for PRs from forks
* Mark C. Miller has introduced some useful MD-related processing into some of his other projects
    - There was some stuff document in the About file in earlier versions of the EB-docs.  Seems to have been removed now.
    - <https://travis-ci.com/github/visit-dav/visit-website/builds/181169664> provides an example of what the logs look like when a spelling check fails
    - <https://github.com/visit-dav/visit-website/blob/gh-pages/.travis.yml> invokes a linter, a spell checker, and a lnk checker
* Long ago, Will Mclendon of SNL wrote a script to validate an article's metadata.  It would probably be useful to dust that off and update it.
