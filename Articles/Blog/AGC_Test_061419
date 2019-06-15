<!--- WARNING: DO NOT EDIT! Auto-generated with wikize_refs.py from ApolloGuidanceComputerPart2.md --->
# Test Version: The Oldest Code on GitHub

**Hero Image:**

 - <img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0615_Apollo2.jpg' />

#### Contributed by [Mark C. Miller](https://github.com/markcmiller86)
#### Publication date: June 14, 2019

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

This is the second of three articles about the AGC. In part 1, we described the
hardware.<sup>[20]</sup> Here, in part 2, we focus on MIT's effort to develop
the software.<sup>[4],[12],[36]</sup>
As in part 1, the scientific computing community will recognize
some familiar themes such as the benefits and challenges of *co-design*, the importance of
sufficient testing resources, the role and impact of software process
improvements and more.

### Extreme Co-design
Initially, about all that was known with any certainty was that a digital
computer would be the centerpiece of a complex collection of GN&C subsystems.
A year would pass before NASA selected the Lunar Orbit
Rendezvous<sup>[37]</sup> (LOR) mission plan involving two separate
and substantially different vehicles each with its own AGC.
AGC software would control everything. Even so-called manually controlled inputs would first
pass through AGC software before affecting the relevant hardware. 

<br> 

<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0619_agc_and_spacecraft3_B.jpg' class='page' />

<br> 

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
But, in the 1960s where there were no DevOps<sup>[38]</sup> best practices and collaborative tools
such as GitLab, Jenkins, Confluence, Kanban and WebEx, or even email, it presented a massive
coordination and management challenge.

### Evolving requirements, versions and flight rope releases
> NASA had established a need for the machine and had determined its general tasks, and
> MIT received a contract based on only a short, very general requirements statement.
> Requirements started changing immediately and continued to change throughout the program.<sup>[39]</sup>

Midway through development, the AGC was redesigned to support more memory and an expanded
instruction set.
They were different enough that each required separate software development teams, a situation that
only worsened already strained resources.
The redesigned AGC had only 2K words of *erasable* core and 36K words of *fixed*
or *rope core* memory. All software and data had to fit into this combined 76KB of memory.

**The essential step for software developers was to produce a *flight program* or *rope*
and release it to Raytheon for rope core  manufacture approximately 4 months prior to launch:
2 months to manufacture the ropes followed by 2 months for installation in the spacecraft,
checkout, integrated system testing, crew rehearsals and final erasable memory load.**

MIT needed to deliver flight programs for ~30 Apollo flights (crewed and uncrewed),
many with unique guidance requirements, planned between 1966 and 1972.<sup>[40]</sup>
The lead engineer in coordinating and approving a completed flight program was
called a *rope mother* and would also name the release. Early on, the names were fairly
creative, including **ECLIPSE**, **SUNRISE**, **RETREAD** and **AURORA**. Eventually,
NASA put a stop to this, and only the names **COLOSSUS** and **LUMINARY** together
with their revision numbers would be used to identify CM and LM flight programs,
respectively.<sup>[24]</sup> **LUMINARY 1A** is the revision used in the first lunar
landing of Apollo 11.

### The AGC software stack
Each flight program involved a combination of common utilities and mission-specific
space guidance subroutines. Mission-specific components required significant
analysis and development time. Early development activity, 1961-1965, focused on
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

<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0619_agc_sw_stack2_B.jpg' class='page' />

<br> 

These programs constituted what we might call today the *Apollo guidance software stack*.
All were implemented in assembly language. By 1965, most of this code had been
written and fully tested and changed little with each new flight program. All
higher level space guidance routines were implemented primarily in the Interpreter
language<sup>[13]</sup> but also by using some of these lower-level pieces.

An example of a space guidance subroutine is computing the relative positions of Earth,
Sun and Moon at any moment. After evaluating options<sup>[34]</sup> in MAC Fortran on 
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
Flying to the moon and returning safely involved *long periods of boredom
punctuated by moments of extreme peril*. A mission was divided into phases by
*velocity change maneuvers* or *burns* of the main engines<sup>[1]</sup>. A complete mission
involved around 11 burns. For each maneuver
there was a corresponding *major mode program*, to handle it.
For every phase of the mission, *the AGC had an app for that*.<sup>[45]</sup>

By far the most critical sequence of maneuvers occurred during lunar landing.
It was divided into four phases (pictured below left) depending on the balance of
automated and manual control the astronauts required: Powered Descent
(major mode P63), Approach (P64), Terminal Descent (P66) and Touchdown (P68).<sup>[5]</sup>
Examples of other mode mode programs were Trans Lunar Injection (P15), 
Return To Earth (P37), Ballistic Re-entry (P66).

Development of a major mode program began with an analysis of the relevant equations
of motion and an assessment of available computational approaches to affect the
desired velocity change (magnitude and direction) subject to numerous constraints
including zero gravity fuel slosh; changing center of mass due to fuel consumption;
main engine performance characteristics; sensor drift and deadbands (e.g. IMU gimbal lock);
optimizing use of propellants; contingency logic for failed (on or off) RCS thrusters;
the Moon's lump gravity field;<sup>[2],[3]</sup> and precision timing to coordinate
a planetary ballet of Earth, Moon Sun and multiple spacecraft and the lines of sight
of communications between them and mission control.

