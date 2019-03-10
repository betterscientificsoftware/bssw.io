# The Oldest Code on GitHub
## Part 2 of 3: The Apollo Guidance Computer Software

**Hero Image:**

- <img src='https://raw.githubusercontent.com/betterscientificsoftware/images/Blog_AGCPart2_MargaretHamilton.png' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: June, 2019

*Part two of three about the Apollo Guidance Computer commemorating the 50th anniversary of the Moon landing.*

The Guidance, Navigation and Control (GN&C)<sup>[3]</sup> system for Apollo was deemed so
critical, it was the first contract NASA awarded only months after Kennedy's speech
to congress announcing plans for a Moon landing<sup>[4]</sup>. So much of the initial
focus was on the hardware that no one involved at the time, either at NASA or MIT,
had any clue about the monumental software development task that lay ahead.

Before a single line of code had been written, the consequences of failure were painfully
demonstrated during the launch of Mariner 1<sup>[1]</sup>. A bug in the guidance software forced
flight controllers to send it a self-destruct command 294 seconds after launch
($18.5M (153M in 2019 dollars)). Investigations revealed the same bug existed in several
previous Ranger missions<sup>[6]</sup> but luckily did not manifest. Because Mariner had also suffered a
non-critical hardware failure, the guidance software had taken a different logic path, one that had never
been exercised previously. The bug was later found to have originated in the hand-written equations
upon which the guidance software was based; a missing over-bar to indicate the use of average rather
than instantaneous velocity.

The complete GN&C system was much more than
the computer. It involved the

The biggest challenge was that all of these components were being developed almost simultaneously.
Their size, weight, interfaces, performance characteristics and anticipated position within the
spacecraft (which effects things like center of mass, torques, moments, angles, etc.), were constantly
changing. In addition, NASA's expectations for what functions the GN&C system would perform were also
expanding (requirements creep). A lot of the changes were motiviated for increased safety and optimizing
the use of propellents.

Viewed holistically, the GN&C system was a massive feedback control system. Th
Fortunately, early on in the software development, the problem was to understand the equations governing
spacecraft motions and developing numerical algorithms capable of utilizing the available data to estimate
control responses would provide the essentail control 

There was no "secondary memory" in the AGC. All software and data had to fit within the rope memory.

This were primarily a concern during powered flight (velocity changes)...when the main engine. So, a
Moon mission was typically broken down into pieces, each piece focusing on the specifics of the 
velocity manuervers required for that portion of the mission. Those involving motions near the Moon
were the most crucial. Lunar Orbit Insertion...there's an app for that, Lunar Landing...there's an
app for that, Lunar liftoff...there's an app for that and Lunar Orbit Rendevouz.
Abort scenarious . 
Without a doubt, the single most important being Lunar landing and 

There were three major approaches for landing on the Moon by Kennedy's deadline. Each involved
substantially different vehicles and mission scenarios. It would be a full year before NASA had
selected Lunar Orbit Rendevous

The computre was only the brains..(picture). It was a wholly integrated
system with the computer acting as the brains. There was to be no direct control...
all astronaut inputs would go through the computer which would interpret the astronaut
inputs and affect the desired controls.

 Initial estimates
placed required memory for all GN&C tasks for a complete Moon mission at 4k words. That
requirement would be revised 4 times eventually an order of magnitude larger.

In the early 1960s, there were several commercial vendors vieing for lucritive contracts
to build guidance systems for NASA. These included IBM, TRW, RCA and even GM (AC Electronics Division).
(Footnote, Chrystler built Redstone Rocket).

When MIT was awarded the contract to build not only
the guidance computer, but the whole GN&C system (ahead of others in autonomous, inertial guidance
systems). This was the first major contract NASA awarded for the Apollo program.

Requirements evolved as various organizations gained experience in designing, implementing,
testing and actually using the GN&C system.

The key step in development of the software for a mission was the release of a program for
manufacture of the "ropes". This manufacture step took weeks to complete

## Software Development Prior to 1966 SW Task Force Review

## Manpower Levels and Organization

## Coding

