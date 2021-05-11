3# Critical Beginner Git Usage Tips

<!-- deck text start -->
Follow these simple guidelines for setting up and using Git and you'll stay out of serious trouble and be more productive.
<!-- deck text end --> 

#### Contributed by [Roscoe A. Bartlett](https://bartlettroscoe.github.io/ "Roscoe A. Bartlett")
#### Publication date: May ??, 2021

<a name="guidelines"></a>

## Guidelines

* [Set up minimal global settings right away on every new computer.](#minimal-setup)
* [Create proper logical commits and commit messages.](#logical-commits)
* [Create small local "checkpoint" commits then cleanup with 'git rebase -i'.](#small-commits-rebase-i)
* [Create local commits before running any commands that might accidentally modify/overwrite uncommitted changes.](#uncommitted-changes)
* [Backup local branches every few hours of work to remote Git repo on remote machine.](#backup-frequently)
* [You can always recover an earlier state of any of your local branches.](#recover-previous-state)
* [Never delete a local Git repo unless you are completely done with it.](#dont-delete-and-reclone)
* [Do not commit large generated (binary) files in a Git repo without careful consideration.](#beware-binary-files)
* [Avoid `git push -f` to a remote branch shared with other people.](#avoid-force-push)


<a name="minimal-setup"></a>

### Set up minimal global settings right away on every new computer <sup>[[minimal-setup](#minimal-setup)]</sup>

Always set up a consistent global Git `user.name` and `user.email` on every machine where you use Git.
(Otherwise you will show up as many different developers according to Git, and it is a pain to resolve these in all of the Git repos you commit to after the fact).
Also, disable push of all branches by default (prior to Git 2.0) or a simple `git push` will push all branches.
In addition, it is nice to see Git output with color (default is no color).
And, to avoid having to resolve the same merge conflicts multiple times, consider turning on the [`git rerere`](https://git-scm.com/docs/git-rerere) feature.
To set these on a new machine, run:

```
$ git config --global user.name "First M. Last"          # CRITICAL
$ git config --global user.email "youremail@someurl.com" # CRITICAL
$ git config --global color.ui true        # Use color in git output to terminal.
$ git config --global push.default simple  # Or 'tracking' with older versions of git.
$ git config --global rerere.enabled 1     # Auto-resolve same conflicts on rebase.
```

Also consider setting up your bash shell prompt and `git` command-completion by downloading the bash scripts [git-prompt.sh](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh) and [git-completion.bash](https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash) and add activating them by adding them to your `~/.bash_profile` file with the lines:

``` 
source ~/git-prompt.sh
source ~/git-completion.bash
PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '
```

These bash scripts make using Git on the command-line much easier and more productive.


<a name="logical-commits"></a>

### Create proper logical commits and commit messages <sup>[[logical-commits](#logical-commits)]</sup>

Creating good commits with good commit messages is important for many reasons.
Commits should contain a single logical change (see "SEPARATE CHANGES" in [gitworkows(7)](https://www.kernel.org/pub/software/scm/git/docs/gitworkflows.html) and "One Commit per Logical Change Solution" in the [Udacity Git course](https://www.udacity.com/course/version-control-with-git--ud123)).
Commit messages should have a short summary line (under 50 chars is the target) and an optional longer body separated by a blank line (see guidelines in [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)).
For example:

```
Summary line for changes (50 chars is target but a little longer okay)

More detailed explanatory text in the body (wrapped to about 72 chars).
The blank line separating the summary from the body is critical to make
commands like 'git log --oneline', 'git rebase -i', and others readable
and useful.

If you use an issue tracker, put references to them like:

Resolves: #123
Also see: #456, #789
```


<a name="small-commits-rebase-i"></a>

### Create small local "checkpoint" commits then cleanup with `git rebase -i` <sup>[[small-commits-rebase-i](#small-commits-rebase-i)]</sup>

To provide for easy local "undos" and better organization of changes into final change-sets, commit often locally using "checkpoint" commits (convention is to use commit summary lines starting with "WIP:").
But before pushing these commits to a remote shared branch, use [`git rebase -i @{u}`](https://www.atlassian.com/git/tutorials/rewriting-history#git-rebase-i) to clean up and reorganize the commits into good "logical" commits (see "SEPARATE CHANGES" above).


<a name="uncommitted-changes"></a>

### Create local commits before running any commands that might accidentally modify/overwrite uncommitted changes <sup>[[uncommitted-changes](#uncommitted-changes)]</sup>

The commands `git pull`, `git merge`, `git rebase`, or other Git operations can alter (or
delete) your local uncommitted changes, either in the working directory or the staging
area/index.
So always create (sometimes temporary) commits for these before running any of these commands (unless you want to throw away uncommitted changes in your local repo, for example with `git checkout`, `git reset`, `git clean`, etc.).


<a name="backup-frequently"></a>

### Backup local branches every few hours of work to remote Git repo on remote machine <sup>[[backup-frequently](#backup-frequently)]</sup>

This is to safeguard your work in case your local machine or disk goes out or your local `.git/` directory becomes corrupted somehow.
(Local Git branches are better than Git stashes because you can back them up to other repos in a version controlled way.
You can’t do that with Git stashes.)


<a name="recover-previous-state"></a>

###  You can always recover an earlier state of any of your local branches if you have been careful to commit your work to local branches <sup>[[recover-previous-state](#recover-previous-state)]</sup>

To recover an earlier state, run [`git reflog`](https://git-scm.com/book/en/v2/Git-Internals-Maintenance-and-Data-Recovery) and then use a combination of [`git checkout`](http://marklodato.github.io/visual-git-guide/index-en.html#checkout) and/or [`git reset –hard`](http://marklodato.github.io/visual-git-guide/index-en.html#reset), etc.
(See [How to undo (almost) anything in Git](https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/#redo-after-undo-local).)


<a name="dont-delete-and-reclone"></a>

### Never delete a local Git repo unless you are completely done with it <sup>[[dont-delete-and-reclone](#dont-delete-and-reclone)]</sup>

Your local Git repos have a [wealth of information that can’t be pushed to other Git repos](https://www.cs.cmu.edu/~davide/howto/git_lose.html) (e.g. `git rerere` info, `git reflog` info, etc.).
If you [have an escape plan (see above)](#recover-previous-state), you should never have to delete a local Git repo and re-clone to get out of some "bad" state.
Only a corrupted disk that corrupts the local Git DB history (which is extremely rare) should cause you to have to re-clone the local Git repo.
(If you feel like you need to delete your local Git repo to get out of some bad state of a non-corrupted repo, then you have not yet learned the basics of Git well enough so keep learning!)


<a name="beware-binary-files"></a>

### Do not commit large generated (binary) files in a Git repo without careful consideration <sup>[[beware-binary-files](#beware-binary-files)]</sup>

Most revision control systems, and Git is no exception, are optimized to handle text/ascii files.
They don't do well with binary files, especially *large* binary files.
Big generated (binary) files committed to a git repo get stuck in the Git history **forever** and can only be removed by "[filtering](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History)" the Git repo (which is a very disruptive process for everyone involved).
That said, sometimes handling binary files in a Git repo cannot be avoided in which case consider using Git [Large File Storage](https://git-lfs.github.com/) (Git-LSF) support.
Git-LFS will add complexity to your workflows but also save you from clogging history.


<a name="avoid-force-push"></a>

### Avoid `git push -f` to a remote branch shared with other people unless everyone involved really knows what they are doing <sup>[[avoid-force-push](#avoid-force-push)]</sup>

Very few Git users know how to adjust to a forced reset remote branch or even what that means.
(However, if everyone involved knows how to adjust with a forced pushed reset branch to a (temp) shared branch or if the branch is not shared, then forced pushes are fine.)


### Conclusion

There are many other helpful guidelines that you can come up with for using Git but the ones above are arguably the most helpful for Git beginners (and some people that have been using Git for many years but never learned these basic guidelines).

<!---
 Publish: preview
 Pinned: no
 Topics: revision control, development tools
 RSS update: 2021-05-??
 --->