<br>

<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0619_agc_major_modes_B.jpg' class='page' />

<br>

### Performance portability and the digital autopilot (DAP)

Digital Autopilot (DAP) software was developed based on *Kalman Filtering*.<sup>[42]</sup>
The computation is decomposed into a *prediction* phase where an idealized model
of the spacecraft is used to estimate the current state. In the second phase, noisy
direct measurement of system state from spacecraft sensors is compared with the
predicted state to produce control decisions.

A key challenge was ensuring that a single implementation of DAP software would provide
effective control given a variety of spacecraft configurations and operating
scenarios. Doing so presented what we would call a *performance portability*
problem.<sup>[10]</sup> Software developers made DAP execution configurable through a
number of parameters. Prior to a burn, astronauts would follow a checklist setting
a number of switches and entering data on the DSKY to set parameters for the DAP
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
  for the AGC itself, which included simulation of the *environment*.
  A key concern was whether the *environment* faithfully represented the
  behavior of the real GN&C hardware and spacecraft in which it was housed,
  including such issues as engine performance, fuel slosh and even structural
  responses of the spacecraft under torques and loads imposed by engine
  gimbaling and thruster firings. The all-digital simulation was implemented in
  MAC Fortran on MIT mainframes and ran at 10% of real-time speed. All-digital
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

<br>

<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0619_agc_alldig_sim_compare_B.jpg' class='page' />

<br>


In the data pictured here, data from actual flight tests of the LM descent engine
is compared with the all-digital simulation. The inner gimbal angle data agree reasonbly
well (left). However, a clear bug is revealed (middle) in failure to faithfully model the outer gimbal angle
because of missing structural dynamics modeling, which was eventually corrected (right).

> The need for formal validation rose with the size of the software. Programs of
> 2,000 words took between 50 and 100 test runs to be fully debugged, and
> full-size flight program took from 1,000 to 1,200 runs.

The all-digital simulation of the AGC would eventually require MIT to purchase one
Honeywell 800, two Honeywell-1800s and two IBM 360/75 peaking at about 4,500 CPU-hours/month
(equiv. H-1800 CPU-hour) testing solely for the all-digital test simulator. These hardware
testing resources together with simulator software development and test operators comprised
nearly 60% of the entire software development budget. 

### Putting the software effort in context
The software effort was about $60M<sup>[17],[18]</sup> ($500M in 2019 dollars), the majority
of it occurring over the last five years or about $100M/year in 2019 dollars.
By comparison, the Exascale Computing Project budget for 2019 is projected to be
$809M, an overwhelming majority of which is not software suggesting that the AGC software
effort was on par with the ECP program.

> Before the first lunar landing, more than 1400 person-years of software
> engineering effort had been expended, with a peak level of effort of 350
> engineers reached in 1968.

A 1972 master's thesis<sup>[17]</sup> breaks down software costs by
category shown below, left. Factoring out the *Computer* category used
almost exclusively for testing, the adjusted, relative costs of the
software development alone are shown below, right. To help keep documentation
costs down, there was even a computer-automated documentation system developed.<sup>[43]</sup>

<br>

<img src='https://github.com/betterscientificsoftware/images/raw/master/Blog_0619_agc_sw_costs_combined_B.jpg' class='page' />

<br>

> In the early stages, there were no "programmers." Instead, engineers and scientists
> learned the techniques of programming. It was believed that competent engineers could
> learn programming more easily than programmers could learn engineering.<sup>[36]</sup>

We can thank Margaret Hamilton, who received the Presidential Medal of Freedom for her
work on the on AGC<sup>[16],[22]</sup>, for being the first to champion
*software engineering*<sup>[21]</sup>
as a discipline unto itself "to bring the software [effort] legitimacy so that it
and those building it would be given due respect." Hamilton was the only woman working
on AGC software and ultimately became a rope mother for the LM fight program **LUMINARY**.

> Throughout much of the Apollo effort, MIT experienced difficulty in estimating the
> time and effort requirements to design, test and verify successive mission programs.<sup>[36]</sup>
>
> No one doubted the quality of the software eventually produced by MIT. It was the
> process used in software development that caused great concern. Five lessons were identified:
> (1) up-to-date documentation is crucial, (2) verification must proceed through
> several levels, (3) requirements must be clearly defined and carefully managed,
> (4) good development plans should be created and executed, and (5) more programmers
> do not mean faster development.<sup>[14]</sup>

The Russian program achieved all of its early successes
using ground-based computers for guidance. This approach is possible
for Earth orbital flights and a single vehicle. Providing sufficiently accurate and timely
guidance for multiple vehicles or lunar missions including soft landing and return to
Earth eventually forced the Russians to begin their own digital, on-board computer
development. In August 1969, the uncrewed Russian probe Zond-7<sup>[48]</sup>
guided by an Argon-11S<sup>[44]</sup> digital computer completed the first fully
successful Russian circumlunar mission.

<!---
Publish: preview
Categories: performance
Topics: high-performance computing, performance portability
Tags: bssw-blog-article
Level: 2
Prerequisites: default
Aggregate: none
--->

