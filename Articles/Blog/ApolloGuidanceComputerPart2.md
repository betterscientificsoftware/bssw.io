# Celebrating Apollo's 50th Anniversary: The Oldest Code on GitHub

**Hero Image:**

 - <img src='../../images/Blog_0615_Apollo2.jpg' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: June 17, 2019

*Second of a three-part series to commemorate the 50th anniversary of the Moon landings.*

Retrocomputing enthusiasts recently uploaded Apollo Guidance Computer (AGC)
source code for various Apollo missions to GitHub. There is even a *Virtual AGC*
that can run this code.<sup>[7]</sup> In all likelihood, it is the oldest *active* code on
GitHub. Remarkably, its development began over half a century ago in the ashes
of Mariner 1, a Venus probe destroyed shortly after launch because of a bug in its
guidance software.<sup>[15],[35]</sup> The prevailing explanation was that in the
transcription of hand-written guidance equations into a software specification
for the contractor, TRW, an overbar to indicate the use of *average* rather than
*instantaneous* velocity went missing, and along with it an $18M
probe ($152M in 2019 dollars) and a regrettable ration of American prestige.
How would MIT and NASA avoid similar mistakes developing software for the AGC?

This is the second of three articles about the AGC. In [part 1](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap), we described the
hardware.<sup>[20]</sup> Here, in part 2, we focus on MIT's effort to develop
the software.<sup>[4],[12],[36]</sup>
As in part 1, the scientific computing community will recognize
some familiar themes such as the benefits and challenges of *co-design*, the importance of
sufficient testing resources, the role and impact of software process
improvements and more.

### Extreme co-design
Initially, about all that was known with any certainty was that a digital
computer would be the centerpiece of a complex collection of GN&C subsystems.
A year would pass before NASA selected the Lunar Orbit
Rendezvous<sup>[37]</sup> (LOR) mission plan involving two separate
and substantially different vehicles each with its own AGC.
AGC software would control everything. Even so-called manually controlled inputs would first
pass through AGC software before affecting the relevant hardware making
the Apollo spacecraft the first all-digital *fly-by-wire*<sup>[49]</sup> vehicles ever created.

![](../../images/Blog_0619_agc_and_spacecraft3_C.jpg)

A challenge in developing the software was that all the GN&C subsystems
pictured above were under development *simultaneously*
right along with the software itself. Their interfaces, performance
characteristics, size, weight and position within the spacecraft, all of
which affect key parameters in the guidance equations, were constantly evolving.
Even techniques to manage the
software effort were under development and evolving with the
software. Eventually, NASA would pressure MIT to adopt techniques pioneered
by IBM to help manage large software development projects.

Today, we would call all of this simultaneous development activity
*co-design,*<sup>[8],[9],[23]</sup> and it has a lot of advantages.
But, in the 1960s when there were no DevOps<sup>[38]</sup> best practices and collaborative tools
such as GitLab, Jenkins, Confluence, Kanban and WebEx, or even email, it presented a massive
coordination and management challenge.

### Evolving requirements, versions and flight rope releases
NASA had established a need for the machine and had determined its general tasks, and
MIT received a contract based on only a short, very general requirements statement.
Requirements started changing immediately and continued to change throughout the program.<sup>[39]</sup>

Midway through development, the AGC was redesigned to support more memory and an expanded
instruction set.
The original and redesigned systems were different enough that each required separate software
development teams, a situation that only worsened already strained resources.
The redesigned AGC had only 2K words of *erasable* core and 36K words of *fixed*
or *rope core* memory. All software and data had to fit into this combined 76KB of memory.

The essential step for software developers was to produce a flight program or rope
and release it to Raytheon for rope core  manufacture approximately 4 months prior to launch:
2 months to manufacture the ropes followed by 2 months for installation in the spacecraft,
checkout, integrated system testing, crew rehearsals and final erasable memory load.

MIT needed to deliver flight programs for ~30 Apollo flights (crewed and uncrewed),
many with unique guidance requirements, planned between 1966 and 1972.<sup>[40]</sup>
The lead engineer in coordinating and approving a completed flight program was
called a *rope mother* and would also name the release. Early on, the names were fairly
creative, including ECLIPSE, SUNRISE, RETREAD and AURORA. Eventually,
NASA put a stop to this, and only the names COLOSSUS and LUMINARY together
with their revision numbers would be used to identify CM and LM flight programs,
respectively.<sup>[24]</sup> LUMINARY 1A is the revision used in the first lunar
landing of Apollo 11.

### The AGC software stack
Each flight program involved a combination of common utilities and mission-specific
space guidance subroutines. Mission-specific components required significant
analysis and development time. Early development activity, 1961–1965, focused on
infrastructural software.

Program Name | Purpose | Size (AGC words)
:--- | :--- | ---:
Executive<sup>[25]</sup> | Priority-driven large/long-running process manager | ~350
Waitlist<sup>[26]</sup> | Time-sequenced small/short-running process manager | ~300
Down-Telemetry<sup>[29]</sup> | Transmit system data to ground | ~200
Restart<sup>[30],[31],[32]</sup> | Error recovery and restart protection | ~1225
Interpreter<sup>[27]</sup> | Space guidance domain-specific programming language interpreter | ~2200
DSKY I/O<sup>[28]</sup> | Cockpit displays and keypad | ~3500
Combined Total | 22% of fixed memory | ~7775

<br>

![](../../images/Blog_0619_agc_sw_stack2_B.jpg)

These programs constituted what we might call today the *Apollo guidance software stack*.
All were implemented in assembly language. By 1965, most of this code had been
written and fully tested and changed little with each new flight program. All
higher level space guidance routines were implemented primarily in the Interpreter
language<sup>[13]</sup> but also by using some of these lower-level pieces.

