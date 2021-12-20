Outline (notes to self)
1. where did m/s come from
2. How much effort to change?
3. What effort was involved?
4. What's next

Towards the end of the 2020 calender year, two flagship DOE simulation projects, Ale3d at LLNL and Sierra at SNL, completed updates to replace the use of master/slave terminology throughout their projects.

If the work involved nothing more than just a simple, global, textual replacement of the words "master" and "slave", there wouldn't be much reason for writing about the experience here.
This work involved changes to source code, dependency interfaces, documentation, test input parameter files and test data files as well as how developers and users alike talk about features of the code where this terminology is used.

However, master-slave terminology is rather *pervasive* not simply within these two projects but throughout scientific computing in general.
It appears in many HPC/CSE contexts such as..

* slide surfaces (https://abaqus-docs.mit.edu/2017/English/SIMACAEITNRefMap/simaitn-c-contactpairform.htm)
* shell-solid element interfacing (https://www.dynasupport.com/tutorial/contact-modeling-in-ls-dyna/contact-types)
* parallel runtime execution models (http://charm.cs.uiuc.edu/research/masterSlave)
* periodic boundary conditions (https://www.researchgate.net/figure/Master-slave-set-up-for-periodic-boundary-conditions-on-VE-with-a-non-periodic-mesh-see_fig3_320079614)
* file systems (https://activemq.apache.org/shared-file-system-master-slave)
* hard drives (https://computer.howstuffworks.com/ide.htm)
* grid computing (https://sites.cs.ucsb.edu/~rich/publications/shao-hcw.pdf)
* graph traversal (https://dl.acm.org/doi/abs/10.1145/3350546.3352536)

The terminology may have [taken root](https://www.cise.ufl.edu/~sahni/papers/masterslave2.pdf) in technology in the 1940s.
Using [Google's NGram viewer](https://books.google.com/ngrams/graph?content=master-slave&year_start=1800&year_end=2019&case_insensitive=on&corpus=26&smoothing=3&direct_url=t4%3B%2Cmaster%20-%20slave%3B%2Cc0%3B%2Cs0%3B%3Bmaster%20-%20slave%3B%2Cc0%3B%3BMaster%20-%20Slave%3B%2Cc0%3B%3BMaster%20-%20slave%3B%2Cc0%3B%3BMASTER%20-%20SLAVE%3B%2Cc0), there is a sharp rise in the use of *master/slave* terminology beginning in the 1940's where it was used by [Raymond Geortz](https://en.wikipedia.org/wiki/Raymond_Goertz) to describe a [remote manipulator](https://en.wikipedia.org/wiki/Remote_manipulator) which is a sort of robotic version of a [glove box](https://en.wikipedia.org/wiki/Glovebox).

In HPC/CSE software the prolific use of the terminlogy often manifests in the names of data types, variables, functions, files, images, GUI widgets, databases, command-line arguments, URLs, servers, documentation, and publications as well as people's mental models and abstractions for talking about objects, algorithms and software or hardware architecture.

Members of both projects including even managers had a long-standing interest in replacing master/slave terminology in their respective projects.
However, mustering the motivation, resources and the critical mass to make it happen remained elusive.
Then, the summer of 2020 happened...
The whole country once again turned its attention to talking about racially-oriented inequities of our society.
This included the world of technology and software.
Gabriel read an article about master/slave terminology in technology and approached project leadership for Sierra about addressing it.

For Ben on the Ale3d project, the catalyzing event was a dependency announcing its plans to replace "master/slave" with "primary/secondary".
For NNSA labs, the terms "primary" and "secondary" typically refer to the major components of a thermonuclear weapon.
Their presence is often accompanied by requirements for handling classified information.
Although the terms "primary" and "secondary" are not themselves classified, using them as prolificly as "master/slave" have been used would present significant challenges in ensuring clean and clear separation between classified and UNclassified information.
Ben felt it was important to get out ahead of these plans and facilitate broader dialog on more workable alternative terms.
In the Ale3d project, "master/slave" terminology was restricted almost entirely to their implementation of slide surfaces where two different parts in a real-world object maintain surface-contact but move relative to each other.
After negotiations with various stakeholders, a suitable replacement for that was simply "Side A" and "Side B".
However, to be thorough Ben felt it was important to replace the terminology everywhere it or it derivatives existed.
In the source code `nslv` might be used as a variable representing the number of slaves.
To reliably replace all such cases required careful study of the code by human eyeballs.
For Sierra, "master/slave" terminlogy was for multiple different topical areas including contact surfaces, 

Apart from the practical aspects of changing code, documentation, test data, there was also effort required in getting all stakeholders to agree to the changes and support the work involved in completing it. 

When the teams began this work, the total effort and resources required to complete were not well known.
The total effort only revealed itself as dominos began to fall.
In addition, no new resources were allocated to complete the work.
The teams had to forego other activities in order to prioritize and complete this work.

