# Working within Multiple Git Branches Simultaneously
<!--deck text start-->
Switching quickly and easily between multiple branches of development in Git is often much more involved than `git checkout`.
<!--deck text end-->

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86 "Mark C. Miller GitHub Profile")
#### Publication date: Feb 12, 2021

Resource information | Details
:--- | :--- 
Article title  | [Git Worktree: The best Git Feature You've Never Heard Of](https://levelup.gitconnected.com/git-worktrees-the-best-git-feature-youve-never-heard-of-9cd21df67baf)
Authors | James Pulec
Date | April, 2020
Length | ~1,300 words, 6 min. read
Focus | Git Productivity

In Git, the [`git checkout`](https://git-scm.com/docs/git-checkout) command is used to switch between branches.
In addition, if some work is incomplete but in progress, a common practice is to use
[`git stash`](https://git-scm.com/docs/git-stash) to temporarily stash changes away before switching branches.

However, when working on multiple branches of development *simultaneously*, there is often more involved than just
stashing half-completed work away or switching the currently active branch. Some code may need to be re-configured
and/or re-compiled; maybe a lot of it. This is particularly true for projects which are sensitive
to timestamp changes of *any* build tree dependencies. Resulting delays can create a productivity issue.

A common approach is to [`git clone`](https://git-scm.com/docs/git-clone) the same repository multiple times and
then set each clone to a different branch. It is even possible to keep local clones synchronized (without going
through their common `origin`) using [`git remote add <name> <local-path>`](https://git-scm.com/docs/git-remote)
and [`git fetch <name>`](https://git-scm.com/docs/git-fetch) (where `<local-path>` is the local directory path to
another local repo clone). However, this involves multiple copies of the git repository which may have negative
implications for disk space or workflow.

Alternatively, you may find [`git worktree`](https://git-scm.com/docs/git-worktree) a better approach than multiple
clones and a useful productivity boost. Git worktrees allow you to work as if you have multiple clones without
having to make explicit cloned copies, saving disk space and perhaps easing any workflow issues. A single `.git`
database, including local hooks and other settings for example, manages all the worktrees. The advantages of Git
worktrees over clones multiply as the number of concurrent branches to be managed grows. On the other hand, if 
it is necessary to manage different repository settings (e.g. hooks, file ignores) across concurrent branches,
multiple clones may be the only solution.

Finally, although [`git worktree`](https://git-scm.com/docs/git-worktree) has been available in Git
since 2015, it is still considered an *experimental* feature and doesn't work with Git submodules.

<!---
Publish: yes
Pinned: no
Categories: skills, development
Topics: revision control, development tools
RSS update: 2021-02-16
--->