An example of a space guidance subroutine is computing the relative positions of Earth,
Sun and Moon at any moment. After evaluating options<sup>[34]</sup> in MAC<sup>[50]</sup> or Fortran on 
mainframe systems, developers settled on an approach using 8th-degree polynomial fits to
time-varying positional data predicted from mainframe solution of the 3-body (Earth, Sun, Moon)
problem. Eight double-precision X, Y and Z polynomial coefficients, 48 words of data,
fitting a 2-week period of Moon position data would
then be stored in fixed memory. Another example is a list of stars<sup>[47]</sup>
and spatial positions used with the Apollo space sextant<sup>[33]</sup>
requiring 112 words.<sup>[41]</sup> This data
and code would be among the 76 kilobytes of a flight program
hand woven into rope core in the months before launch. For time-sensitive data,
multiple ropes for different launch windows would be manufactured as contingencies.
A 1962 memo<sup>[19]</sup> lists 45 major software analysis efforts then
underway for various aspects of planned Apollo missions.

### The AGC had an app for that
Flying to the moon and returning safely involved long periods of boredom
punctuated by moments of extreme peril. A mission was divided into phases by
*velocity change maneuvers* or *burns* of the main engines<sup>[1]</sup>. A complete mission
involved around 11 burns. For each maneuver
there was a corresponding *major mode program*, to handle it.
For every phase of the mission, *the AGC had an app for that*.<sup>[45]</sup>

By far the most critical sequence of maneuvers occurred during lunar landing.
It was divided into four phases (pictured below left) depending on the balance of
automated and manual control the astronauts required: Powered Descent
(major mode P63), Approach (P64), Terminal Descent (P66) and Touchdown (P68).<sup>[5]</sup>
Examples of other major mode programs were Trans Lunar Injection (P15), 
Return To Earth (P37) and Ballistic Re-entry (P66).

Development of a major mode program began with an analysis of the relevant equations
of motion and an assessment of available computational approaches to affect the
desired velocity change (magnitude and direction) subject to numerous considerations 
including zero gravity fuel slosh; changing center of mass due to fuel consumption;
main engine performance characteristics; sensor drift and deadbands (e.g. IMU gimbal lock);
optimizing use of RCS propellants; contingencies for failed (on or off) RCS thrusters;
the Moon's lump gravity field;<sup>[2],[3]</sup> and precision timing to coordinate
a planetary ballet of Earth, Moon, Sun and multiple spacecraft and the lines of sight
of communications between them and mission control.

![](../../images/Blog_0619_agc_major_modes_B.jpg)

### Performance portability and the digital autopilot (DAP)

Digital Autopilot (DAP) software was developed based on *Kalman Filtering*.<sup>[42]</sup>
The computation is decomposed into a *prediction* phase where an idealized model
of the spacecraft is used to estimate the current state. In the second phase, noisy
direct measurement of system state from spacecraft sensors is compared with the
predicted state to produce control decisions.

A key challenge was ensuring that a single implementation of DAP software would provide
effective control given a wide variety of spacecraft configurations and operating
scenarios. Doing so presented what we would call a *performance portability*
problem.<sup>[10]</sup> Software developers made DAP execution configurable through a
number of parameters. Prior to a burn, astronauts would follow a checklist setting
a number of switches and entering data on the DSKY to set parameters for DAP
execution during the burn.<sup>[46]</sup>

Software developers were given a budget of 10% of rope core memory and
20-30% of full computational load (3-4.5 kFLOPS) in which the DAP would have to 
operate. It would take four developers three years and 2,000 words of rope core to develop the
LM DAP software alone. A key optimization realized late in development was that a change
in coordinates used in the computations from *body axes* to *jet axes* reduced complexity
and increased performance.<sup>[6],[11]</sup>

The picture above, right shows the nonlinear switching logic used by the
Kalman filtering algorithm to control RCS jet firings in coasting flight.
With a change of a dial on the control panel, astronauts could adjust the
filter from *coarse* to *fine* control.

### AGC software testing: 60% of the whole effort
Five different levels of testing were developed.

* An all-software simulator (also known as the *all-digital* simulator)
  for the AGC, which included simulation of the *environment*.<sup>[51]</sup>
  A key concern was whether the *environment* faithfully represented the
  behavior of the real GN&C hardware and spacecraft
  including such issues as engine performance, fuel slosh and even structural
  responses of the spacecraft under torques and loads imposed by engine
  gimbaling and thruster firings. The all-digital simulation was implemented in
  MAC and Fortran on MIT mainframes and ran at 10% of real-time speed. All-digital
  simulations were bit-for-bit repeatable.
* A hybrid simulator using a real AGC together with a rope core simulator and a
  combination of digital and analog simulation of various GN&C components, the latter
  requiring two massive machine rooms in the second and third stories of the test facility.
  Hybrid simulations were not repeatable.
* System test labs using a real AGC and real GN&C sensor systems such as the IMU,
  radar and optics. These were used primarily to test AGC hardware and software
  response to noisy inputs from these components.
* Crew rehearsals with a real AGC in the actual spacecraft exercising *some* of
  the actual GN&C subsystems. As a practical matter, such tests of course could not
  include engine or thruster firings but did exercise other system components.
* Actual flight tests of the fully integrated GN&C system both in uncrewed and crewed
  flights. Early missions included several objectives designed specifically to
  test AGC software.

![](../../images/Blog_0619_agc_alldig_sim_compare_B.jpg)

In the data pictured here, data from actual flight tests of the LM descent engine
is compared with the all-digital simulation. The inner gimbal angle data agree reasonably
well (left). However, a clear bug is revealed (middle) in failure to faithfully model the outer gimbal angle
because of missing structural dynamics modeling, which was eventually corrected (right).

