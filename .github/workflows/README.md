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
    - trigger: pull request [opened, synchronized] on master branch
    - job: sync-pull-request
        - Merges PR into preview branch
* no-prs-on-preview.yml (Reject pull requests on preview branch)
    - trigger: pull request [opened, reopened] on preview branch
    - job: reject-pr
        - Attempts to open a PR against the preview branch are immediately closed and an explanatory comment is added to the PR.

# Markdown Checks
* Whole files can skip markdown checks with a comment of the form...
  ```
  <!-- BSSW_GITHUB_CI_IGNORE_MD_CHECKS -->
  ```
* Uses Node.JS tools (npm install)
* [lint check](https://www.npmjs.com/package/markdownlint)
  * Lint rules can be configured by a `.markdownlint.json` file at top of repo
* [link check](https://www.npmjs.com/package/markdown-link-check)
* [spell check](https://www.npmjs.com/package/markdown-spellcheck)
  * global dictionary words can be placed in `.spelling` file at top of repo
  * Per-file dictionary words can be specified by a comment block in the file of
    the form...
    ```
    <!-- BSSW_GITHUB_CI_SPELLING_WORDS
    word1
    word2
    -->
    ```

# Gaps
* PR is closed without merge.  We should back out the whole PR from preview?  Or kill and recreate preview?
* Recreate preview branch.  Trigger manually
    - Delete preview
    - Create preview from master
    - Foreach open PR
        - Merge PR to preview
* Have not investigated possibilities for conflicts and how they should be handled.
* Quality checks on content
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
* Long ago, Will Mclendon of SNL wrote a script to validate an article's metadata.  It would probably be useful to dust that off and update it.
