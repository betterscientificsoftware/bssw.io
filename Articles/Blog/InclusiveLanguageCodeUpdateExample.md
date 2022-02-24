# Experiences replacing `master/slave` terminology in ALE3D and Sierra

<!-- deck text start -->
What is involved in replacing pervasive language representing barriers to being more inclusive?
<!-- deck text end -->

#### Contributed by [Mark C. Miller](http://github.com/markcmiller86 "Mark C. Miller")
#### Publication date: Feb 24, 2022

One way software projects address inclusion is to identify and improve language used in their projects representing barriers to inclusion.
An unfortunately [prolific](https://github.com/search?q=master+slave&type=code) and unmistakably [problematic](https://www.wired.com/story/tech-confronts-use-labels-master-slave/) example in HPC/CSE projects is the use of `master/slave` terminology.

The terminology may have [taken root](https://www.cise.ufl.edu/~sahni/papers/masterslave2.pdf) in technology in the 1940s.
Examination of [Google's NGram viewer](https://books.google.com/ngrams/graph?content=master-slave&year_start=1800&year_end=2019&case_insensitive=on&corpus=26&smoothing=3&direct_url=t4%3B%2Cmaster%20-%20slave%3B%2Cc0%3B%2Cs0%3B%3Bmaster%20-%20slave%3B%2Cc0%3B%3BMaster%20-%20Slave%3B%2Cc0%3B%3BMaster%20-%20slave%3B%2Cc0%3B%3BMASTER%20-%20SLAVE%3B%2Cc0) shows a sharp rise in its use beginning with [Raymond Geortz's](https://en.wikipedia.org/wiki/Raymond_Goertz) description of a [remote manipulator](https://en.wikipedia.org/wiki/Remote_manipulator), which is a sort of robotic version of a [glove box](https://en.wikipedia.org/wiki/Glovebox).

Regardless of origin, the terminology has become *pervasive* throughout scientific computing as well.
It appears in many HPC/CSE contexts such as [slide surfaces](https://abaqus-docs.mit.edu/2017/English/SIMACAEITNRefMap/simaitn-c-contactpairform.htm), [shell-solid element interfacing](https://www.dynasupport.com/tutorial/contact-modeling-in-ls-dyna/contact-types), [parallel runtime execution models](http://charm.cs.uiuc.edu/research/masterSlave), [periodic boundary conditions](https://www.researchgate.net/figure/Master-slave-set-up-for-periodic-boundary-conditions-on-VE-with-a-non-periodic-mesh-see_fig3_320079614), [file systems](https://activemq.apache.org/shared-file-system-master-slave) and [hard drive technology](https://computer.howstuffworks.com/ide.htm), [grid computing](https://sites.cs.ucsb.edu/~rich/publications/shao-hcw.pdf), and [graph traversal](https://dl.acm.org/doi/abs/10.1145/3350546.3352536) to name just a few.

On the one hand, `master/slave` terminology is often used, however imprudently, as a metaphor to hint at some basic aspects of an algorithm.
On the other hand, the metaphor often fails miserably in conveying even the basics *accurately*.

For example, in modern slide surface algorithms where two objects come into *contact* and interact along a shared boundary (e.g. a tire rolling along a road), the object designated as a `master` typically does not actually have the effect of dictating the behavior of any other object designated as a `slave`.
Instead, in modern slide surface algorithms all objects act as *peers* and an updated state is computed where all object's contributions are typically treated *equally*. 
In other words, the basic relationship between the objects is hardly one that is any way similar to the relationship between a `master` and a `slave`.

In HPC/CSE software, use of the terminology can manifest in the names of data types, variables, functions, files, images, GUI widgets, databases, command-line arguments, URLs, server names, documentation, and publications as well as people's mental models and abstractions for talking about objects, algorithms and associated software or hardware architecture.

Towards the end of the 2020 calendar year, two flagship DOE simulation projects, [ALE3D](https://wci.llnl.gov/simulation/computer-codes/ale3d) at [Lawrence Livermore National Lab](https://www.llnl.gov) and [Sierra](https://www.sandia.gov/asc/advanced-simulation-and-computing/integrated-codes/) at [Sandia National Lab](https://www.sandia.gov), completed updates to replace the use of `master/slave` terminology throughout their projects.
The work was spearheaded by [Ben Liu](https://scholar.google.com/citations?user=pA2ybRwAAAAJ&hl=en) of the ALE3D team and [Gabriel Jose de Frias](https://www.osti.gov/search/author:%22de%20Frias,%20Gabriel%20Jose%22) of the Sierra team.

If the work had involved only a global, textual replacement of the words `master` and `slave`, there would not have been much reason for writing about it here.
The work involved changes to source code, dependency interfaces, documentation, test input parameter files and test data files as well as how developers and users alike talk about features of the code where this terminology was previously used.

Managers within both projects had a long-standing interest in replacing `master/slave` terminology.
However, they recognized, wisely, that such activities are far more likely to succeed when they happen organically rather than by management mandate.
Finding a champion, as well as mustering the consensus and resources to take on the work, remained elusive.
Then, the summer of 2020 happened.
The whole country was engaged in dialogue about racially-oriented inequities of our society.
This included the world of technology and software.

Apart from the practical aspects of changes to code, documentation, test data, etc., there was also effort required in getting all stakeholders to agree to the changes and support the work involved in completing them. 

When the teams began the work, the total effort and resources required to complete were not well known.
The total effort only revealed itself as dominoes began to fall.
In addition, no new resources were allocated to complete the work.
The teams had to forego other activities in order to prioritize and complete this work.

### Ben Liu and ALE3D

<!-- the following remarks were reviewed for any classification issues by Paul Amala -->
For Ben on ALE3D, a decisive moment came when [Benjamin Spencer](https://github.com/bwspenc), a developer on the [MOOSE](https://mooseframework.inl.gov) project at [Idaho National Lab](https://inl.gov), announced plans to replace `master/slave` with [`primary/secondary`](https://github.com/idaholab/moose/issues/15457).
This action was intended to encourage collaborators to consider replacing the terminology and to broaden consensus on common replacement terms.

Within the [NNSA labs](https://www.energy.gov/nnsa/national-nuclear-security-administration), the terms `primary` and `secondary` are commonly associated with the major components of a [thermonuclear weapon](https://cgsr.llnl.gov/content/assets/docs/CGSR_NW101_Policy_Wonks_11-04-21_WEB_v5.pdf?#page=19).
Their presence is often accompanied by classified information handling requirements.
Although the terms `primary` and `secondary` are not themselves classified, using them as prolifically as `master` and `slave` have been used would present significant challenges in ensuring clean and clear separation between classified and unclassified information.

In addition, to be thorough, Ben felt it was important to replace not only `master` and `slave`, but also any instances of terminology that *derived* from them.
For example, in the source code `nslvs` (or even `ns`) might be used as a variable representing the number of slave surfaces or in a data file `M_tire` and `S_Road` might be used to indicate the tire object played the role of a `master` slide surface and the road object the role of a `slave` slide surface.
Although automated tooling handled the *common* cases, to reliably replace *derivative* terminology required careful study and manual editing.

1. *Where was the `master/slave` terminology used in the code?*

   > It was restricted almost entirely to our implementation of slide surfaces.
   > After discussions with numerous stakeholders, everyone agreed a suitable replacement was simply *Side A* and *Side B*.
   > That is somewhat specific to slide surfaces but nonetheless worked for all our cases.
 
2. *Did your efforts exploit automated tooling or workflows to complete the changes?
   Was it all sort of manual or maybe `grep` and `sed` scripts?*

   > We used `sed` scripts to help update the code and the manual.
   > We didn't use any compiler tools other than attempting a compile, failing, and fixing it (for the times when the scripts were incorrect).
   > An extensive pull request was used to identify additional (mostly comment and variable naming) changes.
   > A number of other developers on the team were very thorough in looking through this.
 
3. *About how many files and lines of code wound up having to change?*

   > 200+ files, 1200+ lines of code – this is just for data members, more for local variables.
 
4. *Are you aware of any bugs that were introduced due to this effort?*

   > We are not aware of any bugs that we introduced due to this.
 
5. *Were changes to data files, input decks, power-point slides and/or documentation also needed?*

   > Manual documentation changes were mostly limited to one or two chapters.
   > Changes to PowerPoint files are still in progress.
 
6. *How was the change ultimately announced and rolled out to stakeholders?*

   > We sent out a message to major users ahead of the update.
   > With the new release, there was an announcement of major new features/changes that went out with the release.
   > We have been announcing this change as *upcoming* during our training sessions covering slide surfaces.
 
7. *What role did the social climate in the country in the middle of 2020 play?*
 
   > I think that it brought more awareness (to a broader segment of the population) to how systems and language can reinforce and propagate injustice and oppression.
   > In particular, how seemingly little things can add up (microaggressions, etc).
   > For myself, this really made me more aware of the need to change this.
   > I think this was also true for other developers and users.
   > I think the broader social climate helped provide momentum to push through the tedium and address resistance to change.
   > In particular, knowing that Sandia and Idaho National Lab were also working on this helped give me the confidence I needed to continue in what I was doing.
   > Our work on replacing `master/slave` doesn't necessarily "move the needle" much.
   > But, my hope is that it can lead to more substantive change (things like hiring, pipeline, etc.).

8. *How was the work on this funded?*

   > There was no new funding provided to complete this work.
   > We needed to adjust other priorities to fit it in.
   > Nonetheless, management was fully supportive of it.

9. *Did you have a good understanding of what was involved going in?*

   > Not really.
   > The actual coding time needed to change the code and documentation wasn't the main concern.
   > The challenge was in having the dialog essential to bring all stakeholders on board.
 
### Gabriel Jose de Frias and Sierra

For Gabriel on Sierra, a decisive moment came after reading an online article about `master/slave` and approaching Sierra project leadership about addressing it in their code base.

1. *Where was the `master/slave` terminology used in the code?*

   > Contact surfaces (e.g. slide surfaces) were the main capability where the terminology was used in Sierra, but it was also used in multi-point constraints, periodic boundary conditions, and shell-solid joint code.

2. *Did your efforts exploit automated tooling or workflows to complete the changes?
   Was it all sort of manual or maybe `grep` and `sed` scripts?*

   > We used refactoring options in the Eclipse IDE to modify the code.
   > Python scripts to modify input files from tests, which were also made available for users to apply to their files.
 
3. *About how many files and lines of code wound up having to change?*

   > This is a bit hard to answer.
   > Hundreds of files mostly in tests, and some in code, scripts, user manuals and training.
   > The number of lines could be above 1000, but this is a very rough estimate.
 
4. *Did any bugs creep in that resulted in debugging effort to resolve?*

   > No bugs that we know of.
 
5. *Were changes to data files, input decks, power-point slides and/or documentation also needed?*

   > Yes, we made a handful of changes to user manuals and trainings.
 
6. *How was the change ultimately announced and rolled out to stakeholders?*

   > Through sprint reviews every 3 weeks.
   > We involved analysts and developers in ongoing conversations.
 
7. *What role did the social climate in the country in the middle of 2020 play?*

   > The protests made me think more about what I’m doing in my day-to-day to become a better member of society.
   > Am I educating myself enough about these issues?
   > Am I putting myself in other people’s shoes?
   > Am I considering my own biases in my opinions and thoughts?
   > I came across the [_Washington Post_](https://www.washingtonpost.com/opinions/2020/06/12/tech-industry-has-an-ugly-master-slave-problem/) opinion piece trying to answer some of these questions...trying to get a different perspective from my own, and those around me.
   > I would like to think these efforts allow other people to ask similar questions.
   > That they motivate thoughtful discussions about topics that are considered taboo to discuss with your co-workers, or even your friends and family.

8. *How was the work on this funded?*

   > It originally started as grass-roots effort in the Solid Mechanics development team and was eventually embraced by stakeholders and other development teams when we shared what we were doing.

9. *Did you have a good understanding of what was involved going in?*

   > Agreeing on the replacement terminology certainly took longer than I expected.
   > That ended up being a good thing since it prompted us to open up the conversation with several teams at Sandia and even other DOE labs.

### Closing thoughts

While there was [much discussion](https://www.google.com/search?q=%22master%22+%22slave%22+terminology+in+software&sxsrf=AOaemvIy5OkrC1xJEV_CJrUNIG3Tvmtlrg:1643308409486&source=lnt&tbs=qdr:y&sa=X&ved=2ahUKEwjdlYPwyNL1AhVuD0QIHXqoBOsQpwV6BAgBEBk&biw=1616&bih=948&dpr=1) of the `master/slave` issue in the media throughout 2020, it has been a [known](https://tools.ietf.org/id/draft-knodel-terminology-00.html) and [long-standing](https://www.jstor.org/stable/40061475) issue long before 2020, with the earliest online mentions going back [nearly 20 years](http://www.cnn.com/2003/TECH/ptech/11/26/master.term.reut/index.html), and other public discourse almost certainly much earlier.

Beginning in 2021, less than a year after the summer of 2020, the broader US public has seen what can only be described as a [*backlash*](https://fivethirtyeight.com/features/white-backlash-is-a-type-of-racial-reckoning-too/) against these and other [DE&I efforts](https://sloanreview.mit.edu/article/fighting-backlash-to-racial-equity-efforts/).
Hopefully, the community will resist this [habit](https://www.tandfonline.com/doi/full/10.1080/10705422.2021.1998875) and continue to practice and make progress in making HPC/CSE more inclusive.

Some readers may wonder if the people spearheading the efforts described here were [BIPOC](https://www.healthline.com/health/bipoc-meaning).
Yes, they were.
Hopefully, the community will recognize the importance of unburdening our BIPOC colleagues from having to always be the ones doing the heavy lifting in efforts aimed at making HPC/CSE more inclusive.
On the other hand, we must also take care that when we engage in such work, we do so with a commitment of ensuring the voices of our BIPOC colleagues are informing priorities and process.

Given the current social justice climate in which we all operate, some readers may feel that inclusive language efforts are nowhere near enough to meet the moment and are really just a [distraction](https://www.wired.com/story/tech-confronts-use-labels-master-slave/) from bigger issues.
It's hard to argue with that.
Nonetheless, others may feel like such efforts go way too far.
While we can acknowledge both perspectives exist, it is worth considering that when we’re [accustomed](https://www.huffpost.com/entry/when-youre-accustomed-to-privilege_b_9460662) to the status quo, being called to invest effort to be more inclusive may feel like oppression.

<!---
Publish: yes
Pinned: no
Topics: Software process improvement, Documentation, Strategies for more effective teams
RSS update: 2022-02-24
--->