> The need for formal validation rose with the size of the software. Programs of 2,000 words took between 50 and 100 test runs to be fully debugged, and full-size flight program took from 1,000 to 1,200 runs.<sup>[14]</sup>

The all-digital simulation of the AGC would eventually require MIT to purchase one
Honeywell 800, two Honeywell-1800s and two IBM 360/75 peaking at about 4,500 CPU-hours/month
(equiv. H-1800 CPU-hour) testing solely for the all-digital test simulator. These hardware
testing resources together with simulator software development and test operators comprised
nearly 60% of the entire software development budget. 

### Putting the software effort in context
The whole Apollo GN&C system cost about $600M over ten years<sup>[18]</sup>. The software alone
was about 10% of that or about $60M<sup>[17]</sup>, the majority
of it occurring over the last five years. This equates to $100M/year in 2019 dollars.

> Before the first lunar landing, more than 1400 person-years of software engineering effort had been expended, with a peak level of effort of 350 engineers reached in 1968.<sup>[17],[52]</sup>

A 1972 master's thesis<sup>[17]</sup> breaks down software costs by
category shown below, left. Factoring out the *Computer* category used
almost exclusively for testing, the adjusted, relative costs of the
software development alone are shown below, right. To help keep documentation
costs down, there was even a computer-automated documentation system developed.<sup>[43]</sup>

<img src='https://github.com/betterscientificsoftware/bssw.io/raw/main/images/Blog_0619_agc_sw_costs_combined_B.jpg' class='page' />[AGC software development costs by category: left includes test hardware costs and right with hardware costs factored out.]

<br>

> In the early stages, there were no "programmers." Instead, engineers and scientists learned the techniques of programming. It was believed that competent engineers could learn programming more easily than programmers could learn engineering.<sup>[36]</sup>

We can thank Margaret Hamilton, who received the Presidential Medal of Freedom for her
work on the on AGC<sup>[16],[22]</sup>, for being the first to champion
*software engineering*<sup>[21]</sup>
as a discipline unto itself "to bring the software [effort] legitimacy so that it
and those building it would be given due respect." Hamilton was the only woman working
on AGC software and ultimately became a rope mother for the LM fight program LUMINARY.

> Throughout much of the Apollo effort, MIT experienced difficulty in estimating the time and effort requirements to design, test and verify successive mission programs.<sup>[36]</sup>

> No one doubted the quality of the software eventually produced by MIT. It was the process used in software development that caused great concern. Five lessons were identified: (1) up-to-date documentation is crucial, (2) verification must proceed through several levels, (3) requirements must be clearly defined and carefully managed, (4) good development plans should be created and executed, and (5) more programmers do not mean faster development.<sup>[14]</sup>

The Russian program achieved all of its early successes
using ground-based computers for guidance. This approach is possible
for Earth orbital flights and a single vehicle. Providing sufficiently accurate and timely
guidance for multiple vehicles or lunar missions including soft landing and return to
Earth eventually forced the Russians to begin their own digital, on-board computer
development. In August 1969, the uncrewed Russian probe Zond-7<sup>[48]</sup>
guided by an Argon-11S<sup>[44]</sup> digital computer completed the first fully
successful Russian circumlunar mission.

---

[Part 1](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap) | Part 2 | [Part 3](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-users-stories-from-space)

<br>

### Author bio