In the AGC, time-crtical and other system level routines were coded in MAC languge
(MIT Algebraic Compiler -- a variant of Fortran), and then converted by hand into AGC
assembly code. The AGC's operating system, the Executive, job control, waitlist,
and the Interpreter were all coded this way. On the other hand, most guidance applications
were written in the AGC's interpretive language which is really just a domain specific
assembly language for many of the operations involved in orbital guidance computations.

However, before the code for a given guidance application could be written, weeks or even months
of analysis and design effort would go into the defining equations, control logic and algorithms
for selecting. Once the defining equations were written down and the logic and control flow for
driving them, it was often a relatively simple matter of transcribing the result into AGC
interpretive language. For this reason ... coding ...

    * anecdote about engineers vs. coders

## Testing

Outline
  * Monumental software task (consequences of failure, Mariner 1)
  * Focus on hardware, not software
  * NASA and MIT knew hardware design processes...applied the same development cycle to software
    * By 1968, "software engineering" (Margaret Hamilton)
    * probably one of the earliest examples of the "traditional" software development lifecycle
    * maybe reference SABRE
  * Break Moon mission down into phases (all velocity changes) (There's an app for that)
  * AGC architecture (fixed/erasable, ropes, Executive/Wait List, Interpreter)
  * Memory requirements estimate 4K to 40K
  * The complexities
      * Requirements UNKNOWN: Didn't even know mode of mission
      * List all from vugraph
      * Adding requirements
      * massive feedback control loop
      * contingencies, safety
      * maintain two systems Block I and block II
  * The performance portability problem
  * Testing plans
    * Eraseable memory programs
  * "Program" release, GSOP, rope core manufacture
  * First fly by wire ever attempted
  * How the software was actually written
      * Example code
      * anecdote about coders vs. engineers
  * Evolving Mission enhancements
      * Faster rondevous
      * Greater accuracy
      * Lesser fuel margins
      * More weight (lunar rover)
  * User interface
  * Luminary and Collosus
  * Interesting stuff
    * Auto-documentation
    * Other companies wanting to take the job
    * bit-for-bit simulation, reproducibility
    * user stories
    * Transition from triage to optimization after Apollo 1 fire delays
    * Manpower and coders


Notes:
* The software development enironment (writing the code...equations, transcribed to 1
   * Breaking down a mission into steps (velocity changes)
   * Multiple computers
      * SLVDC (IBM), AGS (TRW), 
   * AGC CPU, Erasable and Fixed Memory, Executive & Waitlist, Interpreter, Restart Facilities
   * Engineers design algorithms and code
   * Key goal: produce the ropes
   * Huguely memory constrained.
* Some possible high-level relationships to modern day development
  * auto-doc tools
  * bit-for-bit simulation
  * reproducibility
  * What does CI/CD look like then? Were they doing it? Kinda, they would do full-up simulator tests, patches, reruns
  * introducing the term "software engineering" (makes a lot more sense for an embedded system)
  * Release notes (revision numbers), number of revisions
  * names of software
  * JIT ropes
  * Transition from triage to optimization after Apollo 1 fire delays
  * How code teams were organized
  * Continuous integration
  * No definitive descriptions of day to day life of software developers on AGC
  * User stories and epics?
  * note about using math/engineers to write code 
  * Anecdote about IBM changing one line of code
* What are key differences to HPC
  * embedded
  * REAL TIME
  * tight memory constraints
  * time constraints too (time and space performance)
  * safety, reliability
  * requirements, interfaces, languages changing under development
  * a feedback control system (complicated)
  * dealing with variety of safety contingencies

The AGC software is available on GitHub. In all likelihood, it is the oldest (working) code on
GitHub, part of the Virtual AGC Project.

By the time this blog article is published, Tesla will have patented a new "AI CPU"
to support autonomous nagivation of all Tesla cars. Its part of AutoPilot 3.0. Thats right,
autonomous navigation is a big enough challenge for auto-makers that Tesla has been designing
and manufacturing its own computing technology (hardware and software) to do it. And, this is at relatively slow
speeds (say less than 250kph), on the Earth's 2D surface, over modest distances, say several hundred
kilometers, and with the help of GPS, high resolution maps, ...

Now, imagine the challenges at speeds of 40,000 kph, distances of 400,000 km in 3 dimensions
with no GPS or high resolution maps and with re-entry and orbital insertion tolerances of less
than 1`part in 100,000.

Relate rope core weaving to "agile"

Detail the architecture a bit more
    16 bit, central registers
    I/O channels
    peripheral devices
    block diagram
    executive
    waitlist
    interpreter
    checklists


How was mission divided up into pieces and then apps for each piece
concept of pair programming, peer review, pull requests (same abbreviation PR)

Relationship to astronaut checklists

cycle stealing

One of the newest 

Describe the executive and how it operates (process model)

Auto-documentation tool for checklists

using 22/7 as approx. for PI, including 3rd and 4th harmonics (tindalgram) of earth oblateness

Apollo 1 Fire effect on software schedule

bug tracking = descrepency reporting. (tindalgrams, http://web.mit.edu/digitalapollo/Documents/Chapter7/tindallgrams.pdf, http://tindallgrams.net)
all tindallgrams, http://www.collectspace.com/resources/tindallgrams/tindallgrams02.pdf

Names of computer programs

Constantly changing requirements...interface data.

Each mission different...early missions designed to test systems in off-nominal and contingency settings, provide data
on performance to be fedback and used to revise software used in later missions.

Massive feedback control loop...stability is a huge issue

Agile "ropes"...just in time rope manufacture. Manufacturing ropes is the critical step.

Tindall was basically a systems integration engineer

Looking for everything that could reasonably be eliminated to fit into memory

Traing crew in reading Octal

saturation of honeywell test systems...IBM 360 delivery, MAC compiler (Fortran)

attempt to delete DPS backup of SPS

Advantage of standardized procedures outweigh potential benefits in different abort scenarios

There is a sense that there is a massive optimization problem being solved.

DAta format issues with sub-contractors

Everything involving GNC "events"

Jack Garman interview, https://www.honeysucklecreek.net/interviews/jack_garman.html

Great article on simulations, http://jakob.engbloms.se/archives/2520

There was an app for that...

Great article on Margaret Hamilton, https://hackaday.com/2018/04/10/margaret-hamilton-takes-software-engineering-to-the-moon-and-beyond/, award ... ttps://www.hq.nasa.gov/alsj/a11/a11Hamilton.html

Example of scrums, agile list, http://www.ibiblio.org/apollo/Documents/LUM56_text.pdf

https://www.extremetech.com/computing/274795-tesla-dumps-nvidia-goes-it-alone-on-ai-hardware

Apollo 12 landing, http://www.ibiblio.org/apollo/Documents/LUM102_text.pdf

apollo 11 in detail https://www.doneyles.com/LM/Tales.html

quote from software document

    Each training session related to a particular mission and onboard program. Although particularly beneficial from the crew's point of view, this policy placed a sizable burden on MIT engineers at those times when crew briefing conflicted with
program release. A possible alternati-~ewould have been to have two or three persons devotingftheir energie; to understanding the entire G&N system, solely for crew-training purposes. However, the extremely rapid change and development of onboard programs made this a virtuzlly impossible task.



power used by self-driving cars...

https://www.wired.com/story/self-driving-cars-power-consumption-nvidia-chip/

history of self driving cars..

https://www.wired.com/story/guide-self-driving-cars/

https://electrek.co/2018/08/01/tesla-chip-most-advanced-computer-autonomous-driving-autopilot-hardware-3-update/

Just last month, Tesla announced 
Aparently, Autonomous navigation is a challening problemZZ

Possible angles
  - Autonomous cars, navigation
  - Apollo 12 landing accuracy, software update for two sites
  - Testing software

This is the second of three articles about the Apollo Guidance Computer. In this article we focus
on the effort to develop the software. Each Apollo mission had unique requirements often demanding
mission-specific software to be developed.

Mark Miller is a computer scientist supporting [WSC](https://wci.llnl.gov/about-us/weapon-simulation-and-computing)
program at [LLNL](https://www.llnl.gov) since 1995.
He is a contributor to
[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit)
and the lead developer of
[Silo](https://wci.llnl.gov/simulation/computer-codes/silo)
supporting scalable I/O of LLNL HPC simulations. He has contributed
to various scientific database technologies including
[ASCI-DMF](https://e-reports-ext.llnl.gov/pdf/234737.pdf),
[HDF5](https://support.hdfgroup.org/HDF5/),
[ITAPS](http://www.scidac.gov/math/ITAPS.html),
[MACSio](https://codesign.llnl.gov/macsio.php).
Mark's interests include data models and their impact on software
interoperability, high performance I/O and Software Quality Engineering
([Smart Libraries](https://wci.llnl.gov/codes/smartlibs/UCRL-JRNL-208636.pdf)) for HPC libraries.

New References
[1]: https://en.wikipedia.org/wiki/Mariner_1#Overbar_transcription_error
[2]: http://catless.ncl.ac.uk/Risks/8.75.html#subj1
[3]: https://en.wikipedia.org/wiki/Apollo_PGNCS
[4]: https://youtu.be/TUXuV7XbZvU

Examples of interpretive code...

[5]: https://www.ibiblio.org/apollo/hrst/archive/1687.pdf

[6]: https://en.wikipedia.org/wiki/Ranger_program

Old References

[101]: https://www.nasa.gov/mission_pages/apollo/missions/apollo11.html
[102]: https://en.wikipedia.org/wiki/Moon_landing
[104]: ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf
[105]: https://en.wikipedia.org/wiki/Apollo_Guidance_Computer
[106]: https://youtu.be/YIBhPsyYCiM
[107]: https://pdfs.semanticscholar.org/0d44/2a1b41da2ccbffeda8aa2e1a7c2417ac71e0.pdf
[109]: https://www.ibiblio.org/apollo/hrst/archive/1713.pdf
[1010]: https://en.wikipedia.org/wiki/IBM_System/360_Model_20
[1011]: http://www.bitsavers.org/pdf/ibm/360/fe/GC22-6820-12_System_360_Installation_Manual_Physical_Planning.pdf
[1014]: https://www.ibiblio.org/apollo/klabs/history/history_docs/r713.pdf
[1015]: https://youtu.be/P12r8DKHsak
[1016]: ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf
[1017]: https://en.wikipedia.org/wiki/Magnetic-core_memory
[1018]: https://en.wikipedia.org/wiki/Core_rope_memory
[1019]: https://youtu.be/xx7Lfh5SKUQ
[1022]: https://www.computerhistory.org/revolution/real-time-computing/6/128/529
[1023]: https://en.wikipedia.org/wiki/Fairchild_Semiconductor
[1025]: https://www.ibiblio.org/apollo/hrst/archive/1033.pdf
[1026]: ftp://ssh.esac.esa.int/pub/ekuulker/Apollo15/The-Apollo-Guidance-Computer-Architecture-and-Operation.pdf
[1028]: https://www.ornl.gov/news/ornl-launches-summit-supercomputer
[1029]: https://www.top500.org/green500/list/2018/11/
[1030]: https://en.wikipedia.org/wiki/ILLIAC_IV
[1040]: https://en.wikipedia.org/wiki/Jacquard_loom#Importance_in_computing
[1041]: https://www.ibiblio.org/apollo/klabs/history/history_docs/r713.pdf
[1042]: https://hpc.llnl.gov/hardware/platforms/sierra
[1043]: https://www.computerworld.com/article/2525898/app-development/nasa-s-apollo-technology-has-changed-history.html
[1044]: https://airandspace.si.edu/stories/editorial/apollo-guidance-computer-and-first-silicon-chips
[1045]: https://www.ibm.com/us-en/marketplace/power-systems-ac922
[1046]: http://www.computersciencelab.com/ComputerHistory/HistoryPt2.htm
[1047]: https://youtu.be/P12r8DKHsak?t=35


new tesla chip, https://electrek.co/2019/01/25/teslaf-patents-ai-chip-autopilot-hardware-3-0/


<!---
Image copyright source info…
  Two are public domain...
      * https://commons.wikimedia.org/wiki/File:NASA_spacecraft_comparison.jpg
      * https://en.wikipedia.org/wiki/Apollo_Guidance_Computer#/media/File:Agc_view.jpg
  The Raytheon image I recieved approval email from Raytheon customer relations
--->

<!---
Publish: preview
RSS update: 2019-05-15
Categories: performance
Topics: high performance computing, performance portability
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->
