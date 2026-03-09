# Stuck Writing Software Documentation? Focus on One Good Tutorial

**Hero Image:**

- <img src='../../images/Hero_topic_user_experience_072125.png' />

#### Contributed by [Peter K. G. Williams](https://newton.cx/~peter/)

#### Publication date: January TKTK, 2026

<!-- begin deck -->
BSSw Fellow Peter K. G. Williams has developed a new resource called [One Good
Tutorial](https://onegoodtutorial.org/) that aims to help creators of scientific
software write better documentation with less stress.
<!-- end deck -->

### The challenge of scientific software documentation

“Documentation.” For many authors of scientific software, the word evokes a
feeling of guilt, or dread. Have I written enough? Is what I’ve written any
good? We’re already working outside of our comfort zones — scientists asked to
pass as professional developers, and vice versa. To write really great
documentation to go along with our software, we’d have to don many more hats:
technical writer, information architect, typographer, teacher. If you or your
project are able to marshal all those skill sets, that’s wonderful, but most of
us generally have to do the best we can with limited time, resources, and
expertise. It’s a recipe for a frustrating experience.

What’s more, documentation is often only really tackled when a project is close
to release time, too. It’s not that it’s an afterthought, but it does tend to be
less urgent than adding features or fixing bugs, so it can naturally drift to
the bottom of the priority queue. The unfortunate result is that work on
documentation is frequently getting started when both time and energy are
already low.

### Does it have to be this way?

One day, maybe you’ll be able to wave a magical AI wand and a computer will
write all of your documentation for you, and maybe it won’t even be riddled with
errors. But for the near future, at least, creating high-quality documentation
for your software takes old-fashioned human elbow grease. That’s the bad news.

The good news is that there are a lot of resources out there aiming to help make
the job a little easier. For instance, the [Write the Docs
community](https://www.writethedocs.org/) maintains a [software documentation
guide](https://www.writethedocs.org/guide/) chock full of best practices and
style recommendations. It’s got a lot of detailed information for someone
looking to really hone their writing craft.

Another valuable resource in a very different style is
[Diátaxis](https://diataxis.fr/), which describes itself as “a way of thinking
about and doing documentation.” A bold claim! But one that’s well-founded.
Diátaxis is also known as the Divio system or the “four docs” model, the latter
because its central tenet is that documentation comes in four fundamental
*kinds*: [tutorials](https://diataxis.fr/tutorials/), [how-to
guides](https://diataxis.fr/how-to-guides/),
[reference](https://diataxis.fr/reference/), and
[explanations](https://diataxis.fr/explanation/). Diátaxis doesn’t get into the
nuts and bolts of writing actual documents, but rather presents a theoretical
framework for thinking about documentation as a whole — one that has proven
quite popular.

And now there’s a new resource to mention. I was awarded a [2025 Better
Scientific Software
Fellowship](https://bssw.io/blog_posts/introducing-the-2025-bssw-fellows) to
create materials aimed at people who are documenting scientific software
projects. The goal was to create something pragmatic, intended for people
working on small-to-medium scientific projects who want to do the best they can
with their documentation but also have a lot of other demands on their time.

### Introducing: One Good Tutorial

The resource that I built is called *One Good Tutorial*, and it’s now available
for early feedback at [onegoodtutorial.org][ogt]. It’s not quite polished enough
to be stamped as “version 1.0,” but it’s substantially complete and ready for
real-world testing.

[ogt]: https://onegoodtutorial.org/

The focal point of One Good Tutorial is a short checklist of documentation
elements, such as “Installation instructions” and “Licensing statement”. The
core pitch of One Good Tutorial is: *if your software’s documentation contains
all of the items listed in [the official One Good Tutorial software
documentation checklist][ogt], you have permission to declare that your
documentation is good enough*. Go ahead and move on to the next task in your
to-do list. Hooray!

The goal of the checklist is to turn the task of writing documentation from one
that can feel painfully open-ended into one with a concrete finish line. Of
course, great documentation will go far, far beyond what’s specified in the
checklist, and it would be wonderful if everyone’s documentation were great. But
there are only so many hours in the day, and if you want or need to spend them
on something other than your documentation, that’s wonderful too.

One of the key items on the checklist is — you guessed it — a good tutorial. I
thought that it was so important to emphasize this item that I made it into the
name of the whole project. The emphasis is because when some developers think of
“documentation,” they think of API reference material and nothing else. One of
the fundamental arguments of Diátaxis, which I wholeheartedly agree with, is
that idea is tempting but wrong. Reference material such as API documentation is
important, but it’s important to a certain set of people: those who are already
familiar with your software and are actively using it to solve a problem. For a
new software project, there’s a much more important group of people to target:
*potential* users who have become of your software, but don’t necessarily even
really understand what it’s for, let alone how to use it in detail. These people
need an entirely different kind of documentation: a tutorial. Now, tutorials are
hard to write because they are fundamentally acts of teaching, delivered
remotely and anonymously. Think of how rare truly great teaching is in this
world — it’s daunting. But I contend that for a new project this is the single
most important part of your documentation, and so the one that deserves the
biggest piece of your limited attention.

Alongside the checklist is [the One Good Tutorial playbook][pb]. The playbook is
a suggested set of steps to go from zero to a checklist-compliant suite of
documentation. There’s nothing particularly profound about it, but if you’re not
quite sure how you want to get started, it gives you a tangible way to proceed.
I present the playbook as an HTML slideshow (built using the [reveal.js]
framework), which I’ve found to be a convenient and effective way to present
this kind of step-by-step material.

[pb]: https://onegoodtutorial.org/playbook/
[reveal.js]: https://revealjs.com/

Finally, in support of all of these, One Good Tutorial includes [a series of
in-depth guides][guides]. These are longer articles that offer help on different
aspects of the documentation process, with an emphasis on examples and links to
other resources for those that have the time and inclination to go into greater
depth.

[guides]: https://onegoodtutorial.org/in-depth/

### How you can help

No mystery here: if you’re in a position to, please give [One Good
Tutorial][ogt] a try and [provide some feedback][feedback] about what worked and
what didn’t! Or spread the word to your colleagues who you think might find this
resource useful. You are more than welcome to reach out via [the One Good
Tutorial repository on GitHub][gh] where all of the project materials are
managed. Happy documenting!

[feedback]: https://onegoodtutorial.org/about/#feedback
[gh]: https://github.com/pkgw/onegoodtutorial/

### Author bio

[Peter K. G. Williams](https://newton.cx/~peter/) is an astronomer based at the
[Center for Astrophysics | Harvard & Smithsonian][https://cfa.harvard.edu] in
Cambridge, MA. There he serves as the Technical Lead for the [IAU Minor Planet
Center](https://minorplanetcenter.net), which is tasked with gathering,
analyzing, and publishing all worldwide positional measurements of asteroids.
Alongside his astronomical research, which is focused on time-domain radio
surveys, he has a long history of contributing to open-source software projects,
including service as a core member of the
[conda-forge](https://conda-forge.org/) project. Peter is a [2025 Better
Scientific Software
Fellow](https://bssw.io/blog_posts/introducing-the-2025-bssw-fellows).

<!---
Publish: Yes
Track: BSSw Fellowship
Topics: software process improvement, documentation
--->