Mark C. Miller is a computer scientist supporting the
[WSC](https://wci.llnl.gov/about-us/weapon-simulation-and-computing)
program at [LLNL](https://www.llnl.gov) since 1995.
Among other things, he contributes to
[VisIt](https://wci.llnl.gov/simulation/computer-codes/visit),
[Silo](https://wci.llnl.gov/simulation/computer-codes/silo),
[HDF5](https://www.hdfgroup.org) and
[IDEAS-ECP](https://ideas-productivity.org/activities/ideas-ecp/).

<!---
Publish: yes
Track: experience
RSS update: 2019-06-17
Topics: high-performance computing (hpc), performance portability
Pinned: no
--->

[1-sfer-ezikiw]: https://github.com/betterscientificsoftware/bssw.io/raw/main/images/397_apollo_flightdiagram.jpg "Apollo flight plan diagram created by NASA in 1967 to illustrate the flight path and key mission events for the upcoming Apollo missions to the Moon. To allow our readers to explore the image in more detail we include a link to the full-res image here."
[2-sfer-ezikiw]: https://en.wikipedia.org/wiki/Gravity_of_Earth "Earth's Lumpy Gravity Field"
[3-sfer-ezikiw]: https://en.wikipedia.org/wiki/Gravitation_of_the_Moon "Moon's Lumpy Gravity Field"
[4-sfer-ezikiw]: https://www.americanscientist.org/article/moonshot-computing "Great Article on AGC Software {Hayes B.  (May 2019) Moonshot Computing. American Scientist, Vol. 107, No. 3, pages 142–147}"
[5-sfer-ezikiw]: http://www.klabs.org/history/apollo_11_alarms/eyles_2004/eyles_2004.htm "Tales from the Lunar Landing {Eyles D. (March 2018) 'SUNBURST and LUMINARY An Apollo Memoir, Fort Point Press, Boston, ISBN-13: 978-0986385902}"
[6-sfer-ezikiw]: https://www.mathworks.com/company/newsletters/articles/fly-me-to-the-moon-then-and-now.html "DAP Design Then and Now with MathWorks {Gran RJ. (1999) Fly Me to the Moon - Then and Now, webpage @ mathworks.com}"
[7-sfer-ezikiw]: https://www.ibiblio.org/apollo/index.html "Virtual AGC Project Home Page"
[8-sfer-ezikiw]: https://www.researchgate.net/publication/228517819_Architectural_Simulation_for_Exascale_HardwareSoftware_Co-design "Architectural Simulation for Exascale Hardware/Software Co-design {Janssen, Curtis & Quinlan, Dan & Shalf, John. (2019). Architectural Simulation for Exascale Hardware/Software Co-design.}"
[9-sfer-ezikiw]: https://www.design-reuse.com/articles/31951/the-power-of-developing-hardware-and-software-in-parallel.html "The Power of Developing Hardware and Software in Parallel {De Schutter T. (~2012) The Power of Developing Hardware and Software in Parallel, webpage @ design-reuse.com}"
[10-sfer-ezikiw]: http://web.mit.edu/digitalapollo/Documents/Chapter6/hoagprogreport.pdf?#page=24 "Hoag Report including DAP Design and Performance {Hoag DG. (April 1969) Apollo Navigation, Guidance and Control Systems: A Progress Report, MIT-IL E-2411}"
[11-sfer-ezikiw]: https://www.mathworks.com/help/simulink/slref/developing-the-apollo-lunar-module-digital-autopilot.html "MathWorks Model of DAP"
[12-sfer-ezikiw]: http://www.ibiblio.org/apollo/hrst/archive/1695.pdf "AGC Software Development Plan {Wilson RE., Copps E. et al (October 1967) Apollo Guidance Software Development and Verification Plan, 43 pages}"
[13-sfer-ezikiw]: https://www.ibiblio.org/apollo/hrst/archive/1687.pdf?#page=40 "Example AGC Interpretive Program To Find Quadratic Roots {Muntz CA. (1965) User's Guide to the Block II AGC/LGC Interpreter, MIT-IL, R-489, 70 pages}"
[14-sfer-ezikiw]: https://history.nasa.gov/computers/Ch2-6.html "Overview of Software Development Issues {Kent A, Williams JG (~1987) Computers in Spaceflight: The NASA Experience, web pages}"
[15-sfer-ezikiw]: https://www.airspacemag.com/space/practicing-safe-software-180962744/ "Air & Space Article on Mariner 1 {Goodman B, (August 1994) Practicing Safe Software Smithsonian Air and Space Magazine, p. 60}"
[16-sfer-ezikiw]: https://authors.library.caltech.edu/5456/1/hrst.mit.edu/hrs/apollo/public/conference1/hamilton-intro.htm "Transcript of Interview with Margaret Hamilton"
[17-sfer-ezikiw]: https://www.ibiblio.org/apollo/hrst/archive/1728.pdf "AGC Software Development Productivity and Costs {Rankin DA. (1972) A Model of the Cost of Software Development for the Apollo Spacecraft Computer, Masters Thesis, MIT}"
[18-sfer-ezikiw]: https://history.nasa.gov/SP-4029/Apollo_18-16_Apollo_Program_Budget_Appropriations.htm "Apollo Budget By Sub-Program and Year"
[19-sfer-ezikiw]: https://www.ibiblio.org/apollo/Documents/SGA_Memo11_620716.pdf "List of Software Studies Underway in 1962 {Battin RH (July 1962) SGA Studies Presently Underway, Space Guidance Analysis Memo #11, MIT-IL, 9 pages}"
[20-sfer-ezikiw]: https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap "Part 1 in this series"
[21-sfer-ezikiw]: https://www.computer.org/publications/tech-news/events/what-to-know-about-the-scientist-who-invented-the-term-software-engineering "Origin of the term 'Software Engineering' {Cameron L () What to Know about the Scientist who Invented the term 'Software Engineering', IEEE Computer Society webpage}"
[22-sfer-ezikiw]: https://www.nasa.gov/feature/margaret-hamilton-apollo-software-engineer-awarded-presidential-medal-of-freedom "Margaret Hamilton Medal of Freedom {Russo NP (November 2016) Margaret Hamilton, Apollo Software Engineer, Awarded Presidential Medal of Freedom, NASA History Division webpage}"
[23-sfer-ezikiw]: https://www.google.com/search?client=safari&rls=en&ei=YeryXMO2H6m_0PEPvciWiA8&q=what+is+co-design+in+computing&oq=what+is&gs_l=psy-ab.1.0.35i39l2j0i67l5j0l2j0i131.1499.3009..4244...2.0..0.121.836.5j4......0....1..gws-wiz.......0i71j0i10j0i10i67.bQxpLbPTVwU "Google Search co-design in computing"
[24-sfer-ezikiw]: https://www.ibiblio.org/apollo/AGC-versions.jpg "AGC Software Version History"
[25-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Luminary069/EXECUTIVE.agc "AGC source code for Executive"
[26-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Luminary069/WAITLIST.agc "AGC source code for Waitlist"
[27-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Luminary069/INTERPRETER.agc "AGC source code for Interpreter"
[28-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Luminary069/PINBALL_GAME__BUTTONS_AND_LIGHTS.agc "AGC source code for DSKY and cockpit displays"
[29-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Luminary069/DOWN-TELEMETRY_PROGRAM.agc "AGC source code for Downlink"
[30-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Luminary069/FRESH_START_AND_RESTART.agc "AGC source code for restart"
[31-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Luminary069/RESTARTS_ROUTINE.agc "AGC source code for Interpretive routine restart"
[32-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Luminary069/RESTART_TABLES.agc "AGC source code for restart phase tables"
[33-sfer-ezikiw]: https://www.spaceartifactsarchive.com/2013/05/the-star-chart-of-apollo.html "Apollo space sextant {McGlynn L (May 2013) Star Charts of Apollo webpage}"
[34-sfer-ezikiw]: https://www.ibiblio.org/apollo/Documents/SGA_Memo12_620716.pdf "Position of Moon analysis {Potter JE (July 1962) Storing Position of Moon, Space Guidance Analysis Memo #12, MIT-IL, 7 pages}"
[35-sfer-ezikiw]: https://en.wikipedia.org/wiki/Mariner_1 "Overview of Mariner 1"
[36-sfer-ezikiw]: https://ocw.mit.edu/courses/science-technology-and-society/sts-471j-engineering-apollo-the-moon-project-as-a-complex-system-spring-2007/readings/1_4_9_mit_role.pdf "MIT's Role in The Apollo Project: The Software Effort (Volume V) {Johnson MS Giller DR (1971) MIT's Role in the Project: Final Report on Contracts, Vol. 5 The Software Effort, NAS 9-153 & NAS 9-4065}"
[37-sfer-ezikiw]: https://en.wikipedia.org/wiki/Lunar_orbit_rendezvous "Description of Lunar Orbit Rendezvous (LOR)"
[38-sfer-ezikiw]: https://theagileadmin.com/what-is-devops/ "What is DevOps?"
[39-sfer-ezikiw]: https://history.nasa.gov/computers/Ch2-5.html "Computers in Spaceflight {Kent A, Williams JG (~1987) Computers in Spaceflight: The NASA Experience, web pages}"
[40-sfer-ezikiw]: https://en.wikipedia.org/wiki/List_of_Apollo_missions "List of Apollo Flights"
[41-sfer-ezikiw]: https://github.com/virtualagc/virtualagc/blob/master/Colossus249/STAR_TABLES.agc "AGC source code for star tables"
[42-sfer-ezikiw]: https://en.wikipedia.org/wiki/Kalman_filter "Description of Kalman filter"
[43-sfer-ezikiw]: https://www.ibiblio.org/apollo/hrst/archive/1719.pdf "Automatic Documentation System {Dunbar JC, Larson RA, Augart PT (May 1966) An Automated Documentation Technique for Integrating Apollo Crew Procedures and Computer Logic, MIT-IL, E-1956}"
[44-sfer-ezikiw]: http://web.mit.edu/slava/space/introduction.htm "Russian Argon-11S Guidance Computer"
[45-sfer-ezikiw]: https://www.ibiblio.org/apollo/CMC_data_cards_15_Fabrizio_Bernardini.pdf?#page=25 "AGC CM Major Mode Programs"
[46-sfer-ezikiw]: https://www.ibiblio.org/apollo/CMC_data_cards_15_Fabrizio_Bernardini.pdf?#page=31 "AGC CM DAP Configuration"
[47-sfer-ezikiw]: https://www.ibiblio.org/apollo/CMC_data_cards_15_Fabrizio_Bernardini.pdf?#page=29 "AGC CM Star Names"
[48-sfer-ezikiw]: https://en.wikipedia.org/wiki/Zond_7 "Russian Zond-7 Mission"
[49-sfer-ezikiw]: https://en.wikipedia.org/wiki/Fly-by-wire#Digital_systems "Description of Fly By Wire"
[50-sfer-ezikiw]: http://www.gravityassist.com/IAF-3.3%202010/Ref.%203-230.pdf "MIT Algebraic Compiler (MAC) Language {Laning, J.H., Jr. and Miller, J.S., (1970), MIT Instrumentation Laboratory report R-681, (MIT Charles Stark Draper Laboratory, Report R-681) Cambridge, Mass., November 1970}"
[51-sfer-ezikiw]: https://www.ibiblio.org/apollo/hrst/archive/1678.pdf "A Comprehensive Digital Simulation for the Verification of Apollo Flight Software {Glick FK, Femino SR (January, 1970) MIT-IL Report E-2475, 31 pages}"
[52-sfer-ezikiw]: http://web.mit.edu/aeroastro/news/magazine/aeroastro6/mit-apollo.html "MIT and navigating a path to the moon {AeroAstro Magazine annual report of the MIT Aeronautics and Astronautics Department}"
<!-- DO NOT EDIT BELOW HERE. THIS IS ALL AUTO-GENERATED (sfer-ezikiw) -->
[1]: #sfer-ezikiw-1 "Apollo flight plan diagram created by NASA in 1967 to illustrate the flight path and key mission events for the upcoming Apollo missions to the Moon. To allow our readers to explore the image in more detail we include a link to the full-res image here."
[2]: #sfer-ezikiw-2 "Earth's Lumpy Gravity Field"
[3]: #sfer-ezikiw-3 "Moon's Lumpy Gravity Field"
[4]: #sfer-ezikiw-4 "Great Article on AGC Software"
[5]: #sfer-ezikiw-5 "Tales from the Lunar Landing"
[6]: #sfer-ezikiw-6 "DAP Design Then and Now with MathWorks"
[7]: #sfer-ezikiw-7 "Virtual AGC Project Home Page"
[8]: #sfer-ezikiw-8 "Architectural Simulation for Exascale Hardware/Software Co-design"
[9]: #sfer-ezikiw-9 "The Power of Developing Hardware and Software in Parallel"
[10]: #sfer-ezikiw-10 "Hoag Report including DAP Design and Performance"
[11]: #sfer-ezikiw-11 "MathWorks Model of DAP"
[12]: #sfer-ezikiw-12 "AGC Software Development Plan"
[13]: #sfer-ezikiw-13 "Example AGC Interpretive Program To Find Quadratic Roots"
[14]: #sfer-ezikiw-14 "Overview of Software Development Issues"
[15]: #sfer-ezikiw-15 "Air & Space Article on Mariner 1"
[16]: #sfer-ezikiw-16 "Transcript of Interview with Margaret Hamilton"
[17]: #sfer-ezikiw-17 "AGC Software Development Productivity and Costs"
[18]: #sfer-ezikiw-18 "Apollo Budget By Sub-Program and Year"
[19]: #sfer-ezikiw-19 "List of Software Studies Underway in 1962"
[20]: #sfer-ezikiw-20 "Part 1 in this series"
[21]: #sfer-ezikiw-21 "Origin of the term 'Software Engineering'"
[22]: #sfer-ezikiw-22 "Margaret Hamilton Medal of Freedom"
[23]: #sfer-ezikiw-23 "Google Search co-design in computing"
[24]: #sfer-ezikiw-24 "AGC Software Version History"
[25]: #sfer-ezikiw-25 "AGC source code for Executive"
[26]: #sfer-ezikiw-26 "AGC source code for Waitlist"
[27]: #sfer-ezikiw-27 "AGC source code for Interpreter"
[28]: #sfer-ezikiw-28 "AGC source code for DSKY and cockpit displays"
[29]: #sfer-ezikiw-29 "AGC source code for Downlink"
[30]: #sfer-ezikiw-30 "AGC source code for restart"
[31]: #sfer-ezikiw-31 "AGC source code for Interpretive routine restart"
[32]: #sfer-ezikiw-32 "AGC source code for restart phase tables"
[33]: #sfer-ezikiw-33 "Apollo space sextant"
[34]: #sfer-ezikiw-34 "Position of Moon analysis"
[35]: #sfer-ezikiw-35 "Overview of Mariner 1"
[36]: #sfer-ezikiw-36 "MIT's Role in The Apollo Project: The Software Effort (Volume V)"
[37]: #sfer-ezikiw-37 "Description of Lunar Orbit Rendezvous (LOR)"
[38]: #sfer-ezikiw-38 "What is DevOps?"
[39]: #sfer-ezikiw-39 "Computers in Spaceflight"
[40]: #sfer-ezikiw-40 "List of Apollo Flights"
[41]: #sfer-ezikiw-41 "AGC source code for star tables"
[42]: #sfer-ezikiw-42 "Description of Kalman filter"
[43]: #sfer-ezikiw-43 "Automatic Documentation System"
[44]: #sfer-ezikiw-44 "Russian Argon-11S Guidance Computer"
[45]: #sfer-ezikiw-45 "AGC CM Major Mode Programs"
[46]: #sfer-ezikiw-46 "AGC CM DAP Configuration"
[47]: #sfer-ezikiw-47 "AGC CM Star Names"
[48]: #sfer-ezikiw-48 "Russian Zond-7 Mission"
[49]: #sfer-ezikiw-49 "Description of Fly By Wire"
[50]: #sfer-ezikiw-50 "MIT Algebraic Compiler (MAC) Language"
[51]: #sfer-ezikiw-51 "A Comprehensive Digital Simulation for the Verification of Apollo Flight Software"
[52]: #sfer-ezikiw-52 "MIT and navigating a path to the moon"
<!-- (sfer-ezikiw begin) -->
### References
<!-- (sfer-ezikiw end) -->
* <a name="sfer-ezikiw-1"></a><sup>1</sup>[Apollo flight plan diagram created by NASA in 1967 to illustrate the flight path and key mission events for the upcoming Apollo missions to the Moon. To allow our readers to explore the image in more detail we include a link to the full-res image here.](https://github.com/betterscientificsoftware/bssw.io/raw/main/images/397_apollo_flightdiagram.jpg)
* <a name="sfer-ezikiw-2"></a><sup>2</sup>[Earth's Lumpy Gravity Field](https://en.wikipedia.org/wiki/Gravity_of_Earth)
* <a name="sfer-ezikiw-3"></a><sup>3</sup>[Moon's Lumpy Gravity Field](https://en.wikipedia.org/wiki/Gravitation_of_the_Moon)
* <a name="sfer-ezikiw-4"></a><sup>4</sup>[Great Article on AGC Software<br>Hayes B.  (May 2019) Moonshot Computing. American Scientist, Vol. 107, No. 3, pages 142–147](https://www.americanscientist.org/article/moonshot-computing)
* <a name="sfer-ezikiw-5"></a><sup>5</sup>[Tales from the Lunar Landing<br>Eyles D. (March 2018) 'SUNBURST and LUMINARY An Apollo Memoir, Fort Point Press, Boston, ISBN-13: 978-0986385902](http://www.klabs.org/history/apollo_11_alarms/eyles_2004/eyles_2004.htm)
* <a name="sfer-ezikiw-6"></a><sup>6</sup>[DAP Design Then and Now with MathWorks<br>Gran RJ. (1999) Fly Me to the Moon - Then and Now, webpage @ mathworks.com](https://www.mathworks.com/company/newsletters/articles/fly-me-to-the-moon-then-and-now.html)
* <a name="sfer-ezikiw-7"></a><sup>7</sup>[Virtual AGC Project Home Page](https://www.ibiblio.org/apollo/index.html)
* <a name="sfer-ezikiw-8"></a><sup>8</sup>[Architectural Simulation for Exascale Hardware/Software Co-design<br>Janssen, Curtis & Quinlan, Dan & Shalf, John. (2019). Architectural Simulation for Exascale Hardware/Software Co-design.](https://www.researchgate.net/publication/228517819_Architectural_Simulation_for_Exascale_HardwareSoftware_Co-design)
* <a name="sfer-ezikiw-9"></a><sup>9</sup>[The Power of Developing Hardware and Software in Parallel<br>De Schutter T. (~2012) The Power of Developing Hardware and Software in Parallel, webpage @ design-reuse.com](https://www.design-reuse.com/articles/31951/the-power-of-developing-hardware-and-software-in-parallel.html)
* <a name="sfer-ezikiw-10"></a><sup>10</sup>[Hoag Report including DAP Design and Performance<br>Hoag DG. (April 1969) Apollo Navigation, Guidance and Control Systems: A Progress Report, MIT-IL E-2411](http://web.mit.edu/digitalapollo/Documents/Chapter6/hoagprogreport.pdf?#page=24)
* <a name="sfer-ezikiw-11"></a><sup>11</sup>[MathWorks Model of DAP](https://www.mathworks.com/help/simulink/slref/developing-the-apollo-lunar-module-digital-autopilot.html)
* <a name="sfer-ezikiw-12"></a><sup>12</sup>[AGC Software Development Plan<br>Wilson RE., Copps E. et al (October 1967) Apollo Guidance Software Development and Verification Plan, 43 pages](http://www.ibiblio.org/apollo/hrst/archive/1695.pdf)
* <a name="sfer-ezikiw-13"></a><sup>13</sup>[Example AGC Interpretive Program To Find Quadratic Roots<br>Muntz CA. (1965) User's Guide to the Block II AGC/LGC Interpreter, MIT-IL, R-489, 70 pages](https://www.ibiblio.org/apollo/hrst/archive/1687.pdf?#page=40)
* <a name="sfer-ezikiw-14"></a><sup>14</sup>[Overview of Software Development Issues<br>Kent A, Williams JG (~1987) Computers in Spaceflight: The NASA Experience, web pages](https://history.nasa.gov/computers/Ch2-6.html)
* <a name="sfer-ezikiw-15"></a><sup>15</sup>[Air & Space Article on Mariner 1<br>Goodman B, (August 1994) Practicing Safe Software Smithsonian Air and Space Magazine, p. 60](https://www.airspacemag.com/space/practicing-safe-software-180962744/)
* <a name="sfer-ezikiw-16"></a><sup>16</sup>[Transcript of Interview with Margaret Hamilton](https://authors.library.caltech.edu/5456/1/hrst.mit.edu/hrs/apollo/public/conference1/hamilton-intro.htm)
* <a name="sfer-ezikiw-17"></a><sup>17</sup>[AGC Software Development Productivity and Costs<br>Rankin DA. (1972) A Model of the Cost of Software Development for the Apollo Spacecraft Computer, Masters Thesis, MIT](https://www.ibiblio.org/apollo/hrst/archive/1728.pdf)
* <a name="sfer-ezikiw-18"></a><sup>18</sup>[Apollo Budget By Sub-Program and Year](https://history.nasa.gov/SP-4029/Apollo_18-16_Apollo_Program_Budget_Appropriations.htm)
* <a name="sfer-ezikiw-19"></a><sup>19</sup>[List of Software Studies Underway in 1962<br>Battin RH (July 1962) SGA Studies Presently Underway, Space Guidance Analysis Memo #11, MIT-IL, 9 pages](https://www.ibiblio.org/apollo/Documents/SGA_Memo11_620716.pdf)
* <a name="sfer-ezikiw-20"></a><sup>20</sup>[Part 1 in this series](https://bssw.io/blog_posts/celebrating-apollo-s-50th-anniversary-when-100-flops-watt-was-a-giant-leap)
* <a name="sfer-ezikiw-21"></a><sup>21</sup>[Origin of the term 'Software Engineering'<br>Cameron L () What to Know about the Scientist who Invented the term 'Software Engineering', IEEE Computer Society webpage](https://www.computer.org/publications/tech-news/events/what-to-know-about-the-scientist-who-invented-the-term-software-engineering)
* <a name="sfer-ezikiw-22"></a><sup>22</sup>[Margaret Hamilton Medal of Freedom<br>Russo NP (November 2016) Margaret Hamilton, Apollo Software Engineer, Awarded Presidential Medal of Freedom, NASA History Division webpage](https://www.nasa.gov/feature/margaret-hamilton-apollo-software-engineer-awarded-presidential-medal-of-freedom)
* <a name="sfer-ezikiw-23"></a><sup>23</sup>[Google Search co-design in computing](https://www.google.com/search?client=safari&rls=en&ei=YeryXMO2H6m_0PEPvciWiA8&q=what+is+co-design+in+computing&oq=what+is&gs_l=psy-ab.1.0.35i39l2j0i67l5j0l2j0i131.1499.3009..4244...2.0..0.121.836.5j4......0....1..gws-wiz.......0i71j0i10j0i10i67.bQxpLbPTVwU)
* <a name="sfer-ezikiw-24"></a><sup>24</sup>[AGC Software Version History](https://www.ibiblio.org/apollo/AGC-versions.jpg)
* <a name="sfer-ezikiw-25"></a><sup>25</sup>[AGC source code for Executive](https://github.com/virtualagc/virtualagc/blob/master/Luminary069/EXECUTIVE.agc)
* <a name="sfer-ezikiw-26"></a><sup>26</sup>[AGC source code for Waitlist](https://github.com/virtualagc/virtualagc/blob/master/Luminary069/WAITLIST.agc)
* <a name="sfer-ezikiw-27"></a><sup>27</sup>[AGC source code for Interpreter](https://github.com/virtualagc/virtualagc/blob/master/Luminary069/INTERPRETER.agc)
* <a name="sfer-ezikiw-28"></a><sup>28</sup>[AGC source code for DSKY and cockpit displays](https://github.com/virtualagc/virtualagc/blob/master/Luminary069/PINBALL_GAME__BUTTONS_AND_LIGHTS.agc)
* <a name="sfer-ezikiw-29"></a><sup>29</sup>[AGC source code for Downlink](https://github.com/virtualagc/virtualagc/blob/master/Luminary069/DOWN-TELEMETRY_PROGRAM.agc)
* <a name="sfer-ezikiw-30"></a><sup>30</sup>[AGC source code for restart](https://github.com/virtualagc/virtualagc/blob/master/Luminary069/FRESH_START_AND_RESTART.agc)
* <a name="sfer-ezikiw-31"></a><sup>31</sup>[AGC source code for Interpretive routine restart](https://github.com/virtualagc/virtualagc/blob/master/Luminary069/RESTARTS_ROUTINE.agc)
* <a name="sfer-ezikiw-32"></a><sup>32</sup>[AGC source code for restart phase tables](https://github.com/virtualagc/virtualagc/blob/master/Luminary069/RESTART_TABLES.agc)
* <a name="sfer-ezikiw-33"></a><sup>33</sup>[Apollo space sextant<br>McGlynn L (May 2013) Star Charts of Apollo webpage](https://www.spaceartifactsarchive.com/2013/05/the-star-chart-of-apollo.html)
* <a name="sfer-ezikiw-34"></a><sup>34</sup>[Position of Moon analysis<br>Potter JE (July 1962) Storing Position of Moon, Space Guidance Analysis Memo #12, MIT-IL, 7 pages](https://www.ibiblio.org/apollo/Documents/SGA_Memo12_620716.pdf)
* <a name="sfer-ezikiw-35"></a><sup>35</sup>[Overview of Mariner 1](https://en.wikipedia.org/wiki/Mariner_1)
* <a name="sfer-ezikiw-36"></a><sup>36</sup>[MIT's Role in The Apollo Project: The Software Effort (Volume V)<br>Johnson MS Giller DR (1971) MIT's Role in the Project: Final Report on Contracts, Vol. 5 The Software Effort, NAS 9-153 & NAS 9-4065](https://ocw.mit.edu/courses/science-technology-and-society/sts-471j-engineering-apollo-the-moon-project-as-a-complex-system-spring-2007/readings/1_4_9_mit_role.pdf)
* <a name="sfer-ezikiw-37"></a><sup>37</sup>[Description of Lunar Orbit Rendezvous (LOR)](https://en.wikipedia.org/wiki/Lunar_orbit_rendezvous)
* <a name="sfer-ezikiw-38"></a><sup>38</sup>[What is DevOps?](https://theagileadmin.com/what-is-devops/)
* <a name="sfer-ezikiw-39"></a><sup>39</sup>[Computers in Spaceflight<br>Kent A, Williams JG (~1987) Computers in Spaceflight: The NASA Experience, web pages](https://history.nasa.gov/computers/Ch2-5.html)
* <a name="sfer-ezikiw-40"></a><sup>40</sup>[List of Apollo Flights](https://en.wikipedia.org/wiki/List_of_Apollo_missions)
* <a name="sfer-ezikiw-41"></a><sup>41</sup>[AGC source code for star tables](https://github.com/virtualagc/virtualagc/blob/master/Colossus249/STAR_TABLES.agc)
* <a name="sfer-ezikiw-42"></a><sup>42</sup>[Description of Kalman filter](https://en.wikipedia.org/wiki/Kalman_filter)
* <a name="sfer-ezikiw-43"></a><sup>43</sup>[Automatic Documentation System<br>Dunbar JC, Larson RA, Augart PT (May 1966) An Automated Documentation Technique for Integrating Apollo Crew Procedures and Computer Logic, MIT-IL, E-1956](https://www.ibiblio.org/apollo/hrst/archive/1719.pdf)
* <a name="sfer-ezikiw-44"></a><sup>44</sup>[Russian Argon-11S Guidance Computer](http://web.mit.edu/slava/space/introduction.htm)
* <a name="sfer-ezikiw-45"></a><sup>45</sup>[AGC CM Major Mode Programs](https://www.ibiblio.org/apollo/CMC_data_cards_15_Fabrizio_Bernardini.pdf?#page=25)
* <a name="sfer-ezikiw-46"></a><sup>46</sup>[AGC CM DAP Configuration](https://www.ibiblio.org/apollo/CMC_data_cards_15_Fabrizio_Bernardini.pdf?#page=31)
* <a name="sfer-ezikiw-47"></a><sup>47</sup>[AGC CM Star Names](https://www.ibiblio.org/apollo/CMC_data_cards_15_Fabrizio_Bernardini.pdf?#page=29)
* <a name="sfer-ezikiw-48"></a><sup>48</sup>[Russian Zond-7 Mission](https://en.wikipedia.org/wiki/Zond_7)
* <a name="sfer-ezikiw-49"></a><sup>49</sup>[Description of Fly By Wire](https://en.wikipedia.org/wiki/Fly-by-wire#Digital_systems)
* <a name="sfer-ezikiw-50"></a><sup>50</sup>[MIT Algebraic Compiler (MAC) Language<br>Laning, J.H., Jr. and Miller, J.S., (1970), MIT Instrumentation Laboratory report R-681, (MIT Charles Stark Draper Laboratory, Report R-681) Cambridge, Mass., November 1970](http://www.gravityassist.com/IAF-3.3%202010/Ref.%203-230.pdf)
* <a name="sfer-ezikiw-51"></a><sup>51</sup>[A Comprehensive Digital Simulation for the Verification of Apollo Flight Software<br>Glick FK, Femino SR (January, 1970) MIT-IL Report E-2475, 31 pages](https://www.ibiblio.org/apollo/hrst/archive/1678.pdf)
* <a name="sfer-ezikiw-52"></a><sup>52</sup>[MIT and navigating a path to the moon<br>AeroAstro Magazine annual report of the MIT Aeronautics and Astronautics Department](http://web.mit.edu/aeroastro/news/magazine/aeroastro6/mit-apollo.html)
