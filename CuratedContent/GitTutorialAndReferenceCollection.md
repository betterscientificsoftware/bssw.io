# A Tutorial and Reference Collection for Git

<!-- deck text start --> 
Revision control systems like Git are important for today's software ecosystems to help build better scientific software and improve developer productivity on a project.
Here is an excellent collection of tutorials and other resources  to learn about *Git*.
This overview takes the view that the best way to learn to use Git effectively is to learn it as a data-structure and a set of algorithms to manipulate that data-structure.

<!-- deck text end --> 

#### Contributed by [Roscoe A. Bartlett](https://github.com/bartlettroscoe)
#### Publication date: ???


## Introduction

This page provides links to some useful tutorial and reference information about the Git version control system.
This overview takes the view that the best way to learn to use Git effectively is to learn it as a data-structure and a set of algorithms to manipulate that data-structure which is consistent<sup>[wthigsh]</sup>.
This is important because the Git command-line interface is widely considered to be overly complex and confusing<sup>[gvmwg]</sup>.
For example, the same Git command like [checkout](http://marklodato.github.io/visual-git-guide/index-en.html#checkout) can do wildly different things depending on the other arguments that are passed into the command, or the state of the Git repository.
But Git is still currently the dominant VC system.

## Links to Git tutorial and reference material

For a full featured introduction and reference for Git, a good source is the free online book:

* ​**Pro Git: 2nd Edition** <sup>[pg2]</sup> by Scott Chacon and Ben Straub

But Pro Git is a big book and that is a lot of information for most people to remember.
And some people have a hard time finding the specific information they need in a book like that.
Therefore, provided below are some other shorter more targeted references that some people might find very helpful to understand Git and will want to consult in day-to-day usage of Git.

(NOTE: Since the publication of Pro Git 2nd edition in 2014, many other Git books have come along and many of them are likely to cover newer Git features, but the core of Git is unchanged since before 2008.)

Assuming you are a complete Git beginner and can’t wait to start contributing to a Git repo, you would be wise to first take note of:

* **Critical Beginner Git Usage Tips** <sup>[cbgut]</sup>

After that, for a nice (relatively short) visual reference for common Git operations, see:

* **​Visual Git Reference** <sup>[vgr]</sup>

A nice interactive visual tutorial (and simple Git simulator) and reference for common Git operations is:

* **​Visualizing Git Concepts with D3** <sup>[vgcd3]</sup>

Another similar site is:

* **Learn Git Branching** <sup>[lgb]</sup>

(The "Lean Git Branching" site is more interactive with more guided lessons than the "Visualizing Git Concepts with D3" site.
It also supports more Git commands like "git cherry-pick" and it allows for larger Git branching simulations.
Try out the [sandbox mode](https://learngitbranching.js.org/?NODEMO) to do quick unguided Git workflow simulations.
However, this is still just a simulator for Git so it does not support all Git commands and options.)

To really be able to use Git well, you have to know a little bit about how it works and how it stores changes to a repository.
To help understand this, a nice short overview of the Git object model is given in:

* **​The Git Object Model** <sup>[tgom]</sup>

The data model for Git is not very complicated as data-structures go;
it is that of a directed acyclic graph (DAG) where each node in the graph is a commit which represents a specific version (or snapshot) of the repository (repo).
The edges in the graph between adjacent nodes/commits represent patches or differences between the different versions of the repo’s files and provide the "history" of the changes of the repository.
Once you see how Git stores the different versions (snapshots) of a repo, you can use that information to understand the impact of various decisions and operations.
The *Visual Git Reference* <sup>[vgr]</sup> and nearly every other Git reference refers to this DAG of Git commits in some way.
A more technical description of the Git object model is given in the ​Git Pro [Object Model](http://git-scm.com/book/en/v2/Git-Internals-Git-Objects) chapter.
(Git also uses a more compact storage format called ​[Packfiles](http://git-scm.com/book/en/v2/Git-Internals-Packfiles) that can store deltas to changes in files for older history.)

For those that have the time to work through a longer online tutorial, consider taking the following excellent course which teaches both the basics of version control and Git as well as how to look at Git from a data-structure perspective:

* **Version Control with Git** <sup>[vcwg]</sup>

The above online course from Udacity.com is broken down into well-named sections so you can browse the course to find topics where you would like to see someone explain it in simple language, diagrams, and examples.

Here are some short Git cheat sheets that some may find useful:

* **​Git Cheatsheet** (from Tower) <sup>[gcst]</sup>
* **Git Cheatsheet** (interactive page from NDP Software) <sup>[gcsi]</sup>

(The latter Git Cheatsheet from NDP Software<sup>[gcsi]</sup> graphically shows how git commands move data between the various Git "places" and is a good complement to the *Visual Git Reference* <sup>[vgr]</sup>.

Here are some useful pages with various information about Git:

* **First Aid Git** <sup>[fagit]</sup> (includes search of FAQs)
* **How to undo (almost) anything in Git** <sup>[htuag]</sup>

If you can't find what you are looking for in the above references, do a web search for what you want to know and you will likely find a great explanation for how to do it on StackOverflow or some other site.





[wthigsh]: http://merrigrove.blogspot.com/2014/02/why-heck-is-git-so-hard-places-model-ok.html?m=1 "Why the Check is Git so Hard?  The Places Model"

[gvmwg]: http://blogs.atlassian.com/2012/03/git-vs-mercurial-why-git/ "Git vs. Mercurial: why Git?"

[pg2]: https://git-scm.com/book/en/v2 "Pro Git: 2nd Edition {Chacon, Scott, Straub Ben. 2014}"

[cbgut]: https://bssw.io/items/critical-beginner-git-usage-tips "Critical Beginner Git Usage Tips {Bartlett RA}"

[vgr]: http://marklodato.github.io/visual-git-guide/index-en.html "Visual Git Reference"

[vgcd3]: http://onlywei.github.io/explain-git-with-d3/ "Visualizing Git Concepts with D3"

[lgb]: https://learngitbranching.js.org/ "Learn Git Branching"

[tgom]: http://shafiulazam.com/gitbook/1_the_git_object_model.html "The Git Object Model"

[vcwg]: https://www.udacity.com/course/version-control-with-git--ud123 "Version Control with Git, Udacity.com"

[gcst]: https://www.git-tower.com/blog/git-cheat-sheet/ "Git Cheat Sheet {Tower})"

[gcsi]: http://ndpsoftware.com/git-cheatsheet.html#loc=index; "Git Cheatsheet {NDP Software}"

[fagit]: http://firstaidgit.io/# "First Aid Git"

[htuag]: https://github.blog/2015-06-08-how-to-undo-almost-anything-with-git/ "Show to undo (almost) anything with Git"


<!---
Publish: yes 
Pinned: no
RSS update: ???
Topics: revision control, release and deployment, development tools
--->

<!---
LocalWords:  
--->
